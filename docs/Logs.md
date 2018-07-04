# Logs

Each crawl job has its own set of log files.

Logs are found in the "logs" directory, which exists under the directory
of a specific job. The location of specific log files are provided in
the "Configuration-referenced paths" section of the job page.

##### Logging Properties

Logging properties can be set by modifying the logging.properties file
that is located under the ./conf directory.  For information on using
logging properties, visit <http://logging.apache.org/log4j/>.

##### Log Files

###### alerts.log

This log contains alerts that indicate problems with a crawl.

###### crawl.log

Each URI that Heritrix attempts to fetch will cause a log line to be
written to the `crawl.log` file.  Below is a two line extract from the
log.

``` bash
2011-06-23T17:12:08.802Z   200       1299 http://content-5.powells.com/robots.txt LREP http://content-5.powells.com/cgi-bin/imageDB.cgi?isbn=9780385518635 text/plain #014 20110623171208574+225 sha1:YI
UOKDGOLGI5JYHDTXRFFQ5FF4N2EJRV - -
2011-06-23T17:12:09.591Z   200      15829 http://www.identitytheory.com/etexts/poetics.html L http://www.identitytheory.com/ text/html #025 20110623171208546+922 sha1:7AJUMSDTOMT4FN7MBFGGNJU3Z56MLCMW
- -
```

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Field Name</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Timestamp</p></td>
<td><p>The timestamp in ISO8601 format, to millisecond resolution.  The time is the instant of logging.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://webarchive.jira.com/wiki/spaces/ARIH/pages/5052">Fetch Status Code</a></p></td>
<td><p>Usually this is the HTTP response code but it can also be a negative number if URI processing was unexpectedly terminated.</p></td>
</tr>
<tr class="odd">
<td><p>Document Size</p></td>
<td><p>The size of the downloaded document in bytes.  For HTTP, this is the size of content only.  The size excludes the HTTP response headers.  For DNS, the size field is the total size for the DNS response.</p></td>
</tr>
<tr class="even">
<td><p>Downloaded URI</p></td>
<td><p>The URI of the document downloaded.</p></td>
</tr>
<tr class="odd">
<td><p>Discovery Path</p></td>
<td><p>The breadcrumb codes (discovery path) showing the trail of downloads that lead to the downloaded URI.  As of Heritrix 3.1, the length of the discovery path has been limited to the last 50 hop-types.  For example, a 62-hop path might now appear as &quot;12+LLRLLLRELLLLRLLLRELLLLRLLLRELLLLRLLLRELLLLRLLLRELE&quot;.  This enhancement decreases the size of the log and limits memory usage.</p>
<p>The breadcrumb codes are as follows.</p>
<div class="table-wrap">
<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><code>R</code></p></td>
<td><p>Redirect</p></td>
</tr>
<tr class="even">
<td><code>E</code></td>
<td><p>Embed</p></td>
</tr>
<tr class="odd">
<td><code>X</code></td>
<td><p>Speculative embed (aggressive/Javascript link extraction)</p></td>
</tr>
<tr class="even">
<td><code>L</code></td>
<td><p>Link</p></td>
</tr>
<tr class="odd">
<td><code>P</code></td>
<td><p>Prerequisite (as for DNS or robots.txt before another URI)</p></td>
</tr>
</tbody>
</table>
</div></td>
</tr>
<tr class="even">
<td><p>Referrer</p></td>
<td><p>The URI that immediately preceded the downloaded URI.  This is the referrer.  Both the discovery path and the referrer will be empty for seed URIs.</p></td>
</tr>
<tr class="odd">
<td><p>Mime Type</p></td>
<td><p>The downloaded document mime type.</p></td>
</tr>
<tr class="even">
<td><p>Worker Thread ID</p></td>
<td><p>The id of the worker thread that downloaded the document.</p></td>
</tr>
<tr class="odd">
<td><p>Fetch Timestamp</p></td>
<td><p>The timestamp in RFC2550/ARC condensed digits-only format indicating when the network fetch was started.  If appropriate the millisecond duration of the fetch is appended to the timestamp with a &quot;+&quot; character as separator.</p></td>
</tr>
<tr class="even">
<td><p>SHA1 Digest</p></td>
<td><p>The SHA1 digest of the content only (headers are not digested).</p></td>
</tr>
<tr class="odd">
<td><p>Source Tag</p></td>
<td><p>The source tag inherited by the URI, if source tagging is enabled.</p></td>
</tr>
<tr class="even">
<td><p>Annotations</p></td>
<td><p>If an annotation has been set, it will be displayed.  Possible annotations include: the number of times the URI was tried, the literal &quot;lenTrunc&quot; if the download was truncanted due to exceeding configured size limits, the literal &quot;timeTrunc&quot; if the download was truncated due to exceeding configured time limits or &quot;midFetchTrunc&quot; if a midfetch filter determined the download should be truncated.</p></td>
</tr>
<tr class="odd">
<td><p>warc</p></td>
<td><p>The name of the WARC/ARC file to which the crawled content is written.  This value will only be written if the logExtraInfo property of the loggerModule bean is set to true.  This logged information will be written in <a href="http://www.json.org/">JSON</a> format.</p></td>
</tr>
</tbody>
</table>

