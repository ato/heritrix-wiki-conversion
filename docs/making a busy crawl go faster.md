# making a busy crawl go faster

# My crawl is busy, but I want to try to make it go even faster. How can I do that?

The following are some indicators that a crawl is 'busy':

-   all threads are active
-   there are many independent queues the crawler may consult for new
    URIs – specifically, some are in the 'inactive queue' state and the
    'congestion ratio' is greater-than 1, perhaps much greater
-   CPU utilization as indicated by a tool like 'top' is high

For busy crawls, politeness setting are not the issue – raw system
capacity is.

For example, if all threads are busy and there are plenty of other sites
ready to crawl – as will be common in a large-domain crawl, until/unless
it gets down to a last few large sites – then reducing politeness delays
won't speed things up at all. It's not the limiting factor;
threads/CPU/IO are.

Some tweaks that can help a busy crawl go faster are:

-   use more RAM, either as assigned to JVM (by -Xmx launch parameter)
    or as OS disk cache (automatically used by linux if available)
-   use separate disks for the frontier datastore and w/arc writing
    (`storePaths`, `BdbModule.dir`) to reduce I/O contention
-   experiment with different toe-thread counts to find what value
    optimizes throughput; the best number for your system depends on
    RAM, IO contention, and CPU cores/speed
