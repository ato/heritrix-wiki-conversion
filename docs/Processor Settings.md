# Processor Settings

Processors have settings that effect crawls.  Each processor can be
enabled or disabled.  If disabled, the Processor will not be applied to
any URI.  The following processors have default settings configured by
Heritrix.

###### preparer

-   **preferenceDepthHops** - Number of hops (of any sort) from a seed
    up to which a URI has higher priority scheduling than any remaining
    seed. For example, if set to one, items one hop (link, embed,
    redirect, etc.) away from a seed will be scheduled with HIGH
    priority. If set to -1, no preferencing will occur, and a
    breadth-first search with seeds processed before discovered links
    will proceed. If set to zero, a purely depth-first search will
    proceed, with all discovered links processed before remaining seeds.
    Seed redirects are treated as one hop from a seed.
-   **preferenceEmbedHops** - Number of embed hops (ERX) to bump to
    front of host queue.
-   **canonicalizationPolicy** - Ordered list of URI canonicalization
    rules.  Rules are applied in the order listed from top to bottom.
-   **queueAssignmentPolicy** -  Defines how to assign URIs to queues.
    Can assign by host, by ip, by SURT-ordered authority, by
    SURT-ordered authority truncated to a topmost-assignable domain, and
    into one of a fixed set of buckets (1k).
-   **uriPrecedencePolicy** - Sets an integer precedence value on
    individual URIs when they are first submitted to a frontier for
    scheduling.  A URI's precedence directly affects which URI queue it
    is placed in, but does not affect a queue's precedence relative to
    other queues unless a queue-precedence-policy that consults URI
    precedence values is chosen.
-   **costAssignmentPolicy** - Calculates an integer 'cost' value for
    the given CrawlURI.

###### preselector

-   **recheckScope** - Recheck if URI is in scope. This is meaningful if
    the scope is altered during a crawl.  When URIs are added to queues
    they are checked against the scope.  Setting this value to true
    forces the URI to be checked against the scope when it comes out of
    the queue, possibly after the scope is altered.
-   **blockAll**- Block all URIs from being processed. This is most
    likely to be used in overrides to easily reject certain hosts from
    being processed.
-   **blockByRegex** - Block all URIs matching the regular expression
    from being processed.
-   **allowByRegex** - Allow only URIs matching the regular expression
    to be processed.

###### preconditions

-   **ipValidityDurationSeconds** - The minimum interval for which a
    dns-record will be considered valid (in seconds). If the record's
    DNS TTL is larger, that will be used instead.
-   **robotsValidityDurationSeconds**- The time in seconds that fetched
    robots.txt information is considered valid. If the value is set to
    '0', then the `robots.txt` information will never expire.
-   **calculateRobotsOnly** - Whether to calculate the robot's status of
    a URI, without actually applying any exclusions found. If true,
    excluded URIs will only be annotated in the `crawl.log`, but still
    fetched.

###### fetchDns

-   **acceptNonDnsResolves** - Whether or not to fall-back to
    InetAddress resolution if a DNS lookup fails.  InetAddress
    resolution may use local 'hosts' files or other mechanisms.
-   **digestContent** - Whether or not to perform an on-the-fly digest
    hash of retrieved content-bodies.
-   **digestAlgorithm** - The algorithm (for example MD5 or SHA-1) used
    to perform an on-the-fly digest hash of retrieved content-bodies.

###### fetchHttp

-   **timeoutSeconds** - This setting determines how long an HTTP
    request will wait for a resource to respond.  This setting should be
    set to a high value.
-   **maxLengthBytes** - This setting determines the maximum number of
    bytes to download per document.  When the limit is reached the
    document will be truncated.  By default this setting is a very large
    value (in the exabyte range) that will theoretically never be
    reached.
-   **maxFetchKBSec** - The maximum rate in `KB/sec` to use when
    fetching data from a server. The default of 0 means no maximum.
-   **defaultEncoding** - The character encoding to use for files that
    do not have one specified in the HTTP response headers. The default
    is ISO-8859 -1.
-   **shouldFetchBodyRule**- DecideRules applied after receipt of HTTP
    response headers but before download of the HTTP body. If any rule
    returns FALSE, the fetch is aborted. Prerequisites such as
    `robots.txt` are excluded from filtering, i.e. they cannot be
    midfetch aborted.
-   **soTimeoutMs** - If the socket is unresponsive for this number of
    milliseconds, the request is cancelled.  Setting the value to zero
    (no timeout) is not recommended as it could hang a thread on an
    unresponsive server. This timeout is used to time out socket opens
    and socket reads. Make sure this value is less than `timeoutSeconds`
    for optimal configuration.  This ensures at least one retry read.
-   **sendIfModifiedSince** - Send `If-Modified-Since` header, if
    previous `Last-Modified` fetch history information is available in
    URI history.
-   **sendIfNoneMatch** - Send `If-None-Match` header, if previous
    `Etag` fetch history information is available in URI history.
-   **sendConnectionClose** - Send `Connection: close` header with every
    request.
    -   [w3.org connection header
        documentation](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.10)
-   **sendReferer**- The `Referer` header contains the location the
    crawler came from.  This is the page the current URI was discovered
    in. The `Referer` is usually logged on the remote server and can be
    of assistance to webmasters trying to figure out how a crawler got
    to a particular area on a site.
-   **sendRange**- Send the `Range` header when there is a limit on the
    retrieved document size.  This is for politeness purposes.  The
    `Range` header states  
    that only the first n bytes are of interest.  It is only pertinent
    if `maxLengthBytes` is greater than zero.  Sending the `Range`
    header results in a  
    `206 Partial Content` status response, which is better than cutting
    the response mid-download. On rare occasion, sending the `Range`
    header will  
    generate `416 Request Range Not Satisfiable` response.
