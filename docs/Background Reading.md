# Background Reading

### Must reads

-   Haydon, A; Najork, M. [Mercator: A Scalable, Extensible Web
    Crawler](http://www.research.compaq.com/SRC/mercator/papers/www/paper.html)
    (wayback
    (http://web.archive.org/web/\*/http://research.compaq.com/SRC/mercator/papers/www/paper.html)),
    1999
-   Haydon, A; Najork, M. [High-performance web
    crawling](http://gatekeeper.research.compaq.com/pub/DEC/SRC/research-reports/abstracts/src-rr-173.html),
    2001
-   Kimpton, Stata, Mohr. [Internet Archive Crawler Requirements
    Analysis](Internet%20Archive%20Crawler%20Requirements%20Analysis)
    for library consortium, 2003
-   Lee, H; Leonard, D; Wang, X; Loguinov, D. [IRLbot: Scaling to 6
    Billion Pages and
    Beyond](http://irl.cs.tamu.edu/people/hsin-tsang/papers/www2008.pdf)
    (new from WWW2008)

### Nice to reads

-   Najork, M.; Wiener, J. [Breadth-First Search Crawling Yields
    High-Quality Pages](http://www10.org/cdrom/papers/208/), 2001
-   Cho, J.; Garcia-Molina, H.; Page, L. [Efficient Crawling Through URL
    Ordering](http://dbpubs.stanford.edu:8090/pub/1998-51), 1998
-   Abiteboul, S.; Preda, M.; Cobena, G. [Computing web page importance
    without storing the graph of the web (extended
    abstract)](http://groups.yahoo.com/group/archive-crawler/files/xyleme-crawlorder.pdf),
    2001
-   Olsten, C.; Pandey, S. [Recrawl Scheduling Based on Information
    Longevity](http://www.cs.cmu.edu/~spandey/www08.pdf) (new from
    WWW2008)

### Information on Java with respect to Heritrix/crawling

-   Haydon, A; Najork, M. [Performance Limitations of the Java Core
    Libraries](http://www.research.compaq.com/SRC/mercator/papers/Java99/final.html)
    (may not reflect latest Java issues, Heritrix uses a high
    performance DNS package)

Find these (also may be outdated with respect to current Java and our
implementation choices) at the [archive-crawler Yahoo Group files
page](http://tech.groups.yahoo.com/group/archive-crawler/files/):

-   G. B. Reddy Study of synch vs. asynch IO in Java
-   G. B. Reddy Study of multi-threaded DNS performance in Java

### Others

-   Archive-crawler group
    [files](http://tech.groups.yahoo.com/group/archive-crawler/files/)
-   Cho, J.; Garcia-Molina, H. [The Evolution of the Web and
    Implications for an Incremental
    Crawler](http://scholar.google.com/scholar?hl=en&lr=&safe=off&client=firefox-a&q=author%3A%22Cho%22+intitle%3A%22The+evolution+of+the+web+and+implications+for+an+incremental+crawler%22+&btnG=Search),
    Conf. on Very Large Data Bases, 2000
-   [Focused Crawling The Quest for Topic-specific
    Portals](http://www.cs.berkeley.edu/~soumen/focus/)
-   [Focused Crawling: : A New Approach to Topic-Specific Web Resource
    Discovery](http://www8.org/w8-papers/5a-search-query/crawling/),
    1999, WWW8
-   [Intelligent Crawling on the World Wide Web with Arbitrary
    Predicates](http://www10.org/cdrom/papers/110/), 2001, WWW10
-   [Web Crawling High-Quality Metadata using RDF and Dublin
    Core](http://www2002.org/CDROM/alternate/747/), 2002, WWW11
-   Stanford [WebBase
    Project](http://www-diglib.stanford.edu/~testbed/doc2/WebBase/)
-   [An Introduction to
    Heritrix](http://webteam.archive.org/confluence/download/attachments/5441/Mohr-et-al-2004.pdf) -
    Mohr et al, 4th International Web Archiving Workshop 2004

### Relevant specifications

-   [RFC 2616: Hypertext Transfer Protocol -
    HTTP/1.1](http://www.ietf.org/rfc/rfc2616.txt)
    -   [Clarifying the fundamentals of
        HTTP](http://www2002.org/CDROM/refereed/444/) By Jeffery Mogul,
        an author of RFC-2616.
-   [RFC 3986: Uniform Resource Identifiers (URI): Generic
    Syntax](http://www.rfc.net/rfc3986.html).
-   [HTML 4.01 specification](http://www.w3.org/TR/html401/) (from W3C).
-   Although robots.txt is important for crawling, it's never been
    officially ratified as an RFC. The defacto minimal spec live at
    [robotstxt.org](http://robotstxt.org). Search engines have made a
    number of ad hoc extensions; Google recently shared some info about
    [how GoogleBot implements the Robots Exclusion
    Protocol](http://googlewebmastercentral.blogspot.com/2008/06/improving-on-robots-exclusion-protocol.html).
-   [RFC 1034: Domain Names - Concepts and
    Facilities](ftp://ftp.rfc-editor.org/in-notes/rfc1034.txt)
-   [RFC 1035: Domain Names - Implementation and
    Specification](ftp://ftp.rfc-editor.org/in-notes/rfc1035.txt)

### Attachments

[Download
All](/wiki/download/all_attachments?pageId=5441 "Download all the latest versions of attachments on this page as single zip file."){.download-all-link}

## Attachments:

![](images/icons/bullet_blue.gif){width="8" height="8"}
[crawler-requirements-2003-03.htm](attachments/5441/90997065.htm)
(text/html)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[Mohr-et-al-2004.pdf](attachments/5441/560.pdf) (application/pdf)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[1998-Cho-efficient.pdf](attachments/5441/786450.pdf)
(application/pdf)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[1999-Heydon-javalimits.pdf](attachments/5441/786451.pdf)
(application/pdf)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[1999-Hirai-webbase.pdf](attachments/5441/786452.pdf)
(application/pdf)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[1999-Mercator.pdf](attachments/5441/786453.pdf) (application/pdf)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[2000-Broder-webgraph.pdf](attachments/5441/786454.pdf)
(application/pdf)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[2000-Cho-incremental.pdf](attachments/5441/786455.pdf)
(application/pdf)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[2001-Abiteboul-crawlorder.pdf](attachments/5441/786456.pdf)
(application/pdf)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[2001-Arasu-search.pdf](attachments/5441/786457.pdf) (application/pdf)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[2001-Najork-breadthfirst.pdf](attachments/5441/786458.pdf)
(application/pdf)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[2001-Najork-highperf.pdf](attachments/5441/786459.pdf)
(application/pdf)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[2002-Guillaume-webgraph.pdf](attachments/5441/786460.pdf)
(application/pdf)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[2008-IRLBot.pdf](attachments/5441/786461.pdf) (application/pdf)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[2008-Olston-recrawl.pdf](attachments/5441/786462.pdf)
(application/pdf)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[2002-Shkapenyuk-polybot.pdf](attachments/5441/786463.pdf)
(application/pdf)  
