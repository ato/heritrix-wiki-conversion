# Release Notes - Heritrix 3.2.0

# Release Notes - 3.2.0 (Jan 2014)

-   [Release Notes - 3.2.0
    (Jan 2014)](#ReleaseNotes-Heritrix3.2.0-ReleaseNotes-3.2.0(Jan2014))
    -   [1. Version Numbering
        Convention](#ReleaseNotes-Heritrix3.2.0-1.VersionNumberingConvention)
    -   [2. New and
        Notable](#ReleaseNotes-Heritrix3.2.0-2.NewandNotable)
        -   [Through Heritrix 3.2.0
            (January 2014)](#ReleaseNotes-Heritrix3.2.0-ThroughHeritrix3.2.0(January2014))
            -   [URL-agnostic deduplication
                (HER-2022)](#ReleaseNotes-Heritrix3.2.0-URL-agnosticdeduplication(HER-2022))
            -   [Automatic form login
                (HER-2031)](#ReleaseNotes-Heritrix3.2.0-Automaticformlogin(HER-2031))
            -   [Option to forget all but latest checkpoint
                (HER-2051)](#ReleaseNotes-Heritrix3.2.0-Optiontoforgetallbutlatestcheckpoint(HER-2051))
            -   [Handle stats consistently on checkpoint
                (HER-2048)](#ReleaseNotes-Heritrix3.2.0-Handlestatsconsistentlyoncheckpoint(HER-2048))
            -   [Custom extractor that constructs outlinks from strings
                found in
                content (HER-2024)](#ReleaseNotes-Heritrix3.2.0-Customextractorthatconstructsoutlinksfromstringsfoundincontent(HER-2024))
            -   [Responsive web UI using freemarker templates
                (HER-1726)](#ReleaseNotes-Heritrix3.2.0-ResponsivewebUIusingfreemarkertemplates(HER-1726))
            -   [Improved speculative link extraction from javascript
                (HER-1523)](#ReleaseNotes-Heritrix3.2.0-Improvedspeculativelinkextractionfromjavascript(HER-1523))
        -   [Through Heritrix 3.1.1
            (May 2012)](#ReleaseNotes-Heritrix3.2.0-ThroughHeritrix3.1.1(May2012))
            -   [Nicer code editor for crawl config and script console
                (HER-2001)](#ReleaseNotes-Heritrix3.2.0-Nicercodeeditorforcrawlconfigandscriptconsole(HER-2001))
            -   [Fixed occasional mangling of DNS records in ARCs and
                WARCs
                (HER-1983)](#ReleaseNotes-Heritrix3.2.0-FixedoccasionalmanglingofDNSrecordsinARCsandWARCs(HER-1983))
            -   [Remember all surts across checkpoint/resume
                (HER-1985)](#ReleaseNotes-Heritrix3.2.0-Rememberallsurtsacrosscheckpoint/resume(HER-1985))
            -   [Support for saving script state
                (HER-1984)](#ReleaseNotes-Heritrix3.2.0-Supportforsavingscriptstate(HER-1984))
        -   [Through Heritrix 3.1.0 final
            (October 2011)](#ReleaseNotes-Heritrix3.2.0-ThroughHeritrix3.1.0final(October2011))
            -   [More conservative speculative javascript extraction
                (HER-1951)](#ReleaseNotes-Heritrix3.2.0-Moreconservativespeculativejavascriptextraction(HER-1951))
            -   [A few XML API tag names have changed to follow
                camelcase convention
                (HER-1953)](#ReleaseNotes-Heritrix3.2.0-AfewXMLAPItagnameshavechangedtofollowcamelcaseconvention(HER-1953))
            -   [HTTP authentication type fallback
                (HER-1917)](#ReleaseNotes-Heritrix3.2.0-HTTPauthenticationtypefallback(HER-1917))
            -   [Cookie saving and loading
                (HER-1914)](#ReleaseNotes-Heritrix3.2.0-Cookiesavingandloading(HER-1914))
        -   [Through Heritrix 3.1.0-RC1
            (July 2011)](#ReleaseNotes-Heritrix3.2.0-ThroughHeritrix3.1.0-RC1(July2011))
            -   [Distinct directories for each re-launch of a job
                (HER-1901,
                HER-1900)](#ReleaseNotes-Heritrix3.2.0-Distinctdirectoriesforeachre-launchofajob(HER-1901,HER-1900))
            -   [Use of Spring 3.0
                (HER-1908)](#ReleaseNotes-Heritrix3.2.0-UseofSpring3.0(HER-1908))
            -   [CrawlController pauseAtEnd option replaced with
                runWhileEmpty
                (HER-1776)](#ReleaseNotes-Heritrix3.2.0-CrawlControllerpauseAtEndoptionreplacedwithrunWhileEmpty(HER-1776))
            -   [Optional logExtraInfo in crawl.log, such as name of
                ARC/WARC file (HER-834,
                HER-1790)](#ReleaseNotes-Heritrix3.2.0-OptionallogExtraInfoincrawl.log,suchasnameofARC/WARCfile(HER-834,HER-1790))
            -   [Discover charset as declared in content
                (HER-741)](#ReleaseNotes-Heritrix3.2.0-Discovercharsetasdeclaredincontent(HER-741))
            -   [Support for HTTP proxy authentication
                (HER-915)](#ReleaseNotes-Heritrix3.2.0-SupportforHTTPproxyauthentication(HER-915))
            -   [Allow fetching to begin before full load of large seed
                list
                (HER-1905)](#ReleaseNotes-Heritrix3.2.0-Allowfetchingtobeginbeforefullloadoflargeseedlist(HER-1905))
            -   [Spring-configurable reports
                (HER-1812)](#ReleaseNotes-Heritrix3.2.0-Spring-configurablereports(HER-1812))
            -   [Persisting of history optionally dependent on fetch
                having been archived
                (HER-1791)](#ReleaseNotes-Heritrix3.2.0-Persistingofhistoryoptionallydependentonfetchhavingbeenarchived(HER-1791))
        -   [Through Heritrix 3.1.0-beta
            (April 2011)](#ReleaseNotes-Heritrix3.2.0-ThroughHeritrix3.1.0-beta(April2011))
            -   [Optional Support for 'chunked' Transfer-Encoding,
                HTTP/1.1-identified requests, and 'gzip,deflate'
                Content-Encoding (HER-1876, HER-726,
                HER-1053)](#ReleaseNotes-Heritrix3.2.0-OptionalSupportfor'chunked'Transfer-Encoding,HTTP/1.1-identifiedrequests,and'gzip,deflate'Content-Encoding(HER-1876,HER-726,HER-1053))
            -   [Easier robots-policy configuration and new capabilities
                (HER-1803, HER-1861, HER-1620,
                HER-1880)](#ReleaseNotes-Heritrix3.2.0-Easierrobots-policyconfigurationandnewcapabilities(HER-1803,HER-1861,HER-1620,HER-1880))
            -   [Liveness of frontier and settings-overlay information
                improved (HER-1768, HER-747,
                HER-1823)](#ReleaseNotes-Heritrix3.2.0-Livenessoffrontierandsettings-overlayinformationimproved(HER-1768,HER-747,HER-1823))
            -   [Infer '/favicon.ico' and optionally root page ('/')
                (HER-1799,
                HER-1010)](#ReleaseNotes-Heritrix3.2.0-Infer'/favicon.ico'andoptionallyrootpage('/')(HER-1799,HER-1010))
            -   [New global ExtractorParameters settings 'extract404s'
                and 'extractIndependently' (HER-1848,
                HER-1836)](#ReleaseNotes-Heritrix3.2.0-NewglobalExtractorParameterssettings'extract404s'and'extractIndependently'(HER-1848,HER-1836))
            -   [Improved string-might-be-URI testing
                (HER-1763)](#ReleaseNotes-Heritrix3.2.0-Improvedstring-might-be-URItesting(HER-1763))
            -   [DiskSpaceMonitor component for detecting, pausing in
                low-disk-space conditions
                (HER-1811)](#ReleaseNotes-Heritrix3.2.0-DiskSpaceMonitorcomponentfordetecting,pausinginlow-disk-spaceconditions(HER-1811))
            -   [New formula and default conventions for ARC/WARC naming
                to better guarantee uniqueness
                (HER-1727)](#ReleaseNotes-Heritrix3.2.0-NewformulaanddefaultconventionsforARC/WARCnamingtobetterguaranteeuniqueness(HER-1727))
            -   [Fetcher for 'whois' information
                (HER-1645)](#ReleaseNotes-Heritrix3.2.0-Fetcherfor'whois'information(HER-1645))
            -   [Frontier queue-reporting more configurable
                (HER-1827)](#ReleaseNotes-Heritrix3.2.0-Frontierqueue-reportingmoreconfigurable(HER-1827))
            -   [Checkpointing based on hard-links for space savings,
                flexibility
                (HER-1821)](#ReleaseNotes-Heritrix3.2.0-Checkpointingbasedonhard-linksforspacesavings,flexibility(HER-1821))
            -   [SurtPrefixedDecideRule 'surtsSource' may use file path
                or inline String
                (HER-1857)](#ReleaseNotes-Heritrix3.2.0-SurtPrefixedDecideRule'surtsSource'mayusefilepathorinlineString(HER-1857))
            -   [Workaround for Java 6 update 23 GZIP incompatibilities
                (HER-1865)](#ReleaseNotes-Heritrix3.2.0-WorkaroundforJava6update23GZIPincompatibilities(HER-1865))
            -   [Proper rejection of cookies on top-level-domains/public
                suffixes
                (HER-1864)](#ReleaseNotes-Heritrix3.2.0-Properrejectionofcookiesontop-level-domains/publicsuffixes(HER-1864))
            -   [Crawl.log 'hops path' now shows only last 50 hop-types
                (HER-1834)](#ReleaseNotes-Heritrix3.2.0-Crawl.log'hopspath'nowshowsonlylast50hop-types(HER-1834))
            -   [Protecting operator login credentials from casual
                snooping (HER-1753,
                HER-1804)](#ReleaseNotes-Heritrix3.2.0-Protectingoperatorlogincredentialsfromcasualsnooping(HER-1753,HER-1804))
    -   [3. All Tracked
        Changes](#ReleaseNotes-Heritrix3.2.0-3.AllTrackedChanges)
        -   [Fixed in 3.2.0
            final](#ReleaseNotes-Heritrix3.2.0-Fixedin3.2.0final)
        -   [Fixed in 3.1.1
            final](#ReleaseNotes-Heritrix3.2.0-Fixedin3.1.1final)
        -   [Fixed in 3.1.0
            final](#ReleaseNotes-Heritrix3.2.0-Fixedin3.1.0final)
        -   [Fixed in
            3.1.0-RC1](#ReleaseNotes-Heritrix3.2.0-Fixedin3.1.0-RC1)
        -   [Fixed in
            3.1.0-beta](#ReleaseNotes-Heritrix3.2.0-Fixedin3.1.0-beta)
    -   [4. Known Issues](#ReleaseNotes-Heritrix3.2.0-4.KnownIssues)

These are the project wiki release notes for the 3.2.0 release,
available as of Jan 8, 2014.

Heritrix3 is most suitable for advanced users and projects that are
either customizing Heritrix (with Java or other scripting code) or
embedding Heritrix in a larger system. Please review the Current
Limitations, below, to help determine if Heritrix3 or a current
Heritrix1 (1.14.4 or later) release is best suited for your needs.

Those new to Heritrix3 should also review the [Heritrix 3.0.0 Release
Notes](Release%20Notes%20-%203.0.0) for an overview of differences and
limitations compared to earlier versions.

The 3.2.0 release is available via our build box, at:

<http://builds.archive.org/maven2/org/archive/heritrix/heritrix/3.2.0/heritrix-3.2.0-dist.tar.gz>

(Source and .zip variants are available in the [same
directory](http://builds.archive.org/maven2/org/archive/heritrix/heritrix/3.2.0/).)

Documentation for Heritrix3 is available via the [Heritrix 3.0 User
Guide](Heritrix%203.0%20and%203.1%20User%20Guide), [Heritrix 3.0 API
Guide](Heritrix%203.x%20API%20Guide), and other notes on the [Heritrix
project wiki](Heritrix).

Please discuss questions, problems, and ideas at our [project discussion
list](http://archive-crawler.yahoogroups.com), and submit bug reports or
feature requests via our [project JIRA issue
tracker](https://webarchive.jira.com/browse/HER).

## 1. Version Numbering Convention

Beginning with this release, we are dropping the convention of using an
odd/even point numbering as a signal whether a build or release is
'development/testing' or 'official'. See [Version
Numbering](Version%20Numbering) for details.

## 2. New and Notable

### Through Heritrix 3.2.0 (January 2014)

Minor version number bumped because there are some changes that are not
backward-compatible. For one, heritrix now requires java 1.6. It's also
been a while since the last release, and there some some significant new
features, and lots of other changes.

#### URL-agnostic deduplication ([HER-2022](https://webarchive.jira.com/browse/HER-2022))

Deduplication for identical content, even at different urls.
Configuration is documented here: [Duplication Reduction
Processors](Duplication%20Reduction%20Processors)

#### Automatic form login ([HER-2031](https://webarchive.jira.com/browse/HER-2031))

With new processors ExtractorHTMLForms and FormLoginProcessor, heritrix
can detect typical html login forms and submit a configured username and
password to them. Configuration is documented
at <http://builds.archive.org/javadoc/heritrix-3.x-snapshot/org/archive/modules/forms/ExtractorHTMLForms.html>

#### Option to forget all but latest checkpoint (HER-2051)

Enable periodic checkpointing without worrying that it will overflow the
disk.  When enabled, earlier checkpointed logs are rolled up into new
checkpointed log, earlier bdb checkpoint dirs are deleted and earlier
checkpoint dirs are deleted. Related is
[HER-2056](https://webarchive.jira.com/browse/HER-2056), option not to
rollover warcs on checkpoint.

#### Handle stats consistently on checkpoint ([HER-2048](https://webarchive.jira.com/browse/HER-2048))

On checkpoint resumption, all stats resume counting from where they left
off when checkpointed. In addition, dns lookups are not repeated in a
checkpoint-resumed crawl (unless they're expired, same as in a normal
crawl).

#### Custom extractor that constructs outlinks from strings found in content (HER-2024)

Very flexible extractor module ExtractorMultipleRegex, which can look
for arbitrary regular expressions in the url and content of a page, and
construct urls from the matching
groups. <http://builds.archive.org/javadoc/heritrix-3.x-snapshot/org/archive/modules/extractor/ExtractorMultipleRegex.html>

#### Responsive web UI using freemarker templates ([HER-1726](https://webarchive.jira.com/browse/HER-1726))

Web UI uses freemarker templates to replace hard-coded html in java
source, and foundation for responsiveness.

#### Improved speculative link extraction from javascript ([HER-1523](https://webarchive.jira.com/browse/HER-1523))

Significant tightening of speculative link extraction heuristics based
on statistical analysis.

### Through Heritrix 3.1.1 (May 2012)

#### Nicer code editor for crawl config and script console ([HER-2001](https://webarchive.jira.com/browse/HER-2001))

The crawl configuration cxml editor and the scripting console editor now
use [CodeMirror](http://codemirror.net/), which adds syntax
highlighting, line numbers and other features

#### Fixed occasional mangling of DNS records in ARCs and WARCs ([HER-1983](https://webarchive.jira.com/browse/HER-1983))

A longstanding bug that caused some DNS records in ARCs and WARCs to be
mangled, due to unsafe use of a shared variable among threads, is now
fixed.

#### Remember all surts across checkpoint/resume ([HER-1985](https://webarchive.jira.com/browse/HER-1985))

Surts that were derived from seeds, or listed as surts in the seeds
source, or that were added using a .seeds file in the action directory,
can now be remembered across checkpoint/resume. For that to work **the
relevant SurtPrefixedDecideRule must be a top-level bean.** The default
cxml distributed with heritrix now includes the key decide rule as a
top-level bean with id "acceptSurts".

#### Support for saving script state ([HER-1984](https://webarchive.jira.com/browse/HER-1984))

Added a shared map for arbitrary use during a crawl. It can be used for
state persisting for the duration of the crawl, shared among
ScriptedProcessor, scripting console and other scripts, or other
purposes. In scripts it can be obtained with appCtx.getData().

### Through Heritrix 3.1.0 final (October 2011)

#### More conservative speculative javascript extraction ([HER-1951](https://webarchive.jira.com/browse/HER-1951))

Heritrix 3.1.0-RC1 speculative javascript extraction produced many false
positives, most of which would be 404s when crawled. As of 3.1.0 many of
the common, obvious false positives, including strings containing
characters that rarely appear in urls, strings that look like mimetypes,
and a few other cases, are not treated as likely urls.

#### A few XML API tag names have changed to follow camelcase convention ([HER-1953](https://webarchive.jira.com/browse/HER-1953))

The tag names of some children of sizeTotalReports have changed to use
camelcase, following the convention used everywhere else.

#### HTTP authentication type fallback ([HER-1917](https://webarchive.jira.com/browse/HER-1917))

Previously heritrix HTTP authentication would fail if the first
authentication method requested by the server was not supported, even if
another one was. Now fallback to the supported method works.

#### Cookie saving and loading ([HER-1914](https://webarchive.jira.com/browse/HER-1914))

Heritrix now supports saving cookies to a file and loading them from the
file.

### Through Heritrix 3.1.0-RC1 (July 2011)

#### Distinct directories for each re-launch of a job ([HER-1901](https://webarchive.jira.com/browse/HER-1901), [HER-1900](https://webarchive.jira.com/browse/HER-1900))

Heritrix will now create a new subdirectory of the job directory at the
moment of a job 'launch', to collect files uniquely related to that
launch. The CXML at the time of launch will be copied to that directory,
as well as any other files read as part of individual bean
configuration. The default paths for logs, reports, and arcs/warcs are
now set to subdirectories of the launch directory, though these may as
always be explicitly set to any desired path.

#### Use of Spring 3.0 ([HER-1908](https://webarchive.jira.com/browse/HER-1908))

Heritrix has moved to the Spring 3.0.5 inversion-of-control framework.
Operators should update their custom configurations to be based on the
new default template. (In general, simply updating the declarations in
the top &lt;bean&gt; element, along with any other properties renames as
required elsewhere, will be sufficient to bring an H3.0 configuration
forward.)

#### CrawlController pauseAtEnd option replaced with runWhileEmpty ([HER-1776](https://webarchive.jira.com/browse/HER-1776))

Previously, H3 offered the ability to auto-pause a crawl when it
appeared to have exhausted all eligible URIs. Thus, if desired, an
operator could add more URIs and 'unpause' the crawl to continue
crawling in the same job launch (or simply terminate or 'unpause' while
empty to end the crawl). Instead, H3.1 now offers the option for a crawl
to continue in an active running state even while empty (indefinitely),
via the runWhileEmpty property. The default value for this property is
false, meaning the old behavior of automatic termination when the
frontier is empty of any eligible URIs. The benefit of the new approach
is that URIs can be added at any time and crawling will continue,
without the need to 'unpause' in some situations. A crawl with
'runWhileEmpty' set will only end when explicitly terminated by operator
action.

#### Optional logExtraInfo in crawl.log, such as name of ARC/WARC file ([HER-834](https://webarchive.jira.com/browse/HER-834), [HER-1790](https://webarchive.jira.com/browse/HER-1790))

If the CrawlerLoggerModule's 'logExtraInfo' property is set to 'true'
(default is 'false'), extra information in JSON format will appear after
all other crawl.log fields. (Since the JSON includes whitespace, fields
are only whitespace-delimited up to this field.) This extra info will
include the target ARC/WARC file, if any, to which a URI's contents was
written. (Other processors may also add info here in the future.)

#### Discover charset as declared in content ([HER-741](https://webarchive.jira.com/browse/HER-741))

Heritrix HTML and XML extractors will now try to discover and use a
charset declaration appearing in the content, as long as it is
sufficiently self-consistent that the same charset declaration is
discovered once it is in effect.

#### Support for HTTP proxy authentication ([HER-915](https://webarchive.jira.com/browse/HER-915))

Heritrix can now be configured to crawl through a proxy that requires
authentication. Contributed by Adam Wilmer.

#### Allow fetching to begin before full load of large seed list ([HER-1905](https://webarchive.jira.com/browse/HER-1905))

TextSeedModule has a new property, 'blockAwaitingSeedLines', which if
non-negative will only block the beginning of active crawling for the
given number of seed lines to be enqueued into the frontier. (The
remainder of seed lines will be loaded in the background, while other
processing of the already-loaded seeds proceeds.) The default value is
'-1', meaning the old behavior, only starting fetching after all seeds
have been loaded. An example use of this new property would be when you
are starting with hundreds of thousands or millions of seeds, to begin
network fetching after only a few thousand have loaded.

Important caveats of this feature include: (1) if your scope is derived
from your seeds (not recommended for giant seed lists), URIs may be
discovered before the seed is added which expands the scope to accept
them, which may lead to unexpected undercrawling; (2) the background
thread loading the seeds is unaffected by crawl pauses and checkpoints,
and may take many hours to complete its seed-enqueueing. This thread's
completion is only confirmable indirectly (via a JVM thread dump, or
observing no further growth of 'queued' while paused).

(Crawls using large numbers of seeds also probably want to disable the
'trackSeeds' property of StatisticsTracker, as its dynamically-updated
'Seeds Report' is expensive to maintain with giant seed lists.)

#### Spring-configurable reports ([HER-1812](https://webarchive.jira.com/browse/HER-1812))

The reports that are available during a crawl, and that are written at
the end of a crawl, are now configurable, and new types of reports can
be created and added to the configuration.

#### Persisting of history optionally dependent on fetch having been archived ([HER-1791](https://webarchive.jira.com/browse/HER-1791))

PersistStoreProcessor and PersistLogProcessor have a new option
"onlyStoreIfWriteTagPresent", enabled by default. Writers such as
WARCWriterProcessor set "writeTag" on the current fetch if it, or an
earlier identical fetch, has been archived.
PersistLogProcessor/PersistStoreProcessor need to come after the writer
in the processor chain if onlyStoreIfWriteTagPresent is enabled, or
fetch history will not be persisted.

### Through Heritrix 3.1.0-beta (April 2011)

#### Optional Support for 'chunked' Transfer-Encoding, HTTP/1.1-identified requests, and 'gzip,deflate' Content-Encoding ([HER-1876](https://webarchive.jira.com/browse/HER-1876), [HER-726](https://webarchive.jira.com/browse/HER-726), [HER-1053](https://webarchive.jira.com/browse/HER-1053))

Heritrix will now properly decode the 'chunked' Transfer-Encoding when
encountered – even if encountered in a response to an HTTP/1.0 request,
when technically it should not be used. Additionally, the FetchHTTP
processor now includes the parameter 'useHTTP11' which if true will
cause Heritrix to report its requests as 'HTTP/1.1', which (among other
things) allows sites to use the 'chunked' Transfer-Encoding. (The
default for this parameter is false for now, and Heritrix still does not
reuse a persistent connection for more than one request to a site.)

FetchHTTP also now includes the parameter 'acceptCompression' which if
true will cause Heritrix requests to include an "Accept-Encoding:
gzip,deflate" header offering to receive compressed responses. (The
default for this parameter is false for now.)

As always, responses are saved to ARC/WARC files exactly as they are
received, and some bulk access/viewing tools may not currently support
chunked/compressed responses. (Future updates to the 'Wayback' tool will
address this.)

#### Easier robots-policy configuration and new capabilities ([HER-1803](https://webarchive.jira.com/browse/HER-1803), [HER-1861](https://webarchive.jira.com/browse/HER-1861), [HER-1620](https://webarchive.jira.com/browse/HER-1620), [HER-1880](https://webarchive.jira.com/browse/HER-1880))

The robots policy in effect is now primarily switched via a single short
string: CrawlMetadata's 'robotsPolicyName' parameter. The names 'obey'
and 'classic' are synonyms and always available and mean strict
compliance with standard robots.txt conventions. The name 'ignore' is
also always available and means robots.txt rules are not considered. The
parameter is Sheet-overlayable for individual sites, to allow the common
case where robots-rules are followed by default but for a small number
of crawl-affiliated/permission-granted sites, robots rules may be
ignored. Changes to the name during a crawl take effect immediately,
rather than upon next fetch of robots.txt for affected sites.

The robotsPolicyName may also be the bean name of any instance of a
RobotsPolicy subclass declared in the crawler configuration, to allow
more fine-grained (or even custom) policies. The FirstNamedRobotsPolicy
is a new policy which checks a series of User-Agents in order, and
follows the first to match any specific User-Agent directive in a site's
robots.txt.

Our robots.txt parsing now tolerates trailing '\*' wildcards in Disallow
directives (a common deviation from the original standard) as being
equivalent to the same path-prefix without a trailing '\*'. We do not
yet support the internal '\*' wildcards or trailing-anchor '$'
introduced by Google, but there is an issue,
[HER-1621](https://webarchive.jira.com/browse/HER-1621), to eventually
address this.

The handling of overlapping 'Allow' and 'Disallow' directives has been
made to match other crawlers and webmasters' likely intuitive
understanding (more specific/longer-in-length directives win)
([HER-1880](https://webarchive.jira.com/browse/HER-1880)).

#### Liveness of frontier and settings-overlay information improved ([HER-1768](https://webarchive.jira.com/browse/HER-1768), [HER-747](https://webarchive.jira.com/browse/HER-747), [HER-1823](https://webarchive.jira.com/browse/HER-1823))

Handling of queue-budgeting and rotation/retirement operations has been
refactored to ensure mid-crawl changes (via new overlay sheets or direct
editing with the bean-browse tool or scripting-console) take effect
immediately. Additionally, CrawlURIs may be marked to force the
retirement of their source queue by Processors, and the
DispositionProcessor has an (sheet-overlayable) setting to apply this
marking. More generally, settings changes via new Sheets and
Sheet-associations during a crawl (as inserted via scripting until a
separate UI is developed) now take effect on all URIs being dequeued for
processing, rather than just newly-discovered URIs.

#### Infer '/favicon.ico' and optionally root page ('/') ([HER-1799](https://webarchive.jira.com/browse/HER-1799), [HER-1010](https://webarchive.jira.com/browse/HER-1010))

The ExtractorHTTP processor will now consider any URI on a hostname as
also implying that the '/favicon.ico' from the same host should be
fetched as well. Optionally, the 'inferRootPage' setting, if true, means
to infer the '/' root page from any other URI on the same hostname, as
well. (The default for this setting, matching the old behavior of only
fetching the root page is it was a seed or otherwise discovered and
in-scope, is false.) Discovery via these new heuristics is considered to
be a new 'I' (inferred) hop-type, and is treated the same in
scoping/transclusion decisions as an 'E' (embed).

#### New global ExtractorParameters settings 'extract404s' and 'extractIndependently' ([HER-1848](https://webarchive.jira.com/browse/HER-1848), [HER-1836](https://webarchive.jira.com/browse/HER-1836))

The interface for crawl-wide extractor parameters, ExtractorParameters
(usually provided by the Frontier), includes two new settings. To avoid
extracting links from 404 ("not found") response content, set
'extract404s' to false. (Default is true, matching the old behavior.) To
encourage extractor processors to always perform their best-effort
extraction, even if a previous extractor has marked a URI as
already-handled, set 'extractIndependently' to true. (Default is false,
matching the old behavior.)

#### Improved string-might-be-URI testing ([HER-1763](https://webarchive.jira.com/browse/HER-1763))

The tests used to determine if a string (such as may be found in
otherwise unparsed/uninterpreted Javascript) is sufficiently likely to
be a URI that it may warrant a fetch attempt have been unified into a
UriUtils class and slightly improved. Note that this technique is still
error-prone, and likely to generate some false requests that
occasionally cause problems or annoyance at target websites. To refrain
this approach, either on a full crawl or on a site-by-site basis when
you notice it causing problems, disable or remove the ExtractorJS, and
set ExtractorHTML's 'extractJS' and 'extractValueAttributes' settings to
false.

#### DiskSpaceMonitor component for detecting, pausing in low-disk-space conditions ([HER-1811](https://webarchive.jira.com/browse/HER-1811))

The DiskSpaceMonitor may be added to a crawl, and configured with a list
of paths to monitor. When free space at those paths drops below a
configured level (checked at the same interval as the
progress-statistics.log is updated), the crawl will be paused.
Contributed by Kristinn Sigurðsson; replaces the LowDiskPauseProcessor.

#### New formula and default conventions for ARC/WARC naming to better guarantee uniqueness ([HER-1727](https://webarchive.jira.com/browse/HER-1727))

Instead of specifying the formula for ARC/WARC naming in code and using
a supplied 'prefix' and 'suffix', a template with variable interpolation
may be used. (The configured 'prefix' remains an available variable, as
well as other useful local machine, crawl, and writer properties.) The
default template is:

``` bash
${prefix}-${timestamp17}-${serialno}-${heritrix.pid}~${heritrix.hostname}~${heritrix.port}
```

Compared to previous practice, this adds the local process ID, and the
17-digit timestamp is provided via a service that will always ensure
that each timestamp is at least 1 millisecond after any others
previously offered. These new conventions, in this default template,
thus protect against inadvertent ARC/WARC name collisions even when many
crawls, in many JVMs on the same machine, using the same prefix, are
launched/crawling simultaneously. Although the names so generated are
long, they are extremely likely to be unique under usual conditions. We
recommend against changing this template unless you are certain your
alternate naming system also generates unique names, as downstream tools
for indexing ARCs/WARCs often assume or otherwise benefit from ARC/WARC
filename uniqueness.

#### Fetcher for 'whois' information ([HER-1645](https://webarchive.jira.com/browse/HER-1645))

Heritrix includes an optional fetcher for domain 'whois' data. A small
set of well-established 'whois' servers are preconfigured. The fetcher
uses an ad-hoc/intuitive interpretation of how a 'whois:' scheme URI
should work.

#### Frontier queue-reporting more configurable ([HER-1827](https://webarchive.jira.com/browse/HER-1827))

The standard BdbFrontier (via its superclass WorkQueueFrontier) has two
new settings, 'largestQueuesCount' (default 20) and
'maxQueuesPerReportCategory' (default 2000). These control how many of
the largest queues are tracked and reported in the textual 'frontier
report' and the maximum number of queues per category listed in the
textual 'frontier report'. Note that the largest-queues information may
be approximate when queues shrink out of the top-N, or the value is
changed mid-crawl. (The list is updated only when a queue is noted
growing into the largest group.)

#### Checkpointing based on hard-links for space savings, flexibility ([HER-1821](https://webarchive.jira.com/browse/HER-1821))

Where available, 'hard' links will now be used to collect the
BerkeleyDB-JE files required to reproduce the crawler's state, and
automatic deletion of outdated files not needed for a checkpoint (the
".DEL" files) has been reenabled. This eliminates the need to manually
delete unneeded files, and makes saving-elsewhere or clearing of old
checkpoints easier.

#### SurtPrefixedDecideRule 'surtsSource' may use file path or inline String ([HER-1857](https://webarchive.jira.com/browse/HER-1857))

To match the flexibility of TextSeedModule's 'textSource', the
SurtPrefixedDecideRule 'surtsSource' parameter may now be any
ReadSource, such as a ConfigFile (to read from a local file path) or
ConfigString (to read from the text inline in the crawler configuration
file).

#### Workaround for Java 6 update 23 GZIP incompatibilities ([HER-1865](https://webarchive.jira.com/browse/HER-1865))

Java 6 update 23 (aka JDK6u23) made a backward-incompatible change in
how GZIP streams built from multiple concatenated GZIP members were
handled by Java's GZIPInputStream. Additionally, it introduced a serious
new bug in how GZIP members with 'extra fields' are processed.
(Conventionally all ARCs and WARCs use some kind of GZIP extra field.)
As a result, the ARC/WARC reading code from earlier Heritrix releases
will not work in Java 6 update 23 and update 24 (and possibly later).
Heritrix 3.1.0's ARC/WARC reading code includes a workaround based on
the non-buggy OpenJDK7 GZIP implementation classes, which also include
the new multi-member treatment. The Heritrix 3.1.0 code should work with
both pre- and post- JDK6u23 Sun/Oracle Java distributions.

#### Proper rejection of cookies on top-level-domains/public suffixes ([HER-1864](https://webarchive.jira.com/browse/HER-1864))

Heritrix 3.0.0 incorrectly accepted and returned to other servers
cookies that some sites erroneously set on
top-level-domains/public-suffixes (like ".com"). This was most likely to
happen in very broad/national/world crawls, and could result in
impractically long and inefficient (crawl-slowing) Cookie headers. This
has been fixed.

#### Crawl.log 'hops path' now shows only last 50 hop-types ([HER-1834](https://webarchive.jira.com/browse/HER-1834))

The 5th field of the crawl.log is a symbolic representation of the path
by which a URI was discovered, where each character represented the type
of outlink followed. For example, 'LLREX' means two navigational links,
a redirect, an embed (as with a frame), and a speculative
(Javascript/plugin/media) reference. For crawls with no (or very large)
limits on link-hops-followed-from-seeds, this string could become
arbitrarily long, leading to memory and log bloat and crawl performance
problems. This string has been converted to show only the last 50
hop-types, with a leading integer indicating how many prior hops are not
shown. For example, a 62-hop path might now appear as
"12+LLRLLLRELLLLRLLLRELLLLRLLLRELLLLRLLLRELLLLRLLLRELE".

(Also note that content which is only discoverable through long paths is
increasingly likely, with path length, to be auto-generated material of
negligible value – aka 'crawler traps', whether intentional or not. So
most crawls should use some max-hop value, and we believe that value
should be closer to 'dozens' than 'hundreds' or 'thousands'.)

#### Protecting operator login credentials from casual snooping ([HER-1753](https://webarchive.jira.com/browse/HER-1753), [HER-1804](https://webarchive.jira.com/browse/HER-1804))

If the parameter supplied to the '-a' command-line option at initial
launch is a string beginning with '@', the rest of the string is taken
as a local file from which to read the operator login:password. Thus,
these credentials are not visible to all other machine users via
process-listings. (Of course, if other users are a concern, the local
file, and all other job/class files consulted by Heritrix, must also be
access-protected.)

Additionally, the output echoed to the terminal and heritrix\_out.log
now only reminds how the credentials were set, without echoing them, in
case the terminal or log are (or become) more widely viewable.

Remember, because of the flexibility of the web operator interface in
editing/viewing all local files readable by the crawler process, and the
ability to include arbitrary scripting code in multiple JVM languages in
crawl configurations, **access to the crawler operator web interface
gives near-total access to the hosting machine**. The crawl operator can
do anything through the user interface that the user the crawler is
running as could do at a shell. So be sure to secure your running
instances of Heritrix, in accordance with the recommendations at
[Security Considerations](Security%20Considerations) and your own
organizational practices.

## 3. All Tracked Changes

An exhaustive list of changes through 3.2.0 can be found
here: <https://github.com/internetarchive/heritrix3/commits/3.2.0>

The following tracked issues are recorded as addressed in this 3.2.0
release:

#### Fixed in 3.2.0 final

|                                                                       |                                                                                                                                                                           |                    |             |                                                                                |            |
|:----------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|:------------|:-------------------------------------------------------------------------------|:-----------|
| Key                                                                   | Summary                                                                                                                                                                   | Created            | Reporter    | P                                                                              | Resolution |
| [HER-2059](https://webarchive.jira.com/browse/HER-2059?src=confmacro) | [support url with two consecutive question marks "??"](https://webarchive.jira.com/browse/HER-2059?src=confmacro)                                                         | Dec 07, 2013 03:17 | Noah Levitt | ![Major](https://webarchive.jira.com/images/icons/priorities/major.svg){.icon} | Fixed      |
| [HER-2056](https://webarchive.jira.com/browse/HER-2056?src=confmacro) | [on checkpoint w/arcs are closed and new ones started; add option not to do that](https://webarchive.jira.com/browse/HER-2056?src=confmacro)                              | Oct 11, 2013 00:37 | Noah Levitt | ![Major](https://webarchive.jira.com/images/icons/priorities/major.svg){.icon} | Fixed      |
| [HER-2051](https://webarchive.jira.com/browse/HER-2051?src=confmacro) | [option to forget all but latest checkpoint](https://webarchive.jira.com/browse/HER-2051?src=confmacro)                                                                   | Sep 11, 2013 20:23 | Noah Levitt | ![Major](https://webarchive.jira.com/images/icons/priorities/major.svg){.icon} | Done       |
| [HER-2048](https://webarchive.jira.com/browse/HER-2048?src=confmacro) | [checkpoint-resumed crawl job stats are inconsistent-- some start from 0, some resume from checkpoint numbers](https://webarchive.jira.com/browse/HER-2048?src=confmacro) | Sep 07, 2013 16:47 | Noah Levitt | ![Major](https://webarchive.jira.com/images/icons/priorities/major.svg){.icon} | Fixed      |
| [HER-2042](https://webarchive.jira.com/browse/HER-2042?src=confmacro) | [url agnostic duplicate urls don't appear as such in stats if revisit record not written](https://webarchive.jira.com/browse/HER-2042?src=confmacro)                      | Jun 08, 2013 00:15 | Noah Levitt | ![Major](https://webarchive.jira.com/images/icons/priorities/major.svg){.icon} | Fixed      |

Showing 5 out of 32 issues

#### Fixed in 3.1.1 final

|                                                                       |                                                                                                                                         |                    |                 |                                                                                    |            |
|:----------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------|:-------------------|:----------------|:-----------------------------------------------------------------------------------|:-----------|
| Key                                                                   | Summary                                                                                                                                 | Created            | Reporter        | P                                                                                  | Resolution |
| [HER-2006](https://webarchive.jira.com/browse/HER-2006?src=confmacro) | [option to set bdb cache size as an absolute number instead of a percentage](https://webarchive.jira.com/browse/HER-2006?src=confmacro) | Apr 20, 2012 19:36 | Noah Levitt     | ![Major](https://webarchive.jira.com/images/icons/priorities/major.svg){.icon}     | Fixed      |
| [HER-2005](https://webarchive.jira.com/browse/HER-2005?src=confmacro) | [existing content length decide rule is not flexible enough](https://webarchive.jira.com/browse/HER-2005?src=confmacro)                 | Apr 18, 2012 20:11 | Noah Levitt     | ![Major](https://webarchive.jira.com/images/icons/priorities/major.svg){.icon}     | Fixed      |
| [HER-2004](https://webarchive.jira.com/browse/HER-2004?src=confmacro) | [SEVERE error in FetchWhois on some government domains](https://webarchive.jira.com/browse/HER-2004?src=confmacro)                      | Apr 17, 2012 19:47 | Kenji Nagahashi | ![Major](https://webarchive.jira.com/images/icons/priorities/major.svg){.icon}     | Fixed      |
| [HER-2001](https://webarchive.jira.com/browse/HER-2001?src=confmacro) | [Nicer code editor for crawl config and script console](https://webarchive.jira.com/browse/HER-2001?src=confmacro)                      | Mar 31, 2012 06:56 | Alex Osborne    | ![Minor](https://webarchive.jira.com/images/icons/priorities/minor.svg){.icon}     | Fixed      |
| [HER-1993](https://webarchive.jira.com/browse/HER-1993?src=confmacro) | [Clean up HTML in web interface](https://webarchive.jira.com/browse/HER-1993?src=confmacro)                                             | Feb 29, 2012 21:55 | Kenji Nagahashi | ![Trivial](https://webarchive.jira.com/images/icons/priorities/trivial.svg){.icon} | Fixed      |

Showing 5 out of 16 issues

#### Fixed in 3.1.0 final

|                                                                       |                                                                                                                                                    |                    |                |                                                                                |            |
|:----------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|:---------------|:-------------------------------------------------------------------------------|:-----------|
| Key                                                                   | Summary                                                                                                                                            | Created            | Reporter       | P                                                                              | Resolution |
| [HER-1960](https://webarchive.jira.com/browse/HER-1960?src=confmacro) | [kryo buffer can hog memory, lead to oome](https://webarchive.jira.com/browse/HER-1960?src=confmacro)                                              | Oct 20, 2011 02:18 | Noah Levitt    | ![Major](https://webarchive.jira.com/images/icons/priorities/major.svg){.icon} | Fixed      |
| [HER-1958](https://webarchive.jira.com/browse/HER-1958?src=confmacro) | [race condition on frontier inactive queues](https://webarchive.jira.com/browse/HER-1958?src=confmacro)                                            | Oct 12, 2011 19:14 | Noah Levitt    | ![Major](https://webarchive.jira.com/images/icons/priorities/major.svg){.icon} | Fixed      |
| [HER-1955](https://webarchive.jira.com/browse/HER-1955?src=confmacro) | [Some annoying interaction between new creation of latest link and disk full java bean](https://webarchive.jira.com/browse/HER-1955?src=confmacro) | Sep 30, 2011 19:04 | John Lekashman | ![Minor](https://webarchive.jira.com/images/icons/priorities/minor.svg){.icon} | Fixed      |
| [HER-1954](https://webarchive.jira.com/browse/HER-1954?src=confmacro) | [bdb closed at crawl finish instead of teardown](https://webarchive.jira.com/browse/HER-1954?src=confmacro)                                        | Sep 29, 2011 00:17 | Noah Levitt    | ![Major](https://webarchive.jira.com/images/icons/priorities/major.svg){.icon} | Fixed      |
| [HER-1953](https://webarchive.jira.com/browse/HER-1953?src=confmacro) | [all api xml elements are camelcase except sizeTotalsReport fields](https://webarchive.jira.com/browse/HER-1953?src=confmacro)                     | Sep 28, 2011 00:16 | Noah Levitt    | ![Major](https://webarchive.jira.com/images/icons/priorities/major.svg){.icon} | Fixed      |

Showing 5 out of 32 issues

#### Fixed in 3.1.0-RC1

|                                                                       |                                                                                                                                                                         |                    |                 |                                                                                |            |
|:----------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|:----------------|:-------------------------------------------------------------------------------|:-----------|
| Key                                                                   | Summary                                                                                                                                                                 | Created            | Reporter        | P                                                                              | Resolution |
| [HER-1912](https://webarchive.jira.com/browse/HER-1912?src=confmacro) | [Kryo-deserialization of Robotstxt can consume excess memory by creating multiple copies of RobotsDirective](https://webarchive.jira.com/browse/HER-1912?src=confmacro) | Jul 22, 2011 00:22 | Kenji Nagahashi | ![Major](https://webarchive.jira.com/images/icons/priorities/major.svg){.icon} | Fixed      |
| [HER-1911](https://webarchive.jira.com/browse/HER-1911?src=confmacro) | [H3: make writer-pool 'maxActive' setting adjustable mid-crawl](https://webarchive.jira.com/browse/HER-1911?src=confmacro)                                              | Jul 08, 2011 21:56 | Gordon Mohr     | ![Major](https://webarchive.jira.com/images/icons/priorities/major.svg){.icon} | Fixed      |
| [HER-1910](https://webarchive.jira.com/browse/HER-1910?src=confmacro) | [H3: job-related pages very slow to render (pause mid-way through) in large crawls](https://webarchive.jira.com/browse/HER-1910?src=confmacro)                          | Jul 07, 2011 20:54 | Gordon Mohr     | ![Major](https://webarchive.jira.com/images/icons/priorities/major.svg){.icon} | Fixed      |
| [HER-1909](https://webarchive.jira.com/browse/HER-1909?src=confmacro) | [H3: slow checkpoint resume, locking out web UI during resume](https://webarchive.jira.com/browse/HER-1909?src=confmacro)                                               | Jul 07, 2011 20:49 | Gordon Mohr     | ![Major](https://webarchive.jira.com/images/icons/priorities/major.svg){.icon} | Fixed      |
| [HER-1908](https://webarchive.jira.com/browse/HER-1908?src=confmacro) | [H3: upgrade to Spring 3](https://webarchive.jira.com/browse/HER-1908?src=confmacro)                                                                                    | Jun 28, 2011 22:10 | Gordon Mohr     | ![Major](https://webarchive.jira.com/images/icons/priorities/major.svg){.icon} | Fixed      |

Showing 5 out of 29 issues

#### Fixed in 3.1.0-beta

|                                                                       |                                                                                                                                                     |                    |              |                                                                                |            |
|:----------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|:-------------|:-------------------------------------------------------------------------------|:-----------|
| Key                                                                   | Summary                                                                                                                                             | Created            | Reporter     | P                                                                              | Resolution |
| [HER-1906](https://webarchive.jira.com/browse/HER-1906?src=confmacro) | [checkpointing gives error on Windows](https://webarchive.jira.com/browse/HER-1906?src=confmacro)                                                   | Jun 23, 2011 20:42 | Hunter Stern | ![Minor](https://webarchive.jira.com/images/icons/priorities/minor.svg){.icon} | Fixed      |
| [HER-1880](https://webarchive.jira.com/browse/HER-1880?src=confmacro) | [robots.txt less specific Allow overrides more specific Disallow](https://webarchive.jira.com/browse/HER-1880?src=confmacro)                        | Apr 13, 2011 22:49 | Noah Levitt  | ![Major](https://webarchive.jira.com/images/icons/priorities/major.svg){.icon} | Fixed      |
| [HER-1878](https://webarchive.jira.com/browse/HER-1878?src=confmacro) | [NullPointerException when parsing (some?) WARC files over slow connections](https://webarchive.jira.com/browse/HER-1878?src=confmacro)             | Apr 08, 2011 04:19 | Erik Hetzner | ![Major](https://webarchive.jira.com/images/icons/priorities/major.svg){.icon} | Fixed      |
| [HER-1876](https://webarchive.jira.com/browse/HER-1876?src=confmacro) | [Offer HTTP/1.1 option - for chunked transfer-encoding (but not persistent connections)](https://webarchive.jira.com/browse/HER-1876?src=confmacro) | Apr 06, 2011 20:27 | Gordon Mohr  | ![Major](https://webarchive.jira.com/images/icons/priorities/major.svg){.icon} | Fixed      |
| [HER-1872](https://webarchive.jira.com/browse/HER-1872?src=confmacro) | [PersistLoadProcessor preloadSource does not support url (regression from h1)](https://webarchive.jira.com/browse/HER-1872?src=confmacro)           | Feb 26, 2011 00:25 | Noah Levitt  | ![Major](https://webarchive.jira.com/images/icons/priorities/major.svg){.icon} | Fixed      |

Showing 5 out of 88 issues

## 4. Known Issues

To be determined; follow the [project JIRA issue
tracker](https://webarchive.jira.com/browse/HER) for the latest info.

 
