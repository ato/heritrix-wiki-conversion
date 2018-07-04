# How-To Feed URLs in bulk to a crawler

If you need to feed a large number of URLs to a crawl, at either the
start or any other time before the crawl terminates, there are several
options.

In practice, the first option, provide as seeds, has worked acceptably
up to hundreds of thousands of URLs, if treating those URLs as seeds is
acceptable. The second option, import via web UI or JMX, has worked well
for mixed-size batches of URLs anytime during a crawl, and allows the
hops-path and via values of non-seed URLs to be set. The third option,
importing a recovery log at crawl start, has worked well even into many
tens of millions of URLs, and unlike the other options allows crawling
to begin concurrent with the bulk URLs still being imported (shorter
pause).

Details on each option below.

## Provide them as seeds

Of course, URLs may be entered (or provided in a seeds file) at the
crawl's start. Such URLs may be treated specially by some scope options
– automatically considered in-scope, or used to determine other classes
of related URLs that should also be ruled in-scope.

The seed list may be editted via the web settings UI during a crawl,
though it is recommended that the crawl be paused before such editting.
After completing the edit and resuming the crawl, the seeds list will be
rescanned (unless a scope setting has been changed to disable this
rescan). All the URLs will be preented for frontier scheduling – but any
URL previously scheduled (as an prior seed or discovered during the
crawl) will be ignored as already-included. That is, only new,
undiscovered URLs added to the seed list will be scheduled.

Generally, the web UI's entry area is not usable past a few thousand
entries, and when the seed list exceeds a certain size, the web text
entry area will be disabled. Larger seed lists – into the hundreds of
thousands or millions – can be provided by a seeds file (usually named
seeds.txt). Edits directly to this file will not be detected by a mere
crawler pause/resume – but editting any other setting will cause a
rescan (again unless the option to disable this rescan has been chosen
on the scope). Each time a very large seed list is scanned, there may be
a noticeable long pause, and crawling only begins after all seeds are
imported.

## Use the web UI or JMX import options

When a crawl is paused, the 'View or Edit Frontier URIs' option will
appear in the console's job information area. From the resulting page, a
file containing URIs can be imported. The file can have one URI per
line, or be in the same format as a crawl.log or (uncompressed) recovery
journal (in which cases the hops-path and via-URL will also be
retained). The 'force fetch' checkbox will force the URIs in the file to
be scheduled even if they were previously scheduled/fetched.

Similar options exist through the JMX interface in Heritrix 1. In
Heritrix 3, the [action
directory](https://webarchive.jira.com/wiki/display/Heritrix/Action+Directory)
is a good means.

## Start the crawl with a recovery log

Specifying a recovery log at crawl start, per the [user
manual](http://crawler.archive.org/articles/user_manual/outside.html#recover),
will cause a two-step process to occur with the log that can be used to
add large numbers of URIs to the crawl.

In the first step, all URLs on recovery-log lines beginning 'Fs' are
marked as having been already-scheduled – but not scheduled. This has
the effect of preventing those URIs from being scheduled later by the
crawl. In the second step, all URLs on recovery-log lines beginning 'F+'
are presented for scheduling. Only those not already marked as scheduled
will be scheduled.

Thus by editting or composing a recovery-log format file, the crawl can
be preconfigured to include large numbers of URLs, or consider them
already done and thus unschedulable.

This process works acceptably for tens of millions of URLs, and regular
crawling begins before all lines are processed for the second step.
