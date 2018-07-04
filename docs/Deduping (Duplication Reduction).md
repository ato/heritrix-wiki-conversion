# Deduping (Duplication Reduction)

Starting in release *1.12.0*, a number of Processors can cooperate to
carry forward URI content history between crawls (see
[org.archive.crawler.processor.recrawl](http://crawler.archive.org/apidocs/org/archive/crawler/processor/recrawl/package-summary.html)
package JavaDocs). This reduces the amount of duplicate material
downloaded or stored in later crawls.

# H1 dedupe configuration

Heritrix *1.x* does not support running the same crawl more than once,
so one crawl will need to be configured for *storing* duplication
reduction data, and another crawl will need to be configured for
*loading* duplication reduction data. e.g. excerpt from testing for
[HER-1627](https://webarchive.jira.com/browse/HER-1627):

## configure persist STORE crawl

-   add *FetchHistory* and *PersistLog* processors *after* `FetchHttp`  
    `org.archive.crawler.processor.recrawl.FetchHistoryProcessor`  
    `org.archive.crawler.processor.recrawl.PersistLogProcessor`

## configure persist LOAD crawl

-   *after* PreconditionEnforcer, *before* FetchDNS  
    `org.archive.crawler.processor.recrawl.PersistLoadProcessor`
-   *after* FetchHTTP  
    `org.archive.crawler.processor.recrawl.FetchHistoryProcessor`
-   preload-source:  
    `${HERITRIX_HOME`}/jobs/`${JOB`}/logs/persistlog.txtser.gz

# H3 dedupe configuration

Heritrix *3.x* allows for running the same crawl repeatedly, but
requires a different configuration for the crawl run which *stores*
deduplication data, and the crawl run which *loads* deduplication data
as described in [Duplication Reduction
Processors](Duplication%20Reduction%20Processors). The same model is
followed for H1, except using the *Spring*-world crawler beans CXML
(`crawler-beans.cxml`) for configurating.
