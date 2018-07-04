# Action Directory

Each job directory contains an action directory. By placing files in the
action directory you can trigger actions in a running crawl job, such as
the addition of new URIs to the crawl.

At a regular interval (by default less than a minute), the crawl will
notice any new files in this directory, and take action based on their
filename suffix and their contents. When the action is done, the file
will be moved to the nearby 'done' directory. (For this reason, files
should be composed outside the action directory, then moved there as an
atomic whole. Otherwise, a file may be processed-and-moved while still
being composed.)

The following file suffixes are supported:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>File Suffix</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><code>.seeds</code></p></td>
<td><p>A <code>.seeds</code> file should contain seeds that the Heritrix operator wants to include in the crawl. Placing a <code>.seeds</code> file in the action directory will add the seeds to the running crawl. The same directives as may be used in seeds-lists during initial crawl configuration may be used here.<br />
If seeds introduced into the crawl this way were already in the frontier (perhaps already a seed) this method does not force them.</p></td>
</tr>
<tr class="even">
<td><p><code>.recover</code></p></td>
<td><p>A <code>.recover</code> file will be treated as a traditional recovery journal. (The recovery journal can approximately reproduce the state of a crawl's queues and already-included set, by repeating all URI-completion and URI-discovery events. A recovery journal reproduces less state than a proper checkpoint.) In a first pass, all lines beginning with <code>Fs</code> in the recovery journal will be considered included, so that they can not be enqueued again. Then in a second pass, lines starting with <code>F+</code> will be re-enqueued for crawling (if not precluded by the first pass).</p></td>
</tr>
<tr class="odd">
<td><p><code>.include</code></p></td>
<td><p>A <code>.include</code> file will be treated as a recovery journal, but all URIs no matter what their line-prefix will be marked as already included, preventing them from being re-enqueued from that point on. (Already-enqueued URIs will still be eligible for crawling when they come up.) Using a <code>.include</code> file is a way to suppress the re-crawling of URIs.</p></td>
</tr>
<tr class="even">
<td><p><code>.schedule</code></p></td>
<td><p>A <code>.schedule</code> file will be treated as a recovery journal, but all URIs no matter what their line-prefix will be offered for enqueueing. (However, if they are recognized as already-included, they will not be enqueued.) Using a <code>.schedule</code> file is a way to include URIs in a running crawl by inserting them into the Heritrix crawling queues.</p></td>
</tr>
<tr class="odd">
<td><p><code>.force</code></p></td>
<td><p>A <code>.force</code> file will be treated as a recovery journal with all the URIs marked for force scheduling.  Using a <code>.force</code> file is a way to guarantee that already-included URIs will be re-enqueued and (and thus eventually re-crawled).</p></td>
</tr>
</tbody>
</table>

Any of these files may be gzipped. Any of the files in recovery journal
format (`.recover`, `.include`, `.schedule`, `.force`) may have a `.s`
inserted prior to the functional suffix (for example,
`frontier.s.recover.gz`), which will cause the URIs to be scope-tested
before any other insertion occurs.

For example you could place the following file in the action directory
to schedule a URL:

**example.schedule**

``` bash
F+ http://example.com
```

 

In order to use the action directory, the `ActionDirectory` bean must be
configured in the `crawler-beans.cxml` file as illustrated below.

``` xml
<bean id="actionDirectory" class="org.archive.crawler.framework.ActionDirectory">
<property name="actionDir" value="action" />
<property name="initialDelaySeconds" value="10" />
<property name="delaySeconds" value="30" />
</bean>
```

The class
[org.archive.crawler.frontier.FrontierJournal](https://webarchive.jira.com/source/browse/HER/trunk/heritrix3/engine/src/main/java/org/archive/crawler/frontier/FrontierJournal.java?hb=true)
contains the constants that are recognized as possible directives in a
recovery journal.

Note that the recovery journal format's 'F+' lines may include a
'hops-path' and 'via URI', which are preserved when a URI is enqueued
via the above mechanisms, but that this may not be a complete
representation of all URI state from its discovery in a normal crawl.
