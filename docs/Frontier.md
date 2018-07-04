# Frontier

The Frontier is a Spring bean that maintains the internal state of the
crawl.  The state of the crawl contains information such as previously
crawled or discovered URIs, as well as other information relevant to the
crawl's status. 

There is only one Frontier per crawl job.

In Heritrix 3.0 and 3.1 there is only one kind of Frontier, the
BdbFrontier.  Other Frontiers that were included in Heritrix 1.x are no
longer supported.
