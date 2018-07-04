# Settings Refactoring

# Major Tasks/Missing Features

## The Admin Webapp Does Not Work.

On the one hand, Heritrix can now be controlled remotely via JMX, so
anything you could do via the webapp can now be done via jconsole. Also,
it is mostly trivial to add additional JMX operations per module (see
kickUpdate thoughts below) if necessary.

But, that means the webapp needs to speak JMX in order to control
Heritrix, as there is no longer another way. I'd prefer it if the webapp
were its own standalone project in the source tree.

## The Merge

Changes to trunk must be merged in with changes in my branch. Since so
many packages/classes moved around, I think the easiest thing to do here
would be to generate per-package diffs of trunk's code, merge them in to
pjack\_settings separately, then do an svn move to make pjack\_settings
the new trunk.

## Intermittent BDB Corruption During CheckpointSelfTest.

One of my unit tests occassionally raises a DatabaseException trying to
find the cap of a Frontier queue.

## Missing/altered DecideRules Need to be Restored.

This is outstanding from previous discussions. I had modified DecideRule
to include an "invert" setting, which was widely regarded as a bad move.
I did this to eliminate as many DecideRules as possible, since there are
many of them.

A different way to eliminate some DecideRules would be to add two rules
that handle most operations on CrawlURI fields. So there would be a
"CrawlURIFieldDecideRule" and a "NotCrawlURIFieldDecideRule" that would
let an operator pick a CrawlURI field (or enter an arbitrary attribute
name), pick an operation (is exactly, starts with, ends with, contains,
matches regex...) and then enter a value for that operation. This may
end up causing more work than not, though; I haven't really evaluated
it.

## No Cookie Support in FetchHTTP.

This was an oversight. I knew I was forgetting something. I had  
factored out the cookie-handling code from FetchHTTP, intending to  
create three separate implementations of a new CookieManager
interface:  
IgnoreCookieManager, BdbCookieManager, FileCookieManager. This change  
greatly simplified FetchHTTP's code, but I never actually created
those  
implementations. This would be a simple process of copying the now  
commented-out portions of FetchHTTP that used to deal with cookies
into  
new homes.

## The ProcessorResult is Never Being Evaluated by ToeThread.

Again, an oversight on my part. Processors can return certain signals
to  
the ToeThread, which should tell the ToeThread to (for instance) skip
ahead  
to the postprocessing. These signals are never evaluated by the
ToeThread,  
though, so each CrawlURI always passes through each processor. The  
processors were designed to not blow up in this case, but it's
inefficient.

## Review of Non-Default Modules

The only things that have been truly tested are modules that were
listed  
in the default configuration file for Heritrix. So, for instance,  
AdaptiveRevisitFrontier was never tested. Additionally, certain
features  
(eg, kickUpdate) are not covered by any unit test.

I'd like to at least do a formal review of each module. I'd create a
list  
of "difficult" things to check for (eg, special checkpointing
behavior)  
and ensure the module has been altered to function properly in the new  
system. Or, we can run a largeish crawl that is configured to use each  
untested module and attempt to active/deactive those modules over time
to  
see if they function as expected.

# Refactorings/Code Cleanup

## Elimination of CandidateURI

This was regarded as a good idea, and now's the time to do it. This
should  
go quickly; merge the CandidateURI code into CrawlURI, replace all  
references/constructions of CandidateURI with CrawlURI, ensure tests
still  
work.

## Elimination of CrawlStatusListener

Of necessity, CrawlController is now an MBean. It emits an MBean  
notification when the crawl status changes (eg, from RUNNING to PAUSED).

I simply layered this notification on top of the existing  
CrawlStatusListener architecture. It doesn't make a lot of sense to  
support to event notification systems for the same thing, though.

For that matter, CrawlURIDispositionListener should probably also
change  
to MBean notifications, for the sake of consistency (and to allow
remote  
applications to follow CrawlURI dispositions).

## KickUpdate/Reporter

