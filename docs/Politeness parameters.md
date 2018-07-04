# Politeness parameters

Politeness is chiefly achieved by the crawler's "Frontier"
implementation, which only schedules URIs for processing at a rate which
should not unduly burden the source servers.

(The information here applies to the current
org.archive.crawler.basic.Frontier implementation.)

The most basic aspect of robot politeness is to only open a single
connection to a server at a time. The current Heritrix frontier always
follows this rule. (Eventually, when it is clear a server has the
capacity, perhaps provided by many independent server machines, to
service multiple simultaneous robot requests, we may relax this
behavior.)

A number of other settings can be specified to adjust relatively how
nice Heritrix is to visited servers. There are three key inputs to
Heritrix' decision about when it is alright to visit a server again:

-   When the last request against that server was issued.
-   How long that last request took to complete.
-   How much of an interval (time since last request issued) or delay
    (time since last request finished) the operator specified.

The operator-specified timing constrains may be specified as any
combination of:

-   a multiple of the last completion (the "delay-factor" parameter);
-   a minimum interval from the last request issued (the
    "min-interval-ms" parameter);
-   a minimum delay from the last request completion (the "min-delay-ms"
    parameter);
-   a maximum delay from the last request completion (the "max-delay-ms"
    parameter).

Consider an intended behavior of never issuing more than one request
against a server every 2 seconds; never waiting more than 30 seconds to
revisit a server; but whenever possible within those constraints, giving
a server at least an equal amount of time "off" for every moment
connected. This could be achieved with settings of:

``` bash
min-interval-ms=2000
max-delay-ms=30000
delay-factor=1
min-delay-ms=0 (irrelevant in this case because of the 'interval')
```
