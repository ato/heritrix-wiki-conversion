# Release Notes - 1.14.0

# Release Notes - 1.14.0 (April 2008)

These are the project wiki Release Notes for the 1.14.0 release.

Release 1.14.0 adds a number of small features to the Heritrix 1.x line,
most notably upgrading support for the WARC archived-web-content format
to version 0.17 (ISO Committee Draft). This release also includes 41 bug
fixes or other incremental improvements, including several based on
community contributions or requests.

The 1.14.0 release is now available at [the archive-crawler Sourceforge
project](http://sourceforge.net/project/showfiles.php?group_id=73833&package_id=73980&release_id=595427).

## Notable Changes

### WARC/0.17 support ([HER-1180](https://webarchive.jira.com/browse/HER-1180))

The WARC support now matches the 0.17 specification version (ISO
Committee Draft). The prefix 'Experimental' has been removed from WARC
support class names.

### 'Public suffix'-based queue policy ([HER-1175](https://webarchive.jira.com/browse/HER-1175), [HER-1177](https://webarchive.jira.com/browse/HER-1177))

A new TopmostAssignedSurtQueueAssignmentPolicy assigns URIs to queues
based on the information from publicsuffix.org. Specifically, the queue
name will be based on the SURT form of the topmost domain that may be
assigned from a name registry. This tends to group related subdomains in
the same queue.

### Hosts Report ([HER-1254](https://webarchive.jira.com/browse/HER-1254))

The hosts report automatically dumped at the end of a crawl has two
additional fields per listed host: number of URIs discovered but not
fetched due to robots.txt rules, and number of URIs still pending/queued
when the crawl ended.

### BdbFrontier "dump-pending-at-close" Option ([HER-1255](https://webarchive.jira.com/browse/HER-1255))

BdbFrontier has a new 'expert' setting, "dump-pending-at-close". If
true, during crawl termination, all URIs still pending/queued will be
logged to the crawl.log with status '0' (untried).

### JMX 'dumpUris' operation ([HER-1154](https://webarchive.jira.com/browse/HER-1154))

CrawlJob offers a new 'dumpUris' JMX operation, which offers options
similar to the view URIs option in the web admin UI, but dumps URIs to a
local file.

### Fixes for OutOfMemoryError (OOME) Risks ([HER-1449](https://webarchive.jira.com/browse/HER-1449), [HER-1171](https://webarchive.jira.com/browse/HER-1171))

Two distinct risks for triggering an OutOfMemoryError have been removed,
one concerning heap memory exhaustion in large crawls requiring many
queues, and the other non-heap memory exhaustion when
garbage-collection-triggered finalization may lag in a fast crawl
needing little heap memory.

### Renamed settings: 'overly-eager-link-detection' ([HER-1439](https://webarchive.jira.com/browse/HER-1439)) and 'bind-address' ([HER-1045](https://webarchive.jira.com/browse/HER-1045))

Two settings with potentially-confusing names have been renamed.
'overly-eager-link-detection' in ExtractorHTML and JerichoExtractorHTML,
with a default value of 'true', has been renamed
'extract-value-attributes' to more accurately reflect its effect.
'bind-address' in FetchHTTP, with a default value of the empty string,
has been renamed 'http-bind-address', for consistency with
'http-proxy-host' and 'http-proxy-host' and to avoid confusion with the
admin web UI bind address.

If you use previous version order.xml configuration files with the old
setting names in Heritrix, you will receive non-fatal logged/alert
warnings about "Unknown attribute". To avoid these warnings, either
rename the old settings in the order.xml or, if you are happy with the
default values, you may simply delete the old settings.

## Additional contributors

In addition to the [usual
suspects](http://crawler.archive.org/team-list.html), this release
includes contributed fixes or functionality from:

-   Matt Sanford
-   Eric C. Jensen
-   Kohei TAKEDA

## All Tracked Changes

The following tracked issues are recorded as addressed in this 1.14.0
release:

<http://webteam.archive.org/jira/secure/ReleaseNote.jspa?projectId=10021&styleName=Html&version=10020>

type

key

summary

status

Unable to locate JIRA server for this macro. It may be due to
Application Link configuration.
