# unexpected offsite content

# I asked Heritrix to crawl a specific site; the results include resources from other sites. Why?

If you use one of the default setups, Heritrix assumes you want related
resources required to render the source page/site – such as offsite
images, frames, javascript, and so on. Heritrix also by default errs on
the side of inclusiveness, so sometimes it goes a couple hops off a
target site when following links whose necessity is unclear.

When using a *DecidingScope* (or other *DecideRules* chain) as your
scope, eliminating or adjusting the `TransclusionDecideRule` controls
whether and how deep off-site Heritrix goes. `TooManyHopsDecideRule` can
be adjusted to control the number of outlink hops are followed. The
default (crawler-beans) settings are intended to be moderately
inclusive; following many outlinks and allowing the crawler to discover
and follow transcluded and speculative content. Transcluded content
includes that which is necessary to render a page. Speculative content
is content that appears to be discoverable by the crawler during its
configured discovery processes, i.e. anything that "looks" like a link.

As an alternate example, if you wanted to limit crawling strictly to
*http://www.example.com/* from default (crawler-beans) settings, then
specifying (reject) `TooManyHopsDecideRule` *maxHops = 0* and (accept)
`TransclusionDecideRule` *maxTransHops = 0* and *maxSpeculativeHops = 0*
would prevent the crawler from downloading (or discovering links from)
pages more than zero hops from *http://www.example.com/* - or, trivially
download a single page. You can expand your crawl by not rejecting
outlink hops (*maxHops &gt; 0*) and allowing more transclusion or
speculative discovery (*maxTansHops,maxSpeculativeHops &gt; 0*), and by
including additional helpful hosts in your list of seeds or SURT
prefixes. Examining the output of short, initial test crawls is helpful
in determining how to configure the crawler's scope for the desired
results.

Legacy scopes (SurtPrefixScope, DomainScope, HostScope, PageScope) have
a similar hops setting but are less configurable and efficient and no
longer recommended.
