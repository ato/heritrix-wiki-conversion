# Reports

Reports are found in the "reports" directory, which exists under the
directory of a specific job.  The location of specific report files are
provided in the "Configuration-referenced paths" section of the job
page.

###### Crawl Summary (crawl-report.txt)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Field Name<br />
</p></th>
<th><p>Description<br />
</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Crawl Name<br />
</p></td>
<td><p>The user-defined name of the crawl.<br />
</p></td>
</tr>
<tr class="even">
<td><p>Crawl Status<br />
</p></td>
<td><p>The status of the crawl, such as &quot;Aborted&quot; or &quot;Finished.&quot;<br />
</p></td>
</tr>
<tr class="odd">
<td><p>Duration Time<br />
</p></td>
<td><p>The duration of the crawl to the nearest millisecond.<br />
</p></td>
</tr>
<tr class="even">
<td><p>Total Seeds Crawled<br />
</p></td>
<td><p>The number of seeds that were successfully crawled.<br />
</p></td>
</tr>
<tr class="odd">
<td><p>Total Seeds Not Crawled<br />
</p></td>
<td><p>The number of seeds that were not successfully crawled.<br />
</p></td>
</tr>
<tr class="even">
<td><p>Total Hosts Crawled<br />
</p></td>
<td><p>The number of hosts that were crawled.<br />
</p></td>
</tr>
<tr class="odd">
<td><p>Total URIs Processed<br />
</p></td>
<td><p>The number of URIs that were processed.<br />
</p></td>
</tr>
<tr class="even">
<td><p>URIs Crawled Successfully<br />
</p></td>
<td><p>The number of URIs that were crawled successfully.<br />
</p></td>
</tr>
<tr class="odd">
<td><p>URIs Failed to Crawl<br />
</p></td>
<td><p>The number of URIs that could not be crawled.<br />
</p></td>
</tr>
<tr class="even">
<td><p>URIs Disregarded<br />
</p></td>
<td><p>The number of URIs that were not selected for crawling.<br />
</p></td>
</tr>
<tr class="odd">
<td><p>Processed docs/sec<br />
</p></td>
<td><p>The average number of documents processed per second.<br />
</p></td>
</tr>
<tr class="even">
<td><p>Bandwidth in Kbytes/sec<br />
</p></td>
<td><p>The average number of kilobytes processed per second.<br />
</p></td>
</tr>
<tr class="odd">
<td><p>Total Raw Data Size in Bytes<br />
</p></td>
<td><p>The total amount of data crawled.<br />
</p></td>
</tr>
<tr class="even">
<td><p>Novel Bytes<br />
</p></td>
<td><p>New bytes since last crawl.<br />
</p></td>
</tr>
</tbody>
</table>

###### Seeds (seeds-report.txt)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Field Name<br />
</p></th>
<th><p>Description<br />
</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>code<br />
</p></td>
<td><p>0=not crawled<br />
1=crawled<br />
</p></td>
</tr>
<tr class="even">
<td><p>status<br />
</p></td>
<td><p>Human readable description of whether the seed was crawled.  For example, &quot;CRAWLED.&quot;<br />
</p></td>
</tr>
<tr class="odd">
<td><p>seed<br />
</p></td>
<td><p>The seed URI.<br />
</p></td>
</tr>
<tr class="even">
<td><p>redirect<br />
</p></td>
<td><p>The URI to which the seed redirected.<br />
</p></td>
</tr>
</tbody>
</table>

