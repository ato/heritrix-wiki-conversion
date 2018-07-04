# Heritrix Output

In addition to logs, the following files are generated.  Some of the
information in them is also available in the WUI.

-   [surts.dump](#HeritrixOutput-surts.dump)
-   [negative-surts.dump](#HeritrixOutput-negative-surts.dump)
-   [heritrix\_out.log](#HeritrixOutput-heritrix_out.log)
-   [crawl-report.txt](#HeritrixOutput-crawl-report.txt)
-   [hosts-report.txt](#HeritrixOutput-hosts-report.txt)
-   [mimetype-report.txt](#HeritrixOutput-mimetype-report.txt)
-   [processors-report.txt](#HeritrixOutput-processors-report.txt)
-   [responsecode-report.txt](#HeritrixOutput-responsecode-report.txt)
-   [seeds-report.txt](#HeritrixOutput-seeds-report.txt)
-   [frontier-summary-report.txt](#HeritrixOutput-frontier-summary-report.txt)
-   [source-report.txt](#HeritrixOutput-source-report.txt)
-   [threads-report.txt](#HeritrixOutput-threads-report.txt)
-   [WARC files](#HeritrixOutput-WARCfiles)

###### surts.dump

This file contains the
﻿[SURTs](https://webarchive.jira.com/wiki/spaces/ARIH/pages/1712/SURT+Rules)
form of the seed URIs.

###### negative-surts.dump

This file contains the SURT form of URIs that are to be excluded from
the crawl.

###### heritrix\_out.log

This file captures output to standard out and standard error.  Most of
the output consists of low-level exceptions and logging information.

This file is created in the same directory as the Heritrix jar file.  It
is not associated with any one job, but contains output from all jobs
run by the crawler.

Below is sample output from this file:

``` bash
Darwin internet-archives-macbook-pro.local 10.0.0 Darwin Kernel Version 10.0.0: Fri Jul 31 22:47:34 PDT 2009; root:xnu-1456.1.25~1/RELEASE_I386 i386
java version "1.6.0_15"
Java(TM) SE Runtime Environment (build 1.6.0_15-b03-219)
Java HotSpot(TM) 64-Bit Server VM (build 14.1-b02-90, mixed mode)
JAVA_OPTS= -Xmx256m
core file size          (blocks, -c) 0
data seg size           (kbytes, -d) unlimited
file size               (blocks, -f) unlimited
max locked memory       (kbytes, -l) unlimited
max memory size         (kbytes, -m) unlimited
open files                      (-n) 256
pipe size            (512 bytes, -p) 1
stack size              (kbytes, -s) 8192
cpu time               (seconds, -t) unlimited
max user processes              (-u) 266
virtual memory          (kbytes, -v) unlimited
```

###### crawl-report.txt

This file contains useful metrics about completed jobs.  The report is
created by the `StatisticsTracker` bean.  This file is written at the
end of the crawl.

Below is sample output from this file:

``` bash
Crawl Name: basic
Crawl Status: Finished
Duration Time: 1h33m38s651ms
Total Seeds Crawled: 1
Total Seeds not Crawled: 0
Total Hosts Crawled: 1
Total URIs Processed: 1337
URIs Crawled successfully: 1337
URIs Failed to Crawl: 0
URIs Disregarded: 0
Processed docs/sec: 0.24
Bandwidth in Kbytes/sec: 4
Total Raw Data Size in Bytes: 23865329 (23 MB)
Novel Bytes: 23877375 (23 MB)
```

###### hosts-report.txt

This file contains an overview of the hosts that were crawled.  It also
displays the number of documents crawled and the bytes downloaded per
host.

This file is created by the `StatisticsTracker` bean and is written at
the end of the crawl.

Below is sample output from this file:

``` bash
1337 23877316 www.smokebox.net 0 0
1 59 dns: 0 0
0 0 dns: 0 0
```

###### mimetype-report.txt

This file contains a report displaying the number of documents
downloaded per mime type.  Also, the amount of data downloaded per mime
type is displayed.

This file is created by the `StatisticsTracker` bean and is written at
the end of the crawl.

Below is sample output from this report:

``` bash
624 13248443 image/jpeg
450 8385573 text/html
261 2160104 image/gif
1 74708 application/x-javascript
1 59 text/dns
1 8488 text/plain
```

###### processors-report.txt

This file contains the processors report.  The processors report shows
the activity of each Heritrix processor.  For more information on
processors see [Processing Chains](Processing%20Chains).  It is written
at the end of the crawl.

Below is sample output from this report:

``` bash
CandidateChain - Processors report - 200910300032
  Number of Processors: 2

Processor: org.archive.crawler.prefetch.CandidateScoper

Processor: org.archive.crawler.prefetch.FrontierPreparer


FetchChain - Processors report - 200910300032
  Number of Processors: 9

Processor: org.archive.crawler.prefetch.Preselector

Processor: org.archive.crawler.prefetch.PreconditionEnforcer

Processor: org.archive.modules.fetcher.FetchDNS

Processor: org.archive.modules.fetcher.FetchHTTP
  Function:          Fetch HTTP URIs
  CrawlURIs handled: 1337
  Recovery retries:   0

Processor: org.archive.modules.extractor.ExtractorHTTP
  Function:          Extracts URIs from HTTP response headers
  CrawlURIs handled: 1337  Links extracted:   0

Processor: org.archive.modules.extractor.ExtractorHTML
  Function:          Link extraction on HTML documents
  CrawlURIs handled: 449
  Links extracted:   6894

Processor: org.archive.modules.extractor.ExtractorCSS
  Function:          Link extraction on Cascading Style Sheets (.css)
  ExtractorURIs handled: 0
  Links extracted:   0

Processor: org.archive.modules.extractor.ExtractorJS
  Function:          Link extraction on JavaScript code
  CrawlURIs handled: 1
  Links extracted:   19

Processor: org.archive.modules.extractor.ExtractorSWF
  Function:          Link extraction on Shockwave Flash documents (.swf)
  CrawlURIs handled: 0
  Links extracted:   0


DispositionChain - Processors report - 200910300032
  Number of Processors: 3

Processor: org.archive.modules.writer.WARCWriterProcessor

Processor: org.archive.crawler.postprocessor.CandidatesProcessor

Processor: org.archive.crawler.postprocessor.DispositionProcessor
```

###### responsecode-report.txt

This file contains a report displaying the number of documents
downloaded per status code.  It covers successful codes only.  For
failure codes see the `crawl.log` file.

This file is created by the `StatisticsTracker` bean and is written at
the end of the crawl.

Below is sample output from this report:

``` bash
[#urls] [rescode]
1306 200
31 404
1 1
```

###### seeds-report.txt

This file contains the crawling status of each seed.

This file is created by the `StatisticsTracker` bean and is written at
the end of the crawl.

Below is sample output from this report:

``` bash
[code] [status] [seed] [redirect]
200 CRAWLED http://www.smokebox.net
```

###### frontier-summary-report.txt

This report contains a breakdown of frontier activity on a per-thread
basis.  For each thread running, the status of the frontier queue can be
examined.

Below is sample output from this report.

``` bash
-----===== RETIRED QUEUES =====-----
internet-archives-macbook-pro:reports hstern$
internet-archives-macbook-pro:reports hstern$ cat frontier-summary-report.txt
Frontier report - 201001142216
 Job being crawled: basic

 -----===== STATS =====-----
 Discovered:    3
 Queued:        0
 Finished:      3
  Successfully: 2
  Failed:       0
  Disregarded:  1

 -----===== QUEUES =====-----
 Already included size:     3
               pending:     0

 All class queues map size: 1
             Active queues: 1
                    In-process: 0
                         Ready: 1
                       Snoozed: 0
           Inactive queues: 0 (p1: 0)
            Retired queues: 0
          Exhausted queues: 0

 -----===== MANAGER THREAD =====-----
Java Thread State: RUNNABLE
Blocked/Waiting On: NONE
    java.lang.Thread.getStackTrace(Thread.java:1460)
    org.archive.crawler.framework.ToeThread.reportThread(ToeThread.java:476)
    org.archive.crawler.frontier.WorkQueueFrontier.standardReportTo(WorkQueueFrontier.java:1424)
    org.archive.crawler.frontier.WorkQueueFrontier.reportTo(WorkQueueFrontier.java:1257)
    org.archive.crawler.reporting.FrontierSummaryReport.write(FrontierSummaryReport.java:41)
    org.archive.crawler.reporting.StatisticsTracker.writeReportFile(StatisticsTracker.java:973)
    org.archive.crawler.reporting.StatisticsTracker.dumpReports(StatisticsTracker.java:1000)
    org.archive.crawler.reporting.StatisticsTracker.crawlEnded(StatisticsTracker.java:572)
    org.archive.crawler.reporting.StatisticsTracker.onApplicationEvent(StatisticsTracker.java:1044)
    org.springframework.context.event.SimpleApplicationEventMulticaster$1.run(SimpleApplicationEventMulticaster.java:78)
    org.springframework.core.task.SyncTaskExecutor.execute(SyncTaskExecutor.java:49)
    org.springframework.context.event.SimpleApplicationEventMulticaster.multicastEvent(SimpleApplicationEventMulticaster.java:76)
    org.springframework.context.support.AbstractApplicationContext.publishEvent(AbstractApplicationContext.java:274)
    org.archive.crawler.framework.CrawlController.sendCrawlStateChangeEvent(CrawlController.java:323)
    org.archive.crawler.framework.CrawlController.completeStop(CrawlController.java:375)
    org.archive.crawler.framework.CrawlController.noteFrontierState(CrawlController.java:639)
    org.archive.crawler.frontier.AbstractFrontier.reachedState(AbstractFrontier.java:484)
    org.archive.crawler.frontier.AbstractFrontier.managementTasks(AbstractFrontier.java:412)
    org.archive.crawler.frontier.AbstractFrontier$2.run(AbstractFrontier.java:328)

 -----===== LONGEST QUEUE =====-----
Queue com,fizzandpop,www, (p1)
  0 items
    last enqueued: http://www.fizzandpop.com/
      last peeked: http://www.fizzandpop.com/
   total expended: 2 (total budget: -1)
   active balance: 2998
   last(avg) cost: 1(1)
   totalScheduled fetchSuccesses fetchFailures fetchDisregards fetchResponses robotsDenials successBytes totalBytes fetchNonResponses
   3 2 0 1 2 1 383 383 2
   SimplePrecedenceProvider
   1


 -----===== IN-PROCESS QUEUES =====-----

 -----===== READY QUEUES =====-----
READY#0:
Queue com,fizzandpop,www, (p1)
  0 items
    last enqueued: http://www.fizzandpop.com/
      last peeked: http://www.fizzandpop.com/
   total expended: 2 (total budget: -1)
   active balance: 2998
   last(avg) cost: 1(1)
   totalScheduled fetchSuccesses fetchFailures fetchDisregards fetchResponses robotsDenials successBytes totalBytes fetchNonResponses
   3 2 0 1 2 1 383 383 2
   SimplePrecedenceProvider
   1


 -----===== SNOOZED QUEUES =====-----

 -----===== INACTIVE QUEUES =====-----

 -----===== RETIRED QUEUES =====-----
```

###### source-report.txt

This report contains a line item for each host, which includes the seed
from which the host was reached.

Below is a sample of this report:

``` bash
[source] [host] [#urls]
http://www.fizzandpop.com/ dns: 1
http://www.fizzandpop.com/ www.fizzandpop.com 1
```

**Note**

-   The `sourceTagSeeds` property of the `TextSeedModule` bean must be
    set to true for this report to be generated.
    ``` xml
    <bean id="seeds" class="org.archive.modules.seeds.TextSeedModule">

    <property name="textSource">

    <bean class="org.archive.spring.ConfigString">

    <property name="value">
    <value>
    # [see override above]
            </value>
    </property>
    </bean>
    </property>
    <property name="sourceTagSeeds" value="true"/>
    </bean>
    ```

###### threads-report.txt

This report contains the list of threads that were active at the end of
the crawl.  Detailed information about each thread is also available.

###### WARC files

Assuming you are using the WARC writer that comes with Heritrix, a
number of WARC files will be generated containing crawled content.

You can specify the storage location of WARC files by setting the
`directory` value of the `WARCWriterProcessor` bean.

WARC files are named using the following convention:

\[prefix\]\[12 digit timestamp\]\[series padded to 5 digits\]\[crawler
hostname\].warc.gz

The `WARCWriterProcessor` contains the `prefix` setting.  By default it
is `IAH`.

WARC files with an `.open` suffix are in the process of being written to
by Heritrix.  There may be multiple open WARCs at any given time.

WARC files with an `.invalid` suffix indicate problems writing to the
file.  This may be the result of a bad disk or a fully utilized disk. 
On an I/O problem, Heritrix closes the problematic WARC file and gives
it an `.invalid` suffix.  These files should be checked for coherence.

As of Heritrix 3.1, the "LowDiskPauseProcessor" bean has been replaced
by the "DiskSpaceMonitor" bean.  When writing WARC files, the
DiskSpaceMonitor checks the available space on the configured paths and
if free space has dropped below the defined threshold the crawl is
paused.  In the example below, the path `/warcs` is monitored.  If the
level of free space drops below 500MB the crawls writing to the `/warcs`
directory are paused.

``` xml
<bean id="diskSpaceMonitor" class="org.archive.crawler.monitor.DiskSpaceMonitor"> <property name="pauseThresholdMiB" value="500" /> <property name="monitorConfigPaths" value="true" /> <property name="monitorPaths"> <list> <value>/warcs</value> </list> </property> </bean>
```

As of Heritrix 3.1, the naming convention for WARC files has changed.
 Instead of specifying the formula for ARC/WARC naming in code and using
a supplied 'prefix' and 'suffix', a template with variable interpolation
may be used.  The configured 'prefix' remains an available variable, as
well as other useful local machine, crawl, and writer properties. The
default template is:

``` bash
${prefix}-${timestamp17}-${serialno}-${heritrix.pid}~${heritrix.hostname}~${heritrix.port}
```

The template adds the local process ID and the 17 digit timestamp.  The
timestamp is provided by a service that ensures each timestamp is at
least 1 millisecond after previous millisecond values.  The new default
convention also minimizes the likelihood of ARC/WARC name collisions,
even when many crawls are launched or running simultaneously on the same
local machine, using the same file name prefix.  Although the generated
names are long, they are very likley to be unique under normal
conditions.  It is not recommended that the template by changed unless
the alternate naming system is certain to also generate unique names.
 This is important because down stream tools that index ARCs/WARCs often
assume file name uniqueness and can benefit from their unique
generation.