Rather than having components iterate over their own children and
manually  
invoking kickUpdate(), I think it makes more sense for the settings
system  
to track modules that provide a kickUpdate() implementations. Such
modules  
would implement a KickUpdateable interface; the CrawlController would
expose  
a JMX operation "kickUpdate"; that operation would iterate over all
the  
known KickUpdateable interface, invoking kickUpdate().

Yet another way to handle this would be to avoid the notion of a  
kickUpdate altogether, and have the modules that require a kickUpdate
to  
expose their own method via JMX. That way an operator could kick just  
one module at a time. Not sure which approach is best.

## Interfaces for JMX Modules

CrawlController is now an open MBean. Standard practice for MBeans is
to  
create an interface X that defines the attributes/operations, then
implement  
that interface in a class named XImpl. It's an ugly convention but it
is  
standard. So, the existing CrawlController would become
CrawlControllerImpl,  
and it would implement a CrawlController interface. Modules that depend
on  
keeping a CrawlController reference handy would declare that reference
as  
the interface; that might help with unit testing.

## Delete Commented-Out and Dead Code.

Self-explanatory. Large parts of FetchHTTP and CrawlController were
moved  
to other places, but the old code was just commented out for
reference.  
Now that I'm a bit more confident that these things work, the old code  
should be removed for clarity's sake.

## Documentation

At minimum I'd like the public API of org.archive.state and  
org.archive.settings fully documented, as that would cover the core of  
the new settings system.

## Testing

Again, important things like AdaptiveRevisitFrontier need better test  
coverage in general, but should be at least manually tested before we  
think of release.

# Old Notes

Still left to do before code review:

1.  Make unit test stubs for all modules to ensure they actually conform
    to new settings system. (Done)
2.  Integrate XML format into FileSheetManager. (Done)
3.  Change CrawlJobHandler so that it uses FileSheetManagers instead of
    XMLSettingsHandlers (Done)
4.  Change Heritrix to use new CrawlJobHandler (Done)
5.  Make selftest work again. (99% done)
6.  Make maven dist work again.

Stuff to do during code review but before merge: 

1.   Restore deleted DecideRules, make unit test stubs for them too.

Stuff to do after merge:

1.  Bold new webapp -- either complete rewrite or minor tweaks, but
    either way it should be divorced from actual Heritrix instance (all
    webapp communication should occur over JMX).
2.  Split commons, processors and crawler into 3 separate subprojects to
    ensure that there's no cross-pollution (there are currently classes
    in archive-commons.jar that will will raise a LinkageError if loaded
    in apps other than Heritrix).
3.  Document the hell out of org.archive.state, org.archive.settings and
    org.archive.processors.
4.  Review modules to make sure their documentation is up-to-date.
5.  Turn unit test stubs into actual unit tests.
6.  Create src/test for testing code, create src/i18n for utf8 files.
7.  Clear warnings.

Other stuff that I'm just documenting so I don't forget:

-   Would be nice to have some sort of mechanism so that default values
    for Keys are allowed to violate the constraints for those Keys. In
    particular, it would be nice to have a non-null Constraint on most
    Keys, but still to specify null as the default value. Maybe some
    sort of @Required tag that the manager can use to enforce presence
    of things.
-   Some sort of object lifecycle tracking for objects within sheets --
    would be groovy if JMXSheetManager could automatically register and
    deregister modules that implement DynamicMBean. (Done)

Ugly, ugly bits:

-   Handling of Lists and Maps follows old settings system model, which
    makes it difficult to predict.
-   Formal dependencies place extra burden on crawl operators. (Dealt
    with)
-   Full resolution of settings is too expensive, especially for maps
    and lists. A more efficient implementation of Sheet.get is possible.
-   Weird polymorphism since resolution depends on key type, and not the
    actual value of the Key. (Eg, Key&lt;Object&gt; whose value is a Map
    won't have Map resolution rules applied.) Also Map and List
    implementations cannot also be configuration modules (a Map
    implementation cannot define static Key fields).
