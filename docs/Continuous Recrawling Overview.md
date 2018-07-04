# Continuous Recrawling Overview

-   [Continuous Recrawling
    Overview](#ContinuousRecrawlingOverview-ContinuousRecrawlingOverview)
    -   [Generic
        Scenario](#ContinuousRecrawlingOverview-GenericScenario)
    -   [Concrete Target
        Scenario](#ContinuousRecrawlingOverview-ConcreteTargetScenario)
    -   [Design Strategy](#ContinuousRecrawlingOverview-DesignStrategy)

-   [Continuous Recrawling Phase A Design
    Notes](Continuous%20Recrawling%20Phase%20A%20Design%20Notes)
    -   [Frontier Unbundling Design
        Details](Frontier%20Unbundling%20Design%20Details)
    -   [Springified Heritrix Design
        Details](Springified%20Heritrix%20Design%20Details)
    -   [Streamlined Checkpointing Design
        Details](Streamlined%20Checkpointing%20Design%20Details)
-   [Continuous Recrawling Phase B Design
    Notes](Continuous%20Recrawling%20Phase%20B%20Design%20Notes)
-   [Continuous Recrawling Phase C Design
    Notes](Continuous%20Recrawling%20Phase%20C%20Design%20Notes)

# Continuous Recrawling Overview

## Generic Scenario

In broad terms, this is the main capability we want to add in this
'continuous recrawling' phase of Smart Crawler development.

-   want to crawl X thousand sites (0&lt;X&lt;100)
-   sites/URIs are split into N groups (mostly, by domain; possibly, by
    URI-pattern/discovery-path/etc.)
-   each group has a target minimum-visit-interval and
    maximum-visit-interval
    -   crawlers' goal is to visit pages on a site no more frequently
        than each min-visit-interval, but no less frequently than
        max-visit-interval.
    -   actual rate between those boundaries should be based on observed
        change rates - deduced from content and headers

## Concrete Target Scenario

The realistic, multi-month test crawl we intend as the target use (and
primary testbed) of Continuous Recrawling will be a variant of the
generic scenario with these additional parameters:

-   50K sites chosen: 45K 'general' and 5K 'intense'
-   general sites: min-visit 1 week max-visit 3 months
-   intense sites: min-visit 1 day max-visit 1 month
-   further overlay: 'usually static' filetypes: min-visit 1 month,
    max-visit 6 months

## Design Strategy

We intend to split the design and implementation work into three broad
and somewhat overlapping phases:

Phase A's goals will be to resolve outstanding concerns with the 2.x
settings/configuration system and enhance checkpointing to plausibly
support continuous crawls of arbitrary duration, even if they need to
restart with significantly updated software. These changes will
culminate in the official 3.0 release. [Continuous Recrawling Phase A
Design Notes](Continuous%20Recrawling%20Phase%20A%20Design%20Notes)

Phase B's goals will be to add new capabilities to the Frontier queues,
already-seen structure, and URI history store to support many styles of
recrawling. These changes will appear in the early testing versions of
3.2. [Continuous Recrawling Phase B Design
Notes](Continuous%20Recrawling%20Phase%20B%20Design%20Notes)

Phase C's goals will be to implement a minimal set of workable revisit
policies and accompanying UI work to support the generic and concrete
useage scenarios, and ensure the stability of the work over many months
of crawling and in combination with the earlier Smart Crawler phase
features. These changes will be fully available in the final 3.2
release. [Continuous Recrawling Phase C Design
Notes](Continuous%20Recrawling%20Phase%20C%20Design%20Notes)
