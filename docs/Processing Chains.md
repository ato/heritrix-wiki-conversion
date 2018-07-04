# Processing Chains

Much of the crawler's work is specified by the sequential application of
swappable Processor modules.  These Processors are collected into three
"chains:"

1.  CandidateChain - This chain is applied to URIs being considered for
    inclusion in the crawl, before a URI is enqueued for collection.
2.  FetchChain - This chain is applied to URIs during collection.
3.  DispositionChain - This chain is applied after a URI is fetched,
    analyzed, and link-extracted.

Each URI taken off the Frontier queue runs through the processing
chains.  URIs are always processed in the order shown in the diagram
below, unless a particular processor throws a fatal error or decides to
stop the processing of the current URI.  Each processing chain is made
up of zero or more individual processors.  For example, the FetchChain
might comprise the `extractorCss` and `extractorJs` processors.  Within
a processing step, the order in which the processors are run is the
order in which they are listed in the `crawler-beans.cxml` file.
![](attachments/5735694/5865609.png){.image-center}

## Attachments:

![](images/icons/bullet_blue.gif){width="8" height="8"}
[HeritrixProcessorChains.png](attachments/5735694/5865609.png)
(image/png)  
