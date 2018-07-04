# Precedence Feature Notes

# Precedence Feature Notes

## Introduction

Heritrix 2.0 adds a new mechanism for controlling the order in which
URIs are crawled based on positive integer 'precedence' values on URIs
and queues of related URIs.

Precedence values are an expression of ranking, and lower numbers mean
higher rank and earlier handling. (That is, '1' is the highest
precedence.)

Precedence values are assigned by switchable policies inside the
Heritrix frontier. There is a UriPrecedencePolicy for assigning URI
precedences, and a QueuePrecedencePolicy for assigning queue
precedences. These policies can also be overridden for particular queues
or URI SURT prefixes, so that URIs/queues of natural groupings can be
forced to a specific precedence value.

## URI precedence overview

URI precedence values are assigned when a URI is first scheduled into a
frontier for crawling. There is currently no provision for a URI's
precedence to change after initial assignment.

URI precedence affects the order in which URIs are arranged within a
queue of related URIs. (Many such queues, usually on the basis of domain
name or some fragment thereof, are maintained by a heritrix frontier
implementation.)

Numerically lower precedence values sort earlier in the queue, and thus
can be thought of as having higher precedence.

URI precedence is separate from and subordinate to the 4
'scheduling-directive' constants (of
org.archive.crawler.datamodel.SchedulingConstants). That is, scheduling
directive is considered first, then precedence.

There is no necessary relationship between URI precedence values and
queue precedence values, but a queue policy may consider URI precedences
to set a queue's precedence, as with the
HighestUriQueuePrecedencePolicy.

While hypothetically any number of precedence values up to
Integer.MAX\_VALUE may be used, only values up to 127 are guaranteed by
the current implementation to sort in a queue as expected. Using a large
number of different precedence values will tend to make URI-enqueuing
more expensive (multiple 'hot' insert points in the sorted BDB-backed
queue structure).

## Queue precedence overview

Queue precedence is initially assigned when a URI-queue is created
inside the frontier to take a URI. The queue's precedence is
recalculated after each URI is added or removed to the queue.

Queue precedence determines which queues, among all in existence, are
first consulted to actively provide URIs for crawling. Those queues with
the numerically lowest precedence values – highest precedence rank – are
always consulted first.

If the crawler can keep all worker ToeThreads busy pulling URIs from a
set of active queues, other lower-precedence queues will wait
indefinitely. Only when a ToeThread is idle, and all previously
activated queues are ineligible to provide URIs (because they are
already in-process, or waiting a polite 'snooze' period before
triggering a revisit to a certain site), will the list of all inactive
queues be consulted to find the highest-precedence-rank queue available
to be activated.

Within the same precedence level, queues are consulted in a round-robin
fashion, deactivating to give other queues a chance in accordance with
the same budgeting/session-balance mechanism as in Heritrix 1.x.

The frontier may also have a global 'precedence-floor' value, and queues
at or below this rank are not eligible to provide URIs at all. (They
collect URIs, but never give them out.) However, since the floor value
or an individual queue's value may be changed during the crawl, groups
of URIs can move from ineligible to eligible or vice-versa, without
having to put in scope blocks that cause URIs to be discarded.

Note that the algorithm used for activating and inactivating queues may
have some counter-intuitive properties. For instance, if you assign all
.gov sites a precedence of 1 and all .com sites a precedence of 2, then
.com seeds can still be crawled before .gov seeds, due to the way that
seeds are scheduled in the Frontier. The situation will quickly correct
itself however; the .com sites won't be crawled too deeply before the
.gov sites overtake them.

## UriPrecedencePolicies

