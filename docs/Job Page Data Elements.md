# Job Page Data Elements

###### Job name

The name of the job and the number of times the job has been run.

###### Available checkpoints to recover

As of Heritrix 3.1, if a crawl has been checkpointed, a dropdown box is
displayed showing all the checkpoints that were executed.

###### Job Log

The job log contains a record of commands issued on the job page,
including command responses.

###### Job Status

This area of the job page displays the status of the job.

###### Totals

This area of the job page displays statistics that provide information
about the number of documents crawled and downloaded.

###### Alerts 

This area of the job page lists alerts that the crawl has generated. 
Alerts can be problems that abort the crawl or warnings, which do not
halt the crawl but may be detrimental to the crawl's outcome.

###### Rates

This area of the job page displays statistics that provide the rates at
which documents and bytes of data are being downloaded.  The number of
URIs successfully processed per second is shown.  For this statistic
both the rate of the latest sampling interval and the average rate (in
parenthesis) is shown.  The sampling interval is typically about 20
seconds and can be controlled by the `intervalSeconds` property of the
`StatisticsTracker` Spring bean.  The latest rate of progress can
fluctuate considerably, as the crawler workload varies and housekeeping
memory and file operations occur.  This is especially true if the
sampling interval has been set to a low value.  Also displayed, is the
rate of successful content collection in `KB/second` for the latest
sampling interval and (in parenthesis) the average since the crawl
began.

###### Load

This area of the job page displays statistics that provide load
information.  The number of active threads, compared to the total
available threads is shown.  Typically, if only a small number of
threads are active, it is because activating more threads would exceed
the configured politeness settings.  For example, if all remaining URIs
are on a single host, no more than one thread will be active, unless
parallel queues are enabled.  At times no threads will be active because
of pauses for politeness considerations.

###### Congestion Ratio

The congestion ratio is a rough estimate of how much initial capacity,
as a multiple of current capacity, would be necessary to crawl the
current workload at the maximum rate available given politeness
settings.  This value is calculated by comparing the number of internal
queues that are progressing against those that are waiting for a thread
to become available.

###### Deepest Queue

The deepest queue statistic is the longest chain of URIs that must be
processed sequentially.  This statistic is a better indicator of the
work remaining than the total number of URIs pending.  For example, 1000
URIs in 1000 queues can be completed quickly but 1000 URIs in a single
queue will take much longer to complete.  The average depth is the
average depth of the last URI in every active sequential queue.

###### Elapsed

This area of the job page displays the elapsed time in milliseconds that
a job has been running excluding time in the "paused" state.

###### Threads

This area of the job page displays the number of threads being used. 
The "Threads" text is clickable.  Upon clicking, a detailed report on
each thread will be displayed.

###### Frontier

This area of the job page displays Frontier statistics such as the
number of queued URIs.  The "Frontier" text is clickable.  Upon clicking
a detailed frontier report will be displayed.

###### Memory

This area of the job page displays the amount of memory allocated to the
Java heap, the amount of memory in use, and the maximum size of the Java
heap.

###### Crawl Log

This area of the job page displays the output of the crawl log.  The
crawl log contains detailed information on a running crawl, such as the
URIs that have been fetched.

###### Advanced

This area of the job page provides access to advanced features that can
be used to control a job.

###### Configuration-referenced Paths

This area of the job page displays paths that are relevant to job
configuration and logging.  For example, the path to the `crawl.log`
file is displayed.
