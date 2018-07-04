# Status Codes

###### Status codes

Each crawled URI gets a status code.  This code (or number) indicates
the result of a URI fetch in Heritrix.

Codes ranging from 200 to 599 are standard HTTP response codes and
information about their meanings is available at the [World Wide Web
consortium's Web
page](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html).

Other Heritrix status codes are listed below.

<table>
<thead>
<tr class="header">
<th><p>Code</p></th>
<th><p>Meaning</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>1</p></td>
<td><p>Successful DNS lookup</p></td>
</tr>
<tr class="even">
<td><p>0</p></td>
<td><p>Fetch never tried (perhaps protocol unsupported or illegal URI)</p></td>
</tr>
<tr class="odd">
<td><p>-1</p></td>
<td><p>DNS lookup failed</p></td>
</tr>
<tr class="even">
<td><p>-2</p></td>
<td><p>HTTP connect failed</p></td>
</tr>
<tr class="odd">
<td><p>-3</p></td>
<td><p>HTTP connect broken</p></td>
</tr>
<tr class="even">
<td><p>-4</p></td>
<td><p>HTTP timeout</p></td>
</tr>
<tr class="odd">
<td><p>-5</p></td>
<td><p>Unexpected runtime exception.  See runtime-errors.log.</p></td>
</tr>
<tr class="even">
<td><p>-6</p></td>
<td><p>Prerequisite domain-lookup failed, precluding fetch attempt.<br />
(the main pre-requisite is WHOIS lookup. If you see this it's likely the domain doesn't exist anymore)</p></td>
</tr>
<tr class="odd">
<td><p>-7</p></td>
<td><p>URI recognized as unsupported or illegal.</p></td>
</tr>
<tr class="even">
<td><p>-8</p></td>
<td><p>Multiple retries failed, retry limit reached.</p></td>
</tr>
<tr class="odd">
<td><p>-50</p></td>
<td><p>Temporary status assigned to URIs awaiting preconditions.  Appearance in logs may be a bug.</p></td>
</tr>
<tr class="even">
<td><p>-60</p></td>
<td><p>URIs assigned a failure status.  They could not be queued by the Frontier and may be unfetchable.</p></td>
</tr>
<tr class="odd">
<td><p>-61</p></td>
<td><p>Prerequisite robots.txt fetch failed, precluding a fetch attempt.</p></td>
</tr>
<tr class="even">
<td><p>-62</p></td>
<td><p>Some other prerequisite failed, precluding a fetch attempt.</p></td>
</tr>
<tr class="odd">
<td><p>-63</p></td>
<td><p>A prerequisite (of any type) could not be scheduled, precluding a fetch attempt.</p></td>
</tr>
<tr class="even">
<td>-404</td>
<td>Empty HTTP response interpreted as a 404.</td>
</tr>
<tr class="odd">
<td><p>-3000</p></td>
<td><p>Severe Java Error condition occured such as OutOfMemoryError or StackOverflowError during URI processing.</p></td>
</tr>
<tr class="even">
<td><p>-4000</p></td>
<td><p>&quot;Chaff&quot; detection of traps/content with negligible value applied.</p></td>
</tr>
<tr class="odd">
<td><p>-4001</p></td>
<td><p>The URI is too many link hops away from the seed.</p></td>
</tr>
<tr class="even">
<td><p>-4002</p></td>
<td><p>The URI is too many embed/transitive hops away from the last URI in scope.</p></td>
</tr>
<tr class="odd">
<td><p>-5000</p></td>
<td><p>The URI is out of scope upon reexamination.  This only happens if the scope changes during the crawl.</p></td>
</tr>
<tr class="even">
<td><p>-5001</p></td>
<td><p>Blocked from fetch by user setting.</p></td>
</tr>
<tr class="odd">
<td><p>-5002</p></td>
<td><p>Blocked by a custom processor, which could include the hash mapper (for multi-node crawling) if enabled.</p></td>
</tr>
<tr class="even">
<td><p>-5003</p></td>
<td><p>Blocked due to exceeding an established quota.</p></td>
</tr>
<tr class="odd">
<td><p>-5004</p></td>
<td><p>Blocked due to exceeding an established runtime</p></td>
</tr>
<tr class="even">
<td><p>-6000</p></td>
<td><p>Deleted from Frontier by user.</p></td>
</tr>
<tr class="odd">
<td><p>-7000</p></td>
<td><p>Processing thread was killed by the operator.  This could happen if a thread is an a non-responsive condition.</p></td>
</tr>
<tr class="even">
<td><p>-9998</p></td>
<td><p>Robots.txt rules precluded fetch.</p></td>
</tr>
</tbody>
</table>

**Note**

-   Codes and explanations are also available under the Help link in the
    Web UI.
-   Status codes are subject to change between Heritrix versions.  New
    codes may be added to address new issue areas.

Heritrix status codes are also documented in the [source
code](http://crawler.archive.org/xref/org/archive/crawler/datamodel/FetchStatusCodes.html#38)
(or in FishEye for
[H1](https://webarchive.jira.com/source/browse/HER/trunk/heritrix/src/java/org/archive/crawler/datamodel/FetchStatusCodes.java?hb=true)
and
[H3](https://webarchive.jira.com/source/browse/HER/trunk/heritrix3/modules/src/main/java/org/archive/modules/fetcher/FetchStatusCodes.java?hb=true))
and [in the
glossary](http://crawler.archive.org/articles/user_manual/glossary.html).

This page seems to be duplicated
[here](https://webarchive.jira.com/wiki/display/~hstern/Status+Codes)
and
[here](https://webarchive.jira.com/wiki/display/~kenji/Heritrix+Crawl+Status+Code)
and
[here](https://webarchive.jira.com/wiki/display/ARIH/Crawl+Status+Codes+%28for+Seed+Status+Report%29).
Perhaps these pages should be collapsed into one?
