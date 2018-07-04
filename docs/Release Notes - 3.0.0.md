# Release Notes - 3.0.0

# Release Notes - 3.0.0 (Dec 2009)

-   [Release Notes - 3.0.0
    (Dec 2009)](#ReleaseNotes-3.0.0-ReleaseNotes-3.0.0(Dec2009))
    -   [1. New and Notable](#ReleaseNotes-3.0.0-1.NewandNotable)
        -   [XML Configuration Based on the Spring
            Framework](#ReleaseNotes-3.0.0-XMLConfigurationBasedontheSpringFramework)
        -   [Unified RESTful Interface for Browser and Programmatic
            Control](#ReleaseNotes-3.0.0-UnifiedRESTfulInterfaceforBrowserandProgrammaticControl)
        -   [Apache 2 License](#ReleaseNotes-3.0.0-Apache2License)
        -   [Pauseless
            Checkpointing](#ReleaseNotes-3.0.0-PauselessCheckpointing)
        -   [Support for Millions of
            Seeds](#ReleaseNotes-3.0.0-SupportforMillionsofSeeds)
        -   [Enhanced Scripting
            Functionality](#ReleaseNotes-3.0.0-EnhancedScriptingFunctionality)
        -   [Action Directory](#ReleaseNotes-3.0.0-ActionDirectory)
        -   [Fixed-Interval URI
            Revisitation](#ReleaseNotes-3.0.0-Fixed-IntervalURIRevisitation)
    -   [2. Current
        Limitations](#ReleaseNotes-3.0.0-2.CurrentLimitations)
        -   [No Guided-Form
            Configuration](#ReleaseNotes-3.0.0-NoGuided-FormConfiguration)
        -   [File Proliferation and Automatic
            Renaming](#ReleaseNotes-3.0.0-FileProliferationandAutomaticRenaming)
        -   [Migration Tool
            Limited](#ReleaseNotes-3.0.0-MigrationToolLimited)
    -   [3. Moving from Heritrix
        1.14.x](#ReleaseNotes-3.0.0-3.MovingfromHeritrix1.14.x)
        -   [Operator Web Interface HTTPS By
            Default](#ReleaseNotes-3.0.0-OperatorWebInterfaceHTTPSByDefault)
        -   [Changed Configuration
            Steps](#ReleaseNotes-3.0.0-ChangedConfigurationSteps)
        -   [Build, Launch, Teardown
            In-Place](#ReleaseNotes-3.0.0-Build,Launch,TeardownIn-Place)
        -   [Seed-derived SURT Prefix and SURT Prefix Syntax
            Changes](#ReleaseNotes-3.0.0-Seed-derivedSURTPrefixandSURTPrefixSyntaxChanges)
    -   [4. All Tracked
        Changes](#ReleaseNotes-3.0.0-4.AllTrackedChanges)
    -   [Fixed in 3.0.0](#ReleaseNotes-3.0.0-Fixedin3.0.0)
    -   [Fixed in 3.0.0-RC1](#ReleaseNotes-3.0.0-Fixedin3.0.0-RC1)
    -   [Fixed in 3.0.0-beta](#ReleaseNotes-3.0.0-Fixedin3.0.0-beta)
    -   [Fixed in 3.0.0-alpha](#ReleaseNotes-3.0.0-Fixedin3.0.0-alpha)
    -   [5. Known Issues](#ReleaseNotes-3.0.0-5.KnownIssues)
        -   ["Create new job" gives
            NPE](#ReleaseNotes-3.0.0-%22Createnewjob%22givesNPE)

These are the project wiki release notes for the 3.0.0 release.

Release 3.0.0 is a major release, the first of the Heritrix3 ("H3")
series. It includes new features and issue fixes, and a significant
reworking of the configuration system and user interface based on
current and expected needs.

Heritrix3 is currently suitable for advanced users and projects that are
either customizing Heritrix (with Java or other scripting code) or
embedding Heritrix in a larger system. Please review the Current
Limitations, below, to help determine if Heritrix3 or a current
Heritrix1 (1.14.3 or later) release is best suited for your needs.

The 3.0.0 release is now available for download at [the archive-crawler
Sourceforge
project](https://sourceforge.net/projects/archive-crawler/files/heritrix3/3.0.0/).

Documentation for Heritrix3 is available via the [Heritrix 3.0 User
Guide](Heritrix%203.0%20and%203.1%20User%20Guide) , [Heritrix 3.0 API
Guide](Heritrix%203.x%20API%20Guide) , and other notes on the [Heritrix
project wiki](Heritrix) .

Please discuss questions, problems, and ideas at our [project discussion
list](http://archive-crawler.yahoogroups.com) , and submit bug reports
or feature requests via our [project JIRA issue
tracker](https://webarchive.jira.com/browse/HER) .

## 1. New and Notable

### XML Configuration Based on the Spring Framework

An XML file that conforms to the
[Spring](http://www.springframework.org) Inversion-of-Control container
framework ([version
2.5.6](http://static.springsource.org/spring/docs/2.5.x/reference/beans.html))
is now the mechanism for configuring Heritrix crawl jobs.  This file
exists for each crawl job and replaces the previous order.xml file.  The
file is called `crawler-beans.cxml` (or `profile-crawler-beans.cxml` to
signify a template configuration which may be edited and test-built but
not launched).

### Unified RESTful Interface for Browser and Programmatic Control

The Web User Interface has been redesigned to generally follow REST
architectural principles, allowing simple HTML GETs and POSTs to control
crawler behavior, either with a web browser or other systems.

### Apache 2 License

The Heritrix crawler source code, with the exception of a few files, is
now available under the Apache License, 2.0. See the included file
`LICENSE.txt` for details.

### Pauseless Checkpointing

Checkpoints may be requested without requiring a full-crawler pause, and
complete with a much smaller impact on the rate of progress. See
([HER-1516](https://webarchive.jira.com/browse/HER-1516)   ).

### Support for Millions of Seeds

Heritrix now robustly supports crawls with millions of seeds.  See
([HER-769](https://webarchive.jira.com/browse/HER-769)   ).

### Enhanced Scripting Functionality

Custom Processors and DecideRules may be implemented in Beanshell,
Javascript, or Groovy scripting languages without adding other libraries
or restarting Heritrix, and an enhanced Scripting Console in the
operator web user-interface allows any kind of inspection or
modification of a running crawl.

### Action Directory

The new Action directory allows adding seeds and recovery URI data at
any point during a crawl. See
([HER-1660](https://webarchive.jira.com/browse/HER-1660)   ).

### Fixed-Interval URI Revisitation

An experimental facility for directing the crawler to revisit URIs at a
fixed interval after their initial fetch is available. See
([HER-1714](https://webarchive.jira.com/browse/HER-1714)   ).

## 2. Current Limitations

### No Guided-Form Configuration

Configuring a Heritrix3 crawl requires directly editing a textual XML
configuration file. Simple changes are a matter of replacing or
un-commenting existing values in a model file, while more extensive
changes require understanding the Spring 'beans' container-specification
XML format, and specifying implementation Java classes by their full
names. An interface with individual fields and selection-lists of common
options, as in prior versions of Heritrix, will be restored in a future
release.

### File Proliferation and Automatic Renaming

The new model of relaunching a job in its home directory, rather than
creating a new directory for every launch, increases the likelihood logs
and other files from later runs will attempt to use the same filenames
as earlier runs. In general, Heritrix3 attempts to preserve the earlier
files by renaming them aside, with a timestamp suffix added to their
filenames.

### Migration Tool Limited

The current migration utility, executable class
`org.archive.crawler.migrate.MigrateH1to3Tool`, only works reliably for
changed basic `order.xml` configuration values as reflected in our
bundled default configuration. Also, it makes no effort to convert H1
per-domain/per-host settings overrides. By providing a model H3-based
configuration with some values brought over, and reporting the values it
cannot convert, it may still provide a useful base for other
hand-conversion. Please let us know what advanced configuration in your
Heritrix1 crawls is most important to support in the automated tool.

## 3. Moving from Heritrix 1.14.x

### Operator Web Interface HTTPS By Default

The operator user interface is now accessible only by HTTPS, by default,
on port 8443. A custom self-signed certificate will be generated (if a
server certificate is not specified) and saved for reuse if necessary.
As before, the interface is also only made available via the 'localhost'
interface unless a non-default switch is used to listen on all
interfaces.

Secure the operator interface

**Important:** Via its crawl-configuration and scripting capabilities,
the operator web interface grants the ability to run arbitrary Java
code, and make arbitrary filesystem changes, on the system running the
crawler, with all privileges of the user account used to launch the Java
runtime. As a result, securing the operator interface with network
policies and strong password is very important. Please review the
[Security
Considerations](https://webarchive.jira.com/wiki/display/Heritrix/Heritrix+3.0+User+Guide#Heritrix3.0UserGuide-SecurityConsiderations)
section of the User Manual for more details.

### Changed Configuration Steps

All pre-crawl configuration is guided by a primary XML configuration
file in the 'beans' format of the Spring framework. (It may import other
files or refer to other paths that are consulted, as well.) By
convention, this file is named '`crawler-beans.cxml`'.As noted above,
this file muse be edited directly -- either outside the web user
interface, or via a file-editor page provided in the web user interface
-- to change configuration parameters or the choice of implementing
classes for crawler functionality.

The bundled default profile contains an initial suggested configuration
with recommended values and modules, and should be used as a model to
build other configurations. It is extensively commented to describe
optional properties that may be altered from default values.

A migration program is also available to help operators migrate 1.x
crawl jobs to 3.0 crawl jobs. See
([HER-1641](https://webarchive.jira.com/browse/HER-1641)   ). It
currently only helps map simple configuration values to their new
equivalents, but will also display warnings about configuration that
requires more attention.

A built crawl may be inspected and changed in new ways, including the
Scripting Console and Bean Browser, but these changes will not be
automatically propagated to the CXML configuration.

### Build, Launch, Teardown In-Place

The general lifecycle of a crawl is now:

-   Compose the crawl job configuration as desired, perhaps starting
    from a bundled template or other earlier crawl job
-   **Build** the crawl, which serves to test many aspects of the
    configuration's validity (such as whether the CXML is legal and
    specified all necessary components and legal property values). A
    *built* crawl has had all its components created and connected, but
    has not yet started consuming disk resources or begun network
    activity.
-   **Launch** the crawl, which signals it to begin disk/network
    activity. Our bundled profile will begin in a paused state,
    requiring an un-pause for URI-fetching to actually begin, though
    this may be changed via a configuration property.
-   Monitor the running crawl, pausing/unpausing/checkpointing as
    desired. The job's detail page may always be reloaded in the browser
    for the latest running statistics.
-   Allow the crawl to reach its end or use the **Terminate** option.
    Even after termination, the crawl components remain alive in system
    memory for inspection/reporting.
-   **Teardown** the crawl to discard all crawl components, to free
    memory or allow the job to be freshly 'built' and 'launched' again.

A crawl job may be relaunched repeatedly in the same job directory. (A
new directory is *not* created for each launch.)

### Seed-derived SURT Prefix and SURT Prefix Syntax Changes

There have been some small but important changes in the syntax by which
SURT Prefixes are specified.

First, when deducing an 'implied' SURT prefix from a seed URI, the
presence or absence of a trailing '/' after the URI host portion (or
more precisely, URI authority portion) is no longer significant. The
trailing '/' is always assumed to be present – just as it is in browsers
and on HTTP requests, and the deduced SURT prefix is always limited to
that exact host (or authority). For example, in H3, either the seed
"http://example.com" or "http://example.com/" (note trailing '/') are
both treated as if they have the trailing slash. They both imply the
SURT prefix "http://(com,example,)/", which is only a prefix of URIs
that begin exactly "http://example.com/". If you want to accept all
subdomains of 'example.com', you must supply a suitable SURT prefix
yourself, for example "http://(com,example,".

Second, they syntax for supplying SURT prefixes is the same whether they
are included in your seeds-source text, or a separate surts-source file.
If you are going to provide a hand-crafted SURT prefix, it should be on
a line that begins with the '+' directive, for example
"+http://(com,example,", whether it is in your seeds file or a separate
surt-prefixes file specified via the surtsSourceFile setting.

If you want the SURT prefix to be deduced from a normal URI or even
naked hostname, these may be supplied in the seeds source text, with the
seedsAsSurtPrefixes setting on, or in the surtsSourceFile. For example,
consider the following short text file:

``` bash
images.example.com
http://sounds.example.com
+videos.example.com
+http://(com,exampleresources,
```

If the above is supplied as seeds source text, then the first two lines
will be interpreted as the seeds "http://images.example.com/" and
"http://sounds.example.com/". Further, the two lines beginning '+' will
be announced to any SURT-prefix-sensitive scoping rules – usually just a
single one – and result in that rule including the SURT-prefixes
"http://(com,example,videos,)/" (accepting any URLs on the
videos.example.com domain) and "http://com.exampleresources," (accepting
any URLs on exampleresources.com domain *and any subdomains*).

*If* the *seedsAsSurtPrefixes* setting is true on a particular
SURT-prefix-sensitive scope rule (which is the default), then those two
seeds will also result in that rule accepting URIs fitting the
SURT-prefixes "http://(com,example,images,)/" and
"http://(com,example,sounds,)/".

If that same text is supplied directly as SURTs-source-file, all lines
supply SURT prefixes. (The 'seedsAsSurtPrefixes' setting is irrelevant.)
Those lines beginning '' are considered to already be in SURT form;
those without '' are first coerced into URIs (adding "http://" if
necessary if a scheme isn't present) and then SURT prefixes are deduced.

## 4. All Tracked Changes

The following 111 tracked issues are recorded as addressed in this 3.0
release:

## Fixed in 3.0.0

<http://webarchive.jira.com/jira/secure/ReleaseNote.jspa?projectId=10021&styleName=Html&version=10160>

type

key

summary

status

Unable to locate JIRA server for this macro. It may be due to
Application Link configuration.

## Fixed in 3.0.0-RC1

<http://webarchive.jira.com/jira/secure/ReleaseNote.jspa?projectId=10021&styleName=Html&version=10034>

type

key

summary

status

Unable to locate JIRA server for this macro. It may be due to
Application Link configuration.

## Fixed in 3.0.0-beta

<http://webarchive.jira.com/jira/secure/ReleaseNote.jspa?projectId=10021&styleName=Html&version=10102>

type

key

summary

status

Unable to locate JIRA server for this macro. It may be due to
Application Link configuration.

## Fixed in 3.0.0-alpha

<http://webarchive.jira.com/jira/secure/ReleaseNote.jspa?projectId=10021&styleName=Html&version=10101>

type

key

summary

status

Unable to locate JIRA server for this macro. It may be due to
Application Link configuration.

  

  
  

## 5. Known Issues

### "Create new job" gives NPE

The 3.0.0 "Create new job from recommended starting configuration"
feature will produce a *NullPointerException*. A fix has been submitted
([HER-1725](https://webarchive.jira.com/browse/HER-1725)   ) and will be
included in the next incremental release. The recommended workaround is
to navigate to the default jobs directory starter profile, and use its
**copy** functionality, then revisit the "Engine" page, and press
**rescan**. Your new job should appear in the list of job directories.