UriPrecedencePolicies are a new category of module in Heritrix 2.0 that
determine the URI precedence value for all URIs discovered by the
crawler. The Frontier has a new setting,
[uri-precedence-policy](https://webarchive.jira.com/wiki/spaces/Heritrix/pages/4403/WorkQueueFrontier+uri-precedence-policy),
that determines which URIPrecedencePolicy module is used. Heritrix ships
with the following UriPrecedencePolicy modules:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Module</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="https://webarchive.jira.com/wiki/spaces/Heritrix/pages/4262/BaseUriPrecedencePolicy">BaseUriPrecedencePolicy</a></p></td>
<td><p>Assigns precedence based on operator setting.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://webarchive.jira.com/wiki/spaces/Heritrix/pages/4263/CostUriPrecedencePolicy">CostUriPrecedencePolicy</a></p></td>
<td><p>Assigns precedence based on Heritrix 1.x cost value.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://webarchive.jira.com/wiki/spaces/Heritrix/pages/4265/HopsUriPrecedencePolicy">HopsUriPrecedencePolicy</a></p></td>
<td><p>Assigns precedence to a URI's hops-from-seed count.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://webarchive.jira.com/wiki/spaces/Heritrix/pages/4422/PreloadedUriPrecedencePolicy">PreloadedUriPrecedencePolicy</a></p></td>
<td><p>Assigns precedence from an external file.</p></td>
</tr>
</tbody>
</table>

By default, the Frontier is set to use CostUriPrecedencePolicy, so URIs
should be considered in the same order as in 1.x.

## QueuePrecedencePolicies

QueuePrecedencePolicies are another new category of module that
determine the queue precedence values. The Frontier has another new
setting,
[queue-precedence-policy](https://webarchive.jira.com/wiki/spaces/Heritrix/pages/4405/WorkQueueFrontier+queue-precedence-policy),
that determines which QueuePrecedencePolicy module is used. The
following QueuePrecedencePolicy modules are provided:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Module</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="https://webarchive.jira.com/wiki/spaces/Heritrix/pages/4261/BaseQueuePrecedencePolicy">BaseQueuePrecedencePolicy</a></p></td>
<td><p>Assigns queue precedence based on operator setting.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://webarchive.jira.com/wiki/spaces/Heritrix/pages/4264/HighestUriQueuePrecedencePolicy">HighestUriQueuePrecedencePolicy</a></p></td>
<td><p>Assigns queue precedence based on the highest URI precedence in the queue.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://webarchive.jira.com/wiki/spaces/Heritrix/pages/4266/SuccessCountsQueuePrecedencePolicy">SuccessCountsQueuePrecedencePolicy</a></p></td>
<td><p>Lowers queue precedence as URIs in that queue are successfully crawled.</p></td>
</tr>
</tbody>
</table>

By default, the Frontier uses BaseQueuePrecedencePolicy. In the absence
of operator overrides, all queues will have the same precedence by
default.

## Examples

### Assigning expert-chosen sites, URLs to specific constant precedence levels

First, set the global configuration. Alter the global sheet so that the
Frontier's queue-precedence-policy is BaseQueuePrecedencePolicy, and set
its base-precedence value to 5. Alter the Frontier's
uri-precedence-policy to be BaseUriPrecedencePolicy, and set its
base-precedence value to 5.

Now create two override sheets, one named HighPrioritySites and one
named LowPrioritySites. In the HighPrioritySites sheet, override the
queue-precedence-policy:base-precedence to be 1. In the LowPrioritySites
sheet, override queue-precedence-policy:base-precedence to be 10. Since
the Frontier uses a SurtAuthorityQueueAssignmentPolicy by default, you
can now assign sites a precedence of 1 or 10 by entering an association
of the SURT form of the site to the HighPrioritySites sheet or the
LowPrioritySites sheet. For instance, if you want to crawl .gov sites
before crawling anything else, you can associate "gov," with the
HighPrioritySites sheet. Similarly, if you wanted to crawl .com sites
after crawling everything else, you can associate "com," with the
LowPrioritySites sheet.

You can follow a similar procedure for assigning URI precedence values.
Create two more override sheets, HighPriorityURI and LowPriorityURI, and
override their uri-precedence-policy:base-precedence to be 1 and 10. Now
you can associate URLs with those sheets to increase or decrease the
URI's precedence.

### Declining precedence once collection target thresholds are met

Set the Frontier's queue-precedence-policy to be
[SuccessCountsQueuePrecedencePolicy](https://webarchive.jira.com/wiki/spaces/Heritrix/pages/4266/SuccessCountsQueuePrecedencePolicy),
then modify its
[base-precedence](https://webarchive.jira.com/wiki/spaces/Heritrix/pages/4398/BaseQueuePrecedencePolicy+base-precedence)
and
[increment-counts](https://webarchive.jira.com/wiki/spaces/Heritrix/pages/4425/SuccessCountsQueuePrecedencePolicy+increment-counts)
setting to suit your needs. For example, with a base-precedence value of
2, and 'increment-counts' of "100,1000", each queue will have a
precedence of 2 until 100 URIs are successfully fetched, then a
precedence of 3 for the next 1000 URIs successfully fetched, then
continue to drop one precedence rank for each 1000 URIs successfully
fetched.

### Content-driven focused crawling – assigning precedence based on content

Custom UriPrecedencePolicy implementations can be written to assign
precedence based on the fetched content of a URI. Although Heritrix does
not ship with such a module, there is an example module and unit test in
the trunk code. The example module increases a URI's precedence based on
the presence of a keyword in the fetched content. To see the code and
run the test, first obtain the Heritrix code via SVN (from
<https://archive-crawler.svn.sourceforge.net/svnroot/archive-crawler/trunk/heritrix2>),
then follow the instructions at [Setting up the new Heritrix in
Eclipse](Setting%20up%20the%20new%20Heritrix%20in%20Eclipse). You can
then view the org.archive.crawler.selftest.KeyWordUriPrecedencePolicy
code in the engine/src/test/java directory.

### Assigning precedence based on external (e.g. link-value 'page rank') precalculation

You can use org.archive.crawler.frontier.precedence.PrecedenceLoader
command-line utility to import a plain text file containing URIs and
precedence values into the crawl history database used by a crawl. The
PrecedenceLoader utility takes two arguments, the source file and the
destination directory containing the BDB environment. The source file
should contain URIs, followed by a space, followed by a precedence
value, eg:

    http://crawler.archive.org/license.html 5
    http://crawler.archive.org/downloads.html 2
    http://crawler.archive.org/faq.html 1

See [Offline PageRank Analysis
Notes](Offline%20PageRank%20Analysis%20Notes) for information on how to
generate pank rank information in the above format from a previously
completed crawl.
