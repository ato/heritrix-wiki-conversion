# H3 Dev Notes for Crawl Operators

Latest changes, with notes on impact/use, for those operators following
official test releases and SVN trunk development builds.

-   [Checkpointing](#H3DevNotesforCrawlOperators-Checkpointing)
-   [Fixed Rescheduling](#H3DevNotesforCrawlOperators-FixedRescheduling)
-   [MigrateH1to3Tool](#H3DevNotesforCrawlOperators-MigrateH1to3Tool)
    -   [Usage](#H3DevNotesforCrawlOperators-Usage)
    -   [Example](#H3DevNotesforCrawlOperators-Example)
-   [Processors chain split in 3; LinksScoper/FrontierScheduler
    gone](#H3DevNotesforCrawlOperators-Processorschainsplitin3;LinksScoper/FrontierSchedulergone)
-   [Millions of seeds
    OK](#H3DevNotesforCrawlOperators-MillionsofseedsOK)
-   [Seeds list & SurtPrefixedDecideRule support '-'
    directives](#H3DevNotesforCrawlOperators-Seedslist&SurtPrefixedDecideRulesupport'-'directives)
-   [Seeds list SURT-hinting
    changed](#H3DevNotesforCrawlOperators-SeedslistSURT-hintingchanged)
-   [ActionDirectory for post-launch
    URI-loading](#H3DevNotesforCrawlOperators-ActionDirectoryforpost-launchURI-loading)
-   [Recovery log
    changes](#H3DevNotesforCrawlOperators-Recoverylogchanges)
-   ['sourceTagSeeds' setting moved from frontier to
    SeedModule](#H3DevNotesforCrawlOperators-'sourceTagSeeds'settingmovedfromfrontiertoSeedModule)
-   [CrawlController 'pauseAtStart' now default
    true](#H3DevNotesforCrawlOperators-CrawlController'pauseAtStart'nowdefaulttrue)
-   [QueueAssignmentPolicies: 'parallelQueues' and 'deferToPrevious'
    settings](#H3DevNotesforCrawlOperators-QueueAssignmentPolicies:'parallelQueues'and'deferToPrevious'settings)

### Checkpointing

The H1/H2 checkpointing functionality has been updated and improved to
work with H3. Most notably: a checkpoint may now be triggered without
requiring a full crawl pause.

The primary goal of the checkpointing functionality is to capture a
consistent image of a crawl's state at a particular moment, allowing a
future crawl restart to begin from exactly that point. That restart may
occur after a JVM relaunch, hardware repair or upgrade, migration of the
crawl state to a different machine, change of the crawl configuration,
or even (given some limitations on how much classes can change)
significant changes to the crawl software.

To enable checkpointing, your crawl configuration must contain a
"org.archive.crawler.framework.CheckpointService" bean (now included in
bundled profiles).This bean may be configured with an integer
'checkpointIntervalMinutes' setting to trigger automatic checkpoints at
that interval once the crawl is launched. (The default interval, -1,
means 'no automatic checkpoints'.)

To trigger a checkpoint manually, the web UI's job page includes a
'checkpoint' button which requests a checkpoint immediately, whether the
crawl is paused or not. (Programmatically, the CheckpointService's
requestCrawlCheckpoint() method may be executed.)

By default, each checkpoint creates at a minimum a new directory inside
the CheckpointService's configured 'checkpoints' directory. This
directory has a name of the form
"cp\[sequence-number\]-\[14-digit-timestamp\]", for example
"cp00003-20091120103609".

During a checkpoint, all beans that mark their interest in the
checkpoint process by implementing the interface Checkpointable are told
to save their relevant state. (Note that only 'top-level' beans, in
Spring parlance, can participate in checkpointing.) Beans with a small
amount of state may use utility methods (on the Checkpoint class) to
save their state to the main checkpoint directory. Beans with a larger
amount of state, such as those backed by large on-disk structures, may
store their state in other custom ways which avoid writing or copying
duplicate data. So far, this only happens with beans which use backing
BdbModule services, which all rely on the BdbModule's custom
checkpointing.

(The BdbModule stores its checkpointed state in checkpoint
subdirectories within its preexisting environment directory. Each
directory contains a manifest listing exactly the '.jdb' log files
needed to reconstruct the BDB state at the time of the checkpoint. The
normal BdbModule behavior never deletes obsolete '.jdb' files, only
renaming them to '.del'.)

Each checkpoint rotates all logs, renaming the current log to include
the 'cp\#\#\#\#\#' name as a suffix, starting a fresh log. Thus default
log-viewing in the UI will show empty logs immediately after a
checkpoint, and viewing older log lines requires requesting the older
log file by name. Each checkpoint also closes any ARCs/WARCs in
progress, resulting in smaller-than-target-sizedARCs/WARCs for thos in
progress at the checkpoint moment.

Checkpointing aims to reproduce the frontier (queues/already-seen)
status and running crawl statistics which feed reports perfectly, along
with any other state custom components may choose to save. Processors in
the 'FetchChain' may save slightly-inconsistent running stats \*unless\*
the crawl is paused, as progress is allowed to continue among the
fetch-chain processors during a pauseless checkpoint. (If perfectly
consistent checkpointing is required of these processors, pause the
crawl completely first.) Checkpointing specifically \*does not\* seek to
save state that (1) comes directly from the crawl configuration; (2) is
already captured in logs or ARCs/WARCs and is not consulted again in the
course of a continuing crawl; or (3) would expire if the checkpoint were
to be resumed at an arbitrarily later date. That is, the results of DNS
and robots fetches are not saved in the checkpoint, and resuming the
checkpoint even seconds later will result in automatic refreshing of
such fetched-as-needed data (just as if the crawl were started anew, or
the checkpoint were started long after all current data timed out).

Thus, to backup or migrate a job checkpoint fully, be sure to include
among the backed-up or moved files: (1) configuration files (such as the
cxml or any other files like seeds or SURT lists it refers to); (2) the
'cp\#\#\#\#\#-\#\#\#\#\#\#\#\#\#\#\#\#\#\#' directories (with full
contents) of checkpoints of interest, whether in the 'checkpoints'
directory or BdbModule environment directories; (3) all '.jdb' logs (or
their renamed '.del' versions) references by the checkpoints of
interest.

To trigger a checkpoint recovery, the designated Checkpoint must be part
of the crawl configuration either before the 'build' or 'launch' startup
stages. (Each Checkpointable component notices in its Lifecycle start()
method if this is a 'warm' recover-from-checkpoint or 'cold' fresh
start, and preloads its state as appropriate.) In the web UI, if a job
is built and the CheckpointService reports valid-looking Checkpoint
directories in its 'checkpoints' directory, a drop-down select box will
offer a choice of checkpoints by name. Selecting one before choosing
'launch' will cause that launch to begin with a
checkpoint-resumption.(Programmatically, the
CheckpointService.setRecoveryCheckpointByName method may be used to
activate one of these discovered checkpoints.)

Alternatively, an 'org.archive.checkpointing.Checkpoint' bean,
configured with the proper 'checkpointDir' property, may be declared in
the crawl configuration, and will be Spring auto-wired into a
Checkpointable components before the launch/start() to indicate a
recover-from-checkpoint.

### Fixed Rescheduling

A prototype capability for forcing URIs to be rescheduled at a fixed
interval after each fetch is available. The optional
ReschedulingProcessor may be added as a post-processor in the
DispositionChain, after the DispositionProcessor.

ReschedulingProcessor has one setting, 'rescheduleDelaySeconds'. When
this value is &lt;= 0, no rescheduling occurs (the traditional
behavior). For values greater than 0, a rescheduling time that many
seconds in the future will be calculated and written into the CrawlURI;
the frontier then remembers that URI and arranges for it to be
re-enqueued as soon as possible after that time, provided the crawl is
still running then. (How quickly the URI is then retried then depends on
the other URIs already queued at that time.)

The 'rescheduleDelaySeconds' setting may be overlaid with alternate
values based on SURTs or DecideRules using the Sheets mechanism,
allowing experimentation with different rescheduling rates for URIs on
different hosts or matching different patterns. (Further, the
ReschedulingProcessor could be replaced with arbitrarily complex custom
policies for calculating the rescheduling interval.)

### MigrateH1to3Tool

A utility to assist in creating a working H3 crawl configuration,
starting from a Heritrix 1.X configuration, is now available in the
class org.archive.crawler.migrate.MigrateH1to3Tool.

The class has a main() to be run standalone. It takes two arguments: a
path to an H1 order.xml, and a path to a desired directory where the H3
equivalent should be built.

Initially, it works on all simple-valued global settings of the bundled
default crawl profile that came with Heritrix 1.14.3 -- copying them to
a working H3 template configuration as properties-map syntax
'overrides'. For other customized global crawl settings, it will log a
report of what it could not apply to its H3 template, so that the intent
of that configuration can be manually ported.

The bundled 'bin/heritrix' (or 'bin\\heritrix.cmd' on Windows) launch
scripts may be used to launch other classes, like MigrateH1to3Tool, with
all necessary libraries on the classpath, by supplying the alternate
class name in an environment variable CLASS\_MAIN, and where appropriate
requesting foreground operation with a true FOREGROUND environment
variable. For example, from a bash shell inside the
'heritrix-3.0.0-SNAPSHOT' directory:

#### Usage

    MigrateH2to3Tool - takes a H1 order.xml and creates a similar H3 job directory
    Usage:
      $CLASS_MAIN $FOREGROUND bin/heritrix sourceOrderXmlFile destinationH3JobDir
    where
      CLASS_MAIN          = org.archive.crawler.migrate.MigrateH1to3Tool
      FOREGROUND          = true
      sourceOrderXmlFile  = H1 order.xml
      destinationH3JobDir = H3 job directory (to be created)

#### Example

    $ cd $HERITRIX_HOME
    $ CLASS_MAIN=org.archive.crawler.migrate.MigrateH1to3Tool\
      FOREGROUND=true bin/heritrix\
      ../heritrix-1.14.3/jobs/myoldjob-20090214002857765/order.xml\
      jobs/myH3job

Future revisions will add support for hostname-based settings overrides
and greater variety of customization in choice of Scope, Processor, and
policy implementation classes in the source H1 configuration.

### Processors chain split in 3; LinksScoper/FrontierScheduler gone

See \[HER-1605   \] and [Frontier Unbundling Design
Details](Frontier%20Unbundling%20Design%20Details) for details; the
motivations are threefold:

-   treat 'candidates' that are being analyzed/scoped before scheduling
    the same chain-of-processors flexibility
-   divide the old processing-chain into a first part, whose
    work-in-progress can always be interrupted or ignored for
    checkpointing purposes, and a second part, which always completes
    atomically (scheduling outlinks and recording the final status of a
    tried URI) with regard to checkpointing -- to allow better
    on-the-fly checkpointing
-   provide places for lots of policy-driven decisionmaking/calculations
    to occur outside of the overgrown and overly-contended frontier,
    increasing throughput

What was once done by LinksScoper+FrontierScheduler now happens inside a
new CandidatesProcessor processor, which sends each candidate outlink
through a configurable CandidateChain of other processors. That
CandidateChain currently includes a CandidateScoper processor, which
scope-checks a single outlink, and a FrontierPreparer, which readies
those URIs that pass scope-checking for frontier-scheduling. (The actual
scheduling or promotion-to-seed happen in CandidatesProcessor.)

See the bundled default
[profile-crawler-beans.cxml](https://archive-crawler.svn.sourceforge.net/svnroot/archive-crawler/trunk/heritrix3/dist/src/main/conf/jobs/profile-defaults/profile-crawler-beans.cxml)
in SVN for details of the new recommended configuration of the three
processor chains.

### Millions of seeds OK

The last few places -- mostly in report-generation -- where a crawl with
(tens or hundreds of) millions of seeds might try to use an unbounded
amount of RAM have been eliminated. There should not be a problem
starting a crawl with millions of seeds, or feeding millions of extra
URIs to a crawl that's started (such as with the ActionDirectory
capability described below).

### Seeds list & SurtPrefixedDecideRule support '-' directives

The bean which loads the crawl with seeds now announces non-seed lines
(like those beginning '' or '') to any bean it knows is a SeedListener.
(Configuration autowiring means any named bean that implements
SeedListener will receive such announcements.) A SurtPrefixedDecideRule
whose decision is ACCEPT will consider all '' lines as potential
add-SURT-prefix directives; a SurtPrefixedDecideRule whose decision is
REJECT will consider all '' lines as potential add-SURT-prefix
directives.

The bundled default profile includes a second, later
SurtPrefixedDecideRule, initially empty of all prefixes, which can thus
be filled by this mechanism (or other configuration options) to
Scope-REJECT URIs.

See the bundled default
[profile-crawler-beans.cxml](https://archive-crawler.svn.sourceforge.net/svnroot/archive-crawler/trunk/heritrix3/dist/src/main/conf/jobs/profile-defaults/profile-crawler-beans.cxml)
in SVN for details of the new recommended starting scope-rules.

### Seeds list SURT-hinting changed

In earlier versions of Heritrix, whether or not a seed with no path
ended with a '/' (such as "http://example.com/" or "http://example.com")
made a difference in what SURT-prefix was implied by the seed.
Specifically, the presence of the '/' meant 'exactly this hostname'
(SURT-prefix "http://(com,example,)/") while the absence meant "this
domain and any subdomains" (SURT-prefix "http://(com,example,").

This was strictly a Heritrix-invented subtlety; in both cases, the URIs
are strictly identical at the level of the HTTP protocol or URI
interpretation rules.

A change in the way seeds are read and scheduled for fetching means the
lack of a '/' is normalized before the scoping rules can use its
presence or absence as an interpretation hint. Thus, in H3, the seed
"http://example.com" is equivalent in its SURT-implication to
"http://example.com/". The older more-permissive SURT-prefix can still
be added by means of an explicit "+" directive in the seeds list text.

### ActionDirectory for post-launch URI-loading

A bean class ActionDirectory, if present in a crawl configuration (and
it is recommended to become part of all standard configurations),
watches a configured 'action' directory for any files which appear
(rechecking a configurable interval, default 30 seconds). For each file,
an action is taken in accordance with the file's suffix, then the file
is moved to a 'done' directory.

A file ending '.seeds' will trigger the addition of more seeds. A file
ending '.recover' will be treated as a traditional recovery log -- with
all 'Fs' lines considered included (to suppress recrawling) then all
'F+' lines rescheduled. A file ending '.include', '.schedule', or
'.force' respectively will be treated as if a recovery-log format (with
3-character prefix tag per line), but all URIs listed (regardless of
prefix-tag) will be considered-included, scheduled, or force-scheduled
respectively.

Any of these files may be gzip-compressed (with a '.gz' extension), and
those in recovery-log-format may have a '.s.' inserted prior to the
functional suffix (eg 'frontier.s.recover.gz') to indicate that prior to
other steps, scoping should be attempted against the included URIs.

Dropping the proper files (possibly filtered) into this directory will
likely be the recommended way to recover prior crawl frontier state, or
perform other bulk adds to a running crawler.

### Recovery log changes

The recovery log, formerly named 'recover.gz', is now named
'frontier.recover.gz', both to emphasize that it only logs frontier
information, and to make '.recover' a proper dotted-suffix for other
tools to recognize files in this format.

### 'sourceTagSeeds' setting moved from frontier to SeedModule

As the SeedModule now has responsibility for creating seed CrawlURIs,
and announcing their existence to all consumers (SeedListeners), this
setting for pre-configuring seeds with a tag of their hostname which is
inherited by discovery-descendant URIs is now on SeedModule.

### CrawlController 'pauseAtStart' now default true

The default if otherwise unspecified is now for jobs to start paused --
giving a chance to examine state, load URIs, etc.

Operators may manually 'unpause' via the web interface, or add the
override 'crawlController.pauseAtStart=true' to their configuration.

### QueueAssignmentPolicies: 'parallelQueues' and 'deferToPrevious' settings

SurtAuthorityQueueAssignmentPolicy and HostnameQueueAssignmentPolicy now
derive from a new shared superclass,
URIAuthorityBasedQueueAssignmentPolicy. Two new settings are available
from this superclass:

parallelQueues: default value (and historical behavior) is '1'. If
instead N, all URIs that previously went into the same single-named
queue will go into N related queues (via a consistent hash-mapping of
the path?query portion of the URL). Each queue is considered separately
for traditional politeness based on one-at-a-time connections and
snooze-delays-between-fetches -- so N queues means N fetches could be in
progress against a site at once. Thus, should only be used in an overlay
setting, applied to sites likely to handle multiple connections well.

deferToPrevious: default value is 'true'. historical behavior was
'false'. If true, once a URI is assigned to a queue, it is not rechecked
for assignment to another queue when it is dequeued -- the previous
assignment sticks. For example, if changing 'parallelQueues' to a larger
N mid-crawl, this 'deferToPrevious' means old URIs won't be resplit
among N queues, only new URIs will be so distributed.
