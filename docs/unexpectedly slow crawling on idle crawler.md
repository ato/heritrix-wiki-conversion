# unexpectedly slow crawling on idle crawler

# Why is crawling slower than expected with a not-very-busy crawling machine?

Heritrix is designed to be a polite crawler. Its default configuration
results in serialized (one request at a time per server) and
intermittent (multi-second pauses between requests) politeness with
respect to every target hostname.

It is important for crawl operators to keep in mind that speeding the
crawler by reducing politeness or other tactics may trigger problems for
target sites, anger webmasters, or result in more active countermeasures
(like getting your IP blocked) if you're not crawling with explicit
permission.

Equally important is that you give meaningful and correct
`operatorContactUrl` and `userAgentTemplate` metadata.

With such [Responsible Crawling](Responsible%20Crawling) principles in
mind, if you are confident you have permission to crawl a site more
intensively than the Heritrix defaults, you can decrease the default
delay settings (`delayFactor`, `minDelayMs`, `maxDelayMS`) to request
pages from the same host more frequently.

If the sites still in rotation are spending many minutes between
retries, then they are in the 'slow retry' cycle which is triggered by a
failure to get any response at all from the target server. By default,
such retries are spaced at 900 seconds (15 minutes), and the total
number of such retries is 30. (See `retryDelay` and `maxRetries`.) Thus,
it will take 30x15m == over 7 hours to definitively give up on a URI,
logging it as a failure, and moving on to the next URI on the same host.

The retryDelay may be increased – but should usually be a matter of
minutes rather than seconds, because server unresponsiveness, due to
server or network issues, may be due to issues that take hours to
resolve. The maxRetries may be reduced, though normal crawler processes
require this to be at least 3-5, and smaller numbers let URIs fail
during temporary outage situations. Of course, if many URIs are queued,
and the site never returns to responsiveness, this slow retry cycle can
take days/months to give up on all URIs; in such a case it is the
operator's choice of when to conclude a crawl that is decisive.

Note that if your crawler is already 'busy' – with all threads active,
and the machine's CPU, disk IO, or network bandwidth already maxed out –
then tinkering with delays will not result in faster crawling. Indeed,
you may wish to **increase** delays, so that no single sites are
inconvenienced by your crawling when you are just as happy to spread the
crawler's attention over a larger number of sites.

To speed a crawler that is not limited by politeness considerations, see
[making a busy crawl go
faster](making%20a%20busy%20crawl%20go%20faster).
