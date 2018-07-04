# Heritrix3

Heritrix3 (or 'H3' for short) refers to releases 3.0 and up of Heritrix.

The official [Heritrix 3.0.0 Release](Release%20Notes%20-%203.0.0) is
now available (December 2009).

Future releases planned on the H3 line are a 3.0.1 patch release with
minor fixes and enhancements in the first half of 2010, and a 3.2.0
release with new functionality on the themes of ease-of-use, continuous
crawling, and large-scale crawling.

Available Heritrix3 documentation includes:

-   [Heritrix 3.0 and 3.1 User
    Guide](Heritrix%203.0%20and%203.1%20User%20Guide) 
-   [Heritrix 3.x API Guide](Heritrix%203.x%20API%20Guide)

The 3.X releases have a new Spring-container-based configuration system
and web-service-only browser and remote-control interface.

3.X also moves to a model where a single job, in a single job directory,
may be be relaunched in place many times (instead of creating a new job
directory before each launch).

-   [Running Heritrix3](#Heritrix3-RunningHeritrix3)
    -   [Current Limitations](#Heritrix3-CurrentLimitations)
    -   [Prerequisites](#Heritrix3-Prerequisites)
    -   [Download and Installation](#Heritrix3-DownloadandInstallation)
    -   [Launching and Contacting
        Heritrix](#Heritrix3-LaunchingandContactingHeritrix)
    -   [Engine Summary Page](#Heritrix3-EngineSummaryPage)
    -   [Profile Summary Page](#Heritrix3-ProfileSummaryPage)
    -   [Job Summary Page](#Heritrix3-JobSummaryPage)
    -   [Spring-based Crawl Job
        Configuration](#Heritrix3-Spring-basedCrawlJobConfiguration)
    -   [Job Control and Monitoring](#Heritrix3-JobControlandMonitoring)
    -   [Latest Updates](#Heritrix3-LatestUpdates)

## Running Heritrix3

### Current Limitations

Current versions of H3 through 3.0.0 have the following limitations:

-   All pre-launch configuration editing is via the files on disk or web
    UI's textarea raw file editor.
-   Settings changes or reconfiguration made during a built/running
    crawl is performed directly on the active crawl's object state, and
    will not automatically be reflected in the configuration for future
    launches.
-   When a job is relaunched, previous logs are renamed aside, with new
    names based on the time-of-new-launch.
-   When job reports are generated (on view request or at end-of-crawl),
    they overwrite previous reports. (Copy any reports elsewhere you
    want to save.)

We are considering other new ways to document and assist both pre-crawl
and during-crawl configuration, but something analogous to the long-form
guided field-editing of H1/H2 will not come until some time after the
3.0.1 release.

### Prerequisites

Heritrix3 requires a Java 6 (JDK1.6) runtime. Java 6 was officially
released in December 2006, and offers better performance, relevant
fixes, and useful new libraries. We recommend Sun's Java wherever it is
available.

Our official target platform is Linux and Heritrix gets the most testing
there. However, many users (including some of the core team) report
success on Windows and MacOS, and we welcome reports/fixes of any
glitches encountered there.

(To build Heritrix3 from source requires a recent Maven2, which will
automatically fetch all required 3rd-party libraries.)

### Download and Installation

As of 2009-12, the official 3.0.0 release is available from Sourceforge:

The 3.0.0 release is now available for download at [Heritrix 3.0.0 at
Sourceforge](https://sourceforge.net/projects/archive-crawler/files/heritrix3/3.0.0/).

The 'heritrix-3.1.1-SNAPSHOT-dist.tar.gz' or
'heritrix-3.1.1-SNAPSHOT-dist.zip' packages with the latest dates (will
be of most interest.

All development builds which pass auto-testing (which will include
issues fixed post-release, but may also include new problems) collect in
this area of our Maven2 repository (latest at the bottom):

<http://builds.archive.org:8080/maven2/org/archive/heritrix/heritrix/3.1.1-SNAPSHOT/>

One of the distribution packages named like
*heritrix-3.1.1-XXXXXXX.XXXXXX-XX-dist.tar.gz* are most commonly of
interest. Also, the very latest development auto-build (even if it fails
tests) may always be downloaded from the working directory dist/target/
on our [Continuum build
box](http://builds.archive.org:8081/continuum/servlet/continuum/target/WorkingCopy.vm/view/WorkingCopy/id/76?userDirectory=dist/target). 

As with previous releases, expand in a convenient place and ensure the
bin/heritrix script has proper execute permissions.

### Launching and Contacting Heritrix

Similar to previous releases:

``` bash
% bin/heritrix -a OPERATOR_PASSWORD_OF_YOUR_CHOOSING
```

Unlike with previous releases, the web control interface is only made
available via secure-socket HTTPS, and corresponding to this change
**the default port has changed to 8443**. Additionally, unless you
supply a compatible keystore via the new optional '-s' command-line
switch, an 'ad-hoc' keystore with a new locally-generated SSL-capable
certificate will be created (and then reused on future launches).

To then contact the web interface from a browser running on the same
machine, visit the URL:

    https://localhost:8443/

(If you need to contact the web interface from another machine, your
launch of Heritrix needs to tell it to listen on other of the machine's
IP addresses. You can use the command-line option '-b
IP\_ADDRESS\[,IP\_ADDRESS\]' or '-b /' to listen on all addresses.)

Unless you've done some very uncommon configuration of both Heritrix and
your browser, your browser will not initially recognize the Heritrix
HTTPS session as coming from a trusted source -- and so your first
connection will trigger a warning.  In most browsers, you can however
accept the ad-hoc Heritrix certificate as a permanent exception. (You
should manually verify that the certificate ingerprint shown in the
browser matches that echoed where Heritrix was launched.) From that
point on you will only receive a fresh browser warning if a new
certificate is encountered (as if discarding or installing over the
certificate originally generated).

FireFox3 self-signed certificate error (workaround)

If Firefox does not offer the option of adding an exception directly in
the browser content window, an exception can also be entered via
preferences:

    FireFox > Preferences > Advanced > Encryption > View Certificates >
    Servers > Add Exception [ localhost:8443 ] Get Certificate >
    Confirm Security Exception > OK

### Engine Summary Page

The `/engine/` path in the web interface shows the software version,
memory usage, and a list of all job/profile directories found in the
engine's active 'jobs' directory.

(By default, this is the 'jobs' sub-directory of the Heritrix
installation, but another directory may be specified instead with the
'-j' command-line option. Any subdirectory of the jobs directory
including a '.cxml' crawler-xml file is considered a job/profile
directory.)

A profile is a special kind of job that may be edited and tested for
configuration errors, but not launched -- it is meant to serve as a
reusable template for other jobs. Any job whose '.cxml'
primary-configuration file begins 'profile-' is considered a profile and
locked against launching.

In a fresh installation, launched as above, the only job shown will be
'profile-defaults'.

### Profile Summary Page

Visiting the 'profile-defaults' page will show the Job Summary page for
this profile:

<http://localhost:8443/engine/job/profile-defaults>

The two files which make up this job configuration,
`profile-crawler-beans.cxml` (the primary configuration) and
`defaults.xml` (which is included by an 'import' statement from the
primary) may be viewed and edited. The 'build' button may be used to
assemble the crawl (instantiate a Spring `ApplicationContext`,
triggering all configuration-wiring) as a way to test the configuration
for problems.

Any problems will be reported in a new log, the 'job log', which exists
per job/profile. The latest 5 lines of this log (with most recent first)
will be excerpted in the summary page. (The 'more' link will show the
entire log.)

Two kinds of configuration problems can be discovered by building a
job/profile.

1.  First, there could be configuration inconsistencies which prevent
    Spring instantiation from completing. (For example, required
    settings might be missing, or autowired properties might need
    instances that are not declared.) These will appear as exceptions
    reported in the job log.
2.  Second, even after Spring instantiation completes, a 'validation'
    step will be triggered where components can object if any configured
    values fail to match expected ranges/patterns/etc. These are
    reported as validation problems in the job log.

As with previous Heritrix versions, **the bundled default profile has an
intentional flaw that must be corrected before it will build and
validate**: *you must supply your own crawl-operator contact URL* that
is added to the crawler's 'User-Agent', so that any sites visited by
your crawls know who to contact in the event of problems. (See below for
more about customizing the default profile as a launchable job.)

Even when a *profile* builds/validates successfully, it may not be
launched, to prevent filling the profile/template with the droppings of
a specific crawl run. Instead, a profile should be copied to a separate
job directory before launching. The very bottom of the summary page
includes a 'Copy' option, taking the new job name, to copy the current
profile to a new job. (Jobs may also be copied, and checking the
'profile' box will cause the new copy to be named as a new profile,
whether starting from a job or profile.)

### Job Summary Page

For a non-profile job, the Job Summary page also offers options to
launch, control, and monitor a running job. If using the above 'copy'
functionality to copy the profile-default to a new job called 'testjob',
then the 'testjob' summary page will be at:

    http://localhost:8443/engine/job/testjob

### Spring-based Crawl Job Configuration

See also: [Spring Crawl Configuration](Spring%20Crawl%20Configuration)

Currently, configuring a job involves editing the Spring 'beans'
configuration file(s) which describe how to assemble a crawler from all
available components for a specific job.

These files may be edited directly in the web interface, by making use
of the 'edit' links alongside the discovered primary 'cxml' file name
(and any other imported files).

The default profile has collected all usual, required components into
the 'defaults.xml' file, which is imported at the beginning the primary
'crawler-beans.cxml' file. If building a configuration based on the
defaults, it should never be necessary to edit 'defaults.cxml' -- even
if you want to completely replace one of its definitions, simply placing
a definition with the same 'id' in the 'crawler-beans.cxml' will
supercede the imported definition.

The only two changes absolutely necessary to launch a job based on the
default profile are (1) adding an operator-contact-URL, so that the
built job will validate; and (2) adding a suitable set of seed URLs.
Areas for setting these values are highlighted in the default
'crawler-beans.cxml'.

### Job Control and Monitoring

If a job builds and validates, the 'launch' button on its summary page
will be available. Once launched, the 'pause', 'unpause', and
'terminate' buttons are available for a running job. (The 'discard'
button discards an assembled job, allowing a re-build/re-launch,
possibly after changing the configuration.)

In previous Heritrix versions, it was expected each job directory would
be run once, then not reused. (To launch a similar job, a new job
directory would be created.) Heritrix3 instead expects that a job will
be repeatedly relaunched in the same directory -- possibly automatically
reusing information from previous launches to minimize fetches or
storage of duplicate material, or to optimize the rate at which URIs ar
revisited. The history of launches is evident in the persistent job log.

Once a job is built, the job summary page displays status information
equivalent to the 'console' of previous versions. Links also offer
direct-viewing of all configuration-paths, and report links both
generate a report to a local file, and then display it. (Note that each
time a report is regenerated, including at the end of a crawl, it will
replace the previous version on disk.)

The last 10 lines of the crawl.log -- latest on top -- are shown, and a
link offers a paged browsing through the entire log. 

Editting the configuration file cannot affect a running crawl -- only
the next crawl built from that configuration.

Two advanced options for interacting with a built/launched crawl are the
'scripting console' and 'browse beans' options. The scripting console
allows any script in a supported language (Beanshell, JS, Groovy) to be
executed with access to the assembled crawl. The bean browser offers
views of the crawl's assembled components ('beans') by their
configuration bean names or 'bean paths'.

### Latest Updates

The latest functional additions and changes of interest to test-version
users are described at [H3 Dev Notes for Crawl
Operators.](H3%20Dev%20Notes%20for%20Crawl%20Operators)
