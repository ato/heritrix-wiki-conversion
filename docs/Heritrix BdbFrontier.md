# Heritrix BdbFrontier

The BdbFrontier visits URIs and discovered sites in a generally
breadth-first manner.  It offers configuration options for controlling
how it throttles activity against particular hosts.  Other configuration
options allow a bias towards finishing hosts in progress ("site-first"
crawling) or cycling among all hosts with pending URIs.

Discovered URIs are only crawled once.  The exception is `robots.txt`
and DNS information, which can be configured so that it is refreshed at
specific intervals for each host.

As of Heritrix 3.1, there are two new properties.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Property Name</p></th>
<th><p>Default</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>largestQueuesCount</p></td>
<td><p>20</p></td>
<td><p>This property controls how many of the largest queues are tracked and reported in the &quot;frontier report&quot;.<br />
</p></td>
</tr>
<tr class="even">
<td><p>maxQueuesPerReportCategory<br />
</p></td>
<td><p>2000</p></td>
<td><p>This property controls the maximum number of queues per category listed in the &quot;frontier report&quot;.<br />
</p></td>
</tr>
</tbody>
</table>

Note that the largest-queues information may be approximate when queues
shrink out of the top-N or the value is changed mid-crawl. The list is
updated only when a queue grows into the largest group.