###### Hosts (hosts-report.txt)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Field Name<br />
</p></th>
<th><p>Description<br />
</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>#urls<br />
</p></td>
<td><p>The number of URIs crawled for the host.<br />
</p></td>
</tr>
<tr class="even">
<td><p>#bytes<br />
</p></td>
<td><p>The number of bytes crawled for the host.<br />
</p></td>
</tr>
<tr class="odd">
<td><p>host<br />
</p></td>
<td><p>The hostname.<br />
</p></td>
</tr>
<tr class="even">
<td><p>#robots<br />
</p></td>
<td><p>The number of URIs, for this host, excluded because of <code>robots.txt</code> restrictions.  This number does not include linked URIs from the specifically excluded URIs.<br />
</p></td>
</tr>
<tr class="odd">
<td><p>#remaining<br />
</p></td>
<td><p>The number of URIs, for this host, that have not been crawled yet, but are in the queue.<br />
</p></td>
</tr>
<tr class="even">
<td><p>#novel-urls<br />
</p></td>
<td><p>The number of new URIs crawled for this host since the last crawl.</p></td>
</tr>
<tr class="odd">
<td><p>#novel-bytes</p></td>
<td><p>The amount of new bytes crawled for this host since the last crawl.</p></td>
</tr>
<tr class="even">
<td><p>#dup-by-hash-urls<br />
</p></td>
<td><p>The number of URIs, for this host, that had the same hash code and are essentially duplicates.</p></td>
</tr>
<tr class="odd">
<td><p>#dup-by-hash-bytes<br />
</p></td>
<td><p>The number of bytes of content, for this host, having the same hashcode.</p></td>
</tr>
<tr class="even">
<td><p>#not-modified-urls<br />
</p></td>
<td><p>The number of URIs, for this host, that returned a <a href="http://en.wikipedia.org/wiki/List_of_HTTP_status_codes#3xx_Redirection">304</a> status code.</p></td>
</tr>
<tr class="odd">
<td><p>#not-modified-bytes<br />
</p></td>
<td><p>The amount of of bytes of content, for this host, whose URIs returned a <a href="http://en.wikipedia.org/wiki/List_of_HTTP_status_codes#3xx_Redirection">304</a> status code.</p></td>
</tr>
</tbody>
</table>

###### SourceTags (source-report.txt)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Field Name<br />
</p></th>
<th><p>Description<br />
</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>source<br />
</p></td>
<td><p>The seed.<br />
</p></td>
</tr>
<tr class="even">
<td><p>host<br />
</p></td>
<td><p>The host that was accessed from the seed.<br />
</p></td>
</tr>
<tr class="odd">
<td><p>#urls<br />
</p></td>
<td><p>The number of URIs crawled for this seed host combination.<br />
</p></td>
</tr>
</tbody>
</table>

Note that the SourceTags report will only be generated if the
`sourceTagSeeds` property of the `TextSeedModule` bean is set to true.

``` xml
<bean id="seeds" class="org.archive.modules.seeds.TextSeedModule">
<property name="sourceTagsSeeds">
<value>
true
</value>
</property>
</bean>
```

###### Mimetypes (mimetype-report.txt)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Field Name<br />
</p></th>
<th><p>Description<br />
</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>#urls<br />
</p></td>
<td><p>The number of URIs crawled for a given mime-type.<br />
</p></td>
</tr>
<tr class="even">
<td><p>#bytes<br />
</p></td>
<td><p>The number of bytes crawled for a given mime-type.<br />
</p></td>
</tr>
<tr class="odd">
<td><p>mime-types<br />
</p></td>
<td><p>The mime-type.<br />
</p></td>
</tr>
</tbody>
</table>

###### ResponseCode (responsecode-report.txt)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Field Name<br />
</p></th>
<th><p>Description<br />
</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>#urls<br />
</p></td>
<td><p>The number of URIs crawled for a given response code.<br />
</p></td>
</tr>
<tr class="even">
<td><p>rescode<br />
</p></td>
<td><p>The response code.<br />
</p></td>
</tr>
</tbody>
</table>

###### Processors (processors-report.txt)

This report shows the activity of each processor involved in the crawl. 
For example, the `FetchHTTP` processor is included in the report.  For
this processor the number of URIs fetched is displayed.  The report is
organized to report on each Chain (Candidate, Fetch, and Disposition)
and each processor in each chain.  The order of the report is per the
configuration order in the `crawler-beans.cxml` file.

###### FrontierSummary (frontier-summary-report.txt)

This link displays a report showing the hosts that are queued for
capture.  The hosts are contained in multiple queues.  The details of
each Frontier queue is reported.

###### ToeThreads (threads-report.txt)

This link displays a report showing the activity of each thread used by
Heritrix.  The amount of time the thread has been running is displayed
as well as thread state and thread Blocked/Waiting status.
