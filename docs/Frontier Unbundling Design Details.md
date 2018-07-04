# Frontier Unbundling Design Details

# Initial Analysis

## Discovered URI chain?

Current things that happen to a discovered URI:

-   scope rules applied – some URIs rejected (LinksScoper)
-   URI passed to frontier for scheduling (FrontierScheduler)
    -   URI canonicalized (inside frontier sync; bottleneck)
    -   URI precedence value assigned (inside frontier sync; bottleneck)
-   used to choose queue key (inside frontier)

There may be other bits of processing/classification that can occur to
discovered, not-yet-fetched URIs, so setting all these steps up in a new
configurable chain makes sense from a flexibility standpoint, from and
offloading complexity from frontier standpoint, and decreasing
serialized bottlenecks.

## Policies applied to URI being fetched

Can be moved to a late-in-processing-chain module:

-   disposition disposition decision (success, retry, failure) moves to
    a dispositiondecision module late in processor chain
-   politeness delay moves to politenesspolicy module in processing
    chain

# Three Processing Chains

We can refactor crawl-configuration to feature three chains of
Processors.

Two are together analogous to the existing ProcessorChain, and apply to
URIs that come off the frontier. The first chain is the 'fetch chain',
and includes all steps that may be freely aborted/repeated in the case
of checkpoints. The second chain is the 'disposition chain', and any URI
which begins this chain should finish it, with all the attendant
mutation of frontier queues and total stats,before a checkpoint is
attempted. In the disposition chain, the former CrawlStateUpdater has
been renamed DispositionProcessor and in addition to its previous
robots/stats updating, now updates the CrawlURI with info (like
calculated politeness delays) for the frontier to consider.

The third chain takes the place of steps which now happen in LinksScoper
and FrontierScheduler and the frontier, for URIs that have not yet been
scheduled to a queue. This chain can be called 'candidate chain'. In
addition to scoping, it also prepares the CrawlURI with precalculated
info for all frontier decisions -- allowing these policies to be applied
in parallel, outside the critical frontier locks/managerThread.

## Candidate Chain

The CandidateChain will usually contain only two processors (though of
course more can be added):

-   CandidateScoper: applies scoping to the one URI being processed,
    setting its fetchStatus negative if it should not be scheduled
-   FrontierPreparer:
    -   calculates 'schedulingDirective' coarse prioritization
    -   calculates canonicalized URI
    -   calculates destination-queue key
    -   calculates 'cost'
    -   calculates URI precedence, if any

The candidate chain is applied to URIs:

-   discovered during the crawl

The FrontierPreparer, however, is also available directly to the
Frontier for help prepping any URIs that do not (yet) go through the
CandidateChain, such as seeds or other URIs added other ways mid-crawl.

The CandidateChain is applies to each candidate URI in turn by a new
processor, CandidatesProcessor, that replaces the LinksScoper and
FrontierScheduler.

## Fetch Chain

The FetchChain is the same as the first part of the general processing
chain from H1/H2. It includes processors which:

-   recheck scoping, if desired
-   check/enforce preconditions
-   try a fetch
-   do link-extraction
-   write ARC/WARC

## Disposition Chain

The DispositionChain contains all steps which should be done atomically
with regard to checkpointing. It will typically include just two
processors:

-   CandidatesProcessor: replaces the old LinksScoper and
    FrontierScheduler, running the candidate chain on each discovered
    URI, then scheduling (or applying special discovered-seed handling)
    for any URIs not cancelled by that chain
-   DispositionProcessor: the renamed CrawlStateUpdater, updating stats,
    robots, and prefilling the CrawlURI with decisions/delays for the
    frontier to consult

(Some crawls may wish to move ARC/WARC writing to the disposition chain,
if the risk of a small number of duplicate written-fetches after
checkpoint-resumptions is a concern.)

s
