# Feature Notes - 1.12.0

## Overview

The key new features of 1.12.0 involve support for strategies to reduce
the amount of duplicate material crawled or stored. Each is accomplished
by adding one or more new processors to the crawler's processing chain,
using new options on old processors, and possibly carrying forward
information from earlier crawls to later crawls.

The three stategies implemented are:

### A. Note and discard exact duplicate content repeated from previous crawls.

Content is retrieved and hashed, and when hash exactly matches previous
retrieval, the duplication is noted and the duplicate content discarded.
Reduces storage used but not bandwidth.

This is accomplished in Heritrix 1.12.0 by:

-   Using the FetchHistoryProcessor and either PersistLogProcessor or
    PersistStoreProcessor (but not both) on an initial crawl
-   Carrying forward the initial crawl info in a form accessible to a
    later crawl, perhaps by using utility functionality on the
    PersistProcessor class
-   Using the PersistLoadProcessor and FetchHistoryProcessor in a
    following crawl so that relevant history information is available at
    store-decision time
-   Using new options on any writer processors to skip or abbrieviate
    storage as desired

### B. Abbrieviate retrieval of unchanged content.

Based on headers of previous retrieval of same URI, adjust current
retrieval (via conditional-GET requests) so that if content is
unchanged, retrieval ends quickly and cheaply and no duplicate content
is stored. Motivated by KB-Denmark study (Clausen 2004); reduces
bandwidth used as well as storage.

This is accomplished in Heritrix 1.12.0 by:

-   Using the FetchHistoryProcessor and either PersistLogProcessor or
    PersistStoreProcessor on an initial crawl
-   Carrying forward the initial crawl info in a form accessible to a
    later crawl, perhaps by using utility functionality on the
    PersistProcessor class
-   Using the PersistLoadProcessor and FetchHistoryProcessor in a
    following crawl so that relevant history information is available at
    store-decision time
-   Using new capabilities of the FetchHTTP processor to issue
    conditional-GETs where appropriate
-   Using new options on any writer processors to skip or abbrieviate
    storage as desired

### C. Note and discard duplicate 'trap' content from same crawl.

For one simple kind of crawler-trap, where followup URIs return
identical content at different (extended) URIs, disable link-extraction.

The TrapSuppressExtractor in 1.12.0 demonstrates this strategy, and
could be the basis for other similar trap/duplicate suppression
processors.

## Initial Crawl

Two processors are added to a crawl to ensure URI data sufficient for
future duplication reduction is retained:

1.  FetchHistoryProcessor, after the last fetching processor.
2.  Either PersistLogProcessor or PersistStoreProcessor (but not both),
    after all other processors.

## Between Crawls

A recrawl must have its BerkeleyDB-JE 'environment' (typically stored in
the 'state' directory) primed with a uri-history database to enable
duplication-reduction features.

If the PersistStoreProcessor was used, the 'state' directory from the
previous crawl may be used directly in the next crawl. Alternatively,
the PersistProcessor (which has a utility main() method) may be invoked
at the command line to copy the uri-history database from the
environment in the first crawl's state directory to a new environment
directory.

If the PersistLogProcessor was used, the generated log (default name
'persistlog.txtser') must be imported to a environment directory. Again,
the PersistProcessor utility main() may be used.

In both cases where the PersistProcessor utility main() is used, the
first argument is the 'source' (either an environment directory or
persist-log) and the seoond argument is the 'destination' (environment
directory).

## Recrawl

The recrawl must have its 'state' directory pointed at a valid
environment directory with uri-history from the previous crawl(s). (This
environment will be modified in place by the recrawl in progress.)

The recrawl must also use the following two processors:

1.  FetchHistoryProcessor, after the last fetching processor
2.  PersistLoadProcessor, before any fetch processor

(It may also use either a PersistStoreProcessor or PersistLogProcessor,
to continue saving information from this crawl for future crawls.)

If conditional-GETs against webservers are desired to reduce bandwidth
usage, ensure that the 'send-if-modified-since' and/or
'send-if-none-match' (etags) options are enabled on the FetchHTTP
processor. Remember that when conditional GETs work, the duplicate
content is never received, and so outlinks that have changed may never
be discovered. (When using conditional GETs, you may also want ot ensure
all URIs from the first crawl are
[re-fed](How-To%20Feed%20URLs%20in%20bulk%20to%20a%20crawler) into the
recrawl.)

If skipping the writing of repeat content (by identical content digest)
is desired to reduce storage usage, ensure the 'skip-identical-digests'
option is enabled on the ARC/WARC writing processor. (URIs which are not
written are annotated as 'unwritten' in the crawl.log.)