###### progress-statistics.log

This log is written by the StatisticsTracker bean.  At configurable
intervals, a log line detailing the progress of the crawl is written to
this file.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Field Name</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>timestamp</p></td>
<td><p>Timestamp in ISO8601 format indicating when the log line was written.</p></td>
</tr>
<tr class="even">
<td><p>discovered</p></td>
<td><p>Number of URIs discovered to date.</p></td>
</tr>
<tr class="odd">
<td><p>queued</p></td>
<td><p>Number of URIs currently queued.</p></td>
</tr>
<tr class="even">
<td><p>downloaded</p></td>
<td><p>Number of URIs downloaded to date.</p></td>
</tr>
<tr class="odd">
<td><p>doc/s(avg)</p></td>
<td><p>Number of document downloaded per second since the last snapshot.  The value in parenthesis is measured since the crawl began.</p></td>
</tr>
<tr class="even">
<td><p>KB/s(avg)</p></td>
<td><p>Amount in kilobytes downloaded per second since the last snapshot.  The value in parenthesis is measured since the crawl began.</p></td>
</tr>
<tr class="odd">
<td><p>dl-failures</p></td>
<td><p>Number of URIs that Heritrix has failed to download.</p></td>
</tr>
<tr class="even">
<td><p>busy-thread</p></td>
<td><p>Number of toe threads busy processing a URI.</p></td>
</tr>
<tr class="odd">
<td><p>mem-use-KB</p></td>
<td><p>Amount of memory in use by the Java Virtual Machine.</p></td>
</tr>
<tr class="even">
<td><p>heap-size-KB</p></td>
<td><p>The current heap size of the Java Virtual Machine.</p></td>
</tr>
<tr class="odd">
<td><p>congestion</p></td>
<td><p>The congestion ratio is a rough estimate of how much initial capacity, as a multiple of current capacity, would be necessary to crawl the current workload at the maximum rate available given politeness settings.  This value is calculated by comparing the number of internal queues that are progressing against those that are waiting for a thread to become available.</p></td>
</tr>
<tr class="even">
<td><p>max-depth</p></td>
<td><p>The size of the Frontier queue with the largest number of queued URIs.</p></td>
</tr>
<tr class="odd">
<td><p>avg-depth</p></td>
<td><p>The average size of all the Frontier queues.   </p></td>
</tr>
</tbody>
</table>

###### runtime-errors.log

This log captures unexpected exceptions and errors that occur during the
crawl. Some may be due to hardware limitations (out of memory, although
that error may occur without being written to this log), but most are
probably due to software bugs, either in Heritrix's core but more likely
in one of its pluggable classes.

###### uri-errors.log

This log stores errors that resulted from attempted URI fetches. 
Usually the cause is non-existent URIs.  This log is usually only of
interest to advanced users trying to explain unexpected crawl behavior.

###### frontier.recover.gz

The `frontier.recover.gz` file is a gzipped journal of Frontier events.
It can be used to restore the Frontier after a crash.