-   **ignoreCookies** - Disable cookie handling.
-   **sslTrustLevel**- The SSL certificate trust level. The range is
    from the default `open` (trust all certs including expired,
    selfsigned, and those for which we do not have a CA) through `loose`
    (trust all valid certificates including selfsigned), normal (all
    valid certificates not including selfsigned) and strict (Cert is
    valid and DN must match servername).
-   **acceptHeaders** - Accept Headers to include in each request. Each
    must be the complete header, e.g., `Accept-Language: en`.
-   **httpBindAddress**- Local IP address or hostname to use when making
    connections (binding sockets). When not specified, uses default
    local address(es).
-   **httpProxyHost** - The proxy host ip address.
-   **httpProxyPort** - The proxy port.
-   **digestContent** - Whether or not to perform an on-the-fly digest
    hash of retrieved content-bodies.
-   **digestAlgorithm** - Specifies which algorithm (for example MD5 or
    SHA-1) is used to perform an on-the-fly digest hash of retrieved
    content-bodies.

###### extractorHtml

-   **extractJavascript** - If true, in-page Javascript is scanned for
    strings that appear to be URIs. This typically finds both valid and
    invalid URIs.  Attempts to fetch the invalid URIs can generate
    webmaster concern over odd crawler behavior. Default is true.
-   **extractValueAttributes**- If true, strings that look like URIs
    found in unusual places (such as form `VALUE` attributes) will be
    extracted. This typically finds both valid and invalid URIs. 
    Attempts to fetch the invalid URIs may generate webmaster concerns
    over odd crawler behavior. Default is true.
-   **ignoreFormActionUrls** - If true, URIs appearing as the `ACTION`
    attribute in HTML FORMs are ignored. Default is false.
-   **extractOnlyFormGets** - If true, only `ACTION` URIs with a
    `METHOD` of `GET` (explicit or implied) are extracted. Default is
    true. 
-   **treatFramesAsEmbedLinks**- If true, `FRAME/IFRAME SRC`-links are
    treated as embedded resources (like `IMG`, 'E' hop-type).  Otherwise
    they are treated as navigational links.  Default is true.
-   **ignoreUnexpectedHtml** - If true, URIs which end in typical
    non-HTML extensions (such as `.gif`) will not be scanned as if it
    were HTML.  Default is true.
-   **maxElementLength** - The maximum length of an HTML element.
-   **maxAttributeNameLength** - The maximum length of an HTML attribute
    name.
-   **maxAttributeValueLength** - The maximum length of an HTML
    attribute value.

###### warcWriter

-   **compress** - If this setting is true, WARC file content will be
    compressed.  Note that compression applies to each content item
    stored in the WARC.
-   **prefix** - The prefix of the WARC filename.
-   **maxFileSizeBytes**- This setting determines the maximum size in
    bytes for each WARC file.  Once the WARC file reaches this size, no
    URIs will be written to it and another WARC file will be created to
    handle the remaining URIs.  This setting is not a hard limit.  If
    exceptionally large URIs are being downloaded, the WARC file may
    greatly exceed this limit.  Content items stored in WARC files are
    never split between WARCs.
-   **storePaths**- This setting is a list of paths into which WARC
    files will be written.  If more than one path is specified, a
    round-robin approach will be used to choose the path.  This setting
    is safe to change during a crawl.
-   **poolMaxActive**- Heritrix maintains a pool of WARC files that are
    each ready to accept downloaded documents.  This approach is used to
    prevent WARC writing from being a bottleneck in a multithreaded
    environment. This setting establishes the maximum number of such
    files to keep ready. The default value is five. For small crawls
    that you want to limit to a single WARC file, this setting should be
    set to one.
-   **maxWaitForIdleMs** - controls how long a thread waits for an
    reusable writer before considering creating a new one. If creation
    isn't allowed, threads will wait indefinitely for a writer to become
    available.
-   **skipIdenticalDigests**- Whether to skip the writing of a record
    when URI history information is available and indicates the prior
    fetch had an identical content digest.  Default is false.
-   **maxTotalBytesToWrite** - Total file bytes to write to disk. Once
    the size of all files on disk has exceeded this limit, this
    processor will stop the crawler. A value of zero means no upper
    limit.
-   **directory** - The directory in which the `storePaths` will be
    configured.
-   **writeRequests** -  Whether to write `request` type records.
    Default is true.
-   **writeMetadata** - Whether to write `metadata` type records.
    Default is true.
-   **writeRevisitForIdenticalDigests**- Whether to write `revisit` type
    records when a URI's history indicates the previous fetch had an
    identical content digest. Default is true.
-   **writeRevisitForNotModified** - Whether to write `revisit` type
    records when a `304-Not Modified` response is received. Default is
    true.

###### candidates

-   **seedsRedirectNewSeeds** - If enabled, any URI found because a seed
    redirected to it (original seed returned 301 or 302), will also be
    treated as a seed.

###### disposition

-   **delayFactor** - How many multiples of the last fetch elapsed time
    to wait before recontacting the same server.
-   **minDelayMs**- The minimum time to wait after a request has been
    completed before recontacting the same server.  This value overrides
    the `delayFactor`.
-   **respectCrawlDelayUpToSeconds** - Whether to respect a
    `Crawl-Delay` (in seconds) provided by the site's `robots.txt`.
-   **maxDelayMs**- The maximum amount of time to wait after a request
    has been completed before recontacting the same server.  This value
    overrides the `delayFactor`.
-   **maxPerHostBandwidthUsageKbSec** - The maximum per-host bandwidth
    usage.
