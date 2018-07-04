# Continuous Recrawling Phase A Design Notes

# Phase A Design Notes: Settings & Checkpoint Updates

We expect phase A to end in a standalone 2.2 release.

## Settings/Configuration

Heritrix 2.0's configuration...

-   is modeled on Spring framework in significant ways
-   did not adopt it outright due to concerns that it could not support
    our need to override both values and implementing classes for groups
    of URIs
-   does not yet offer an easy/automated way to bring over 1.x settings
-   uses a custom, ordering-sensitive properties-like on-disk format
    which has generated concern in early feedback
-   leaves override mappings (URIs-&gt;special settings) in a
    hard-to-archive BerkeleyDB database

Plan: move to Spring 2.5-based configuration

-   makes crawler configuration fit a standard model for wiring
    alternate components together and supplying configuration values
-   provides a well-characterized XML format for configuration

Issue: supporting overrides

-   Spring's custom Scopes and wiring callbacks should allow inserting
    an extra level of indirection (wrapper) on components and primitive
    values
-   Actual resolution of values/components would be deferred to runtime,
    and consult override mappings first

Issue: archivable configuration

-   override mappings and alternatve values would also be specified in
    Spring model/syntax
-   those could be included in master config file or others included by
    reference
-   result: configuration of any complexity **could** be represented as
    a single large file – very easy to archive and version
-   or, it could be represented as a collection of related files, most
    of which are standard boilerplate components reused over a long
    period

Issue: changing settings mid-crawl

-   will be possible but by direct manipulation of crawler component
    beans
-   implication: starting configuration will need to be manually changed
    separately
-   for investigation: ways to make this easier/less-error-prone

Issue: UI for composing Spring config

-   offer raw text edit with format/dependency validation option
-   offer guided edit modes (fields with help text, XML-as-template)

Issue: 1.x to 2.x migration tool

-   will wait until Spring-ified settings are ready
-   will work for simple configurations; will provide exception list of
    issues operator needs to hand-fix at end
-   general strategy: walk 1.x settings, find handler for that setting,
    build new XML

See also: [Springified Heritrix Design
Details](Springified%20Heritrix%20Design%20Details)

## Checkpointing

Heritrix checkpointing currently...

-   requires a full-crawler pause
-   relies heavily on Java serialization, for all component state
-   very fragile if software changes before restore (we've never had
    checkpoint compatibility between major releases, and usually not
    between minor releases either)

Plan: quicker, easier, more robust checkpointing

-   split URI processing into two phases: that which is transient (can
    be thrown away as long as URI is retried) and that which changes
    persistent stats or structures (which should complete to consistency
    before checkpoint proceeds)
-   step right after laggy network fetch is threshold between phases
-   allow holding URIs after fetch – semi-paused crawler – so checkpoint
    can occur as soon as all needing-persistence processing finishes
    (but without waiting for any fetches to complete)
-   deemphasize serialization; perform most component-state-saving to a
    loose textual format (JSON or XML) for easier
    restore-to-altered-code or offline hand-editting
-   move activities that are simply copying outside crawler process:
    that is, the checkpoint is mostly manifest of files to restore
    crawl; it's up to operator to copy those elsewhere if desired
-   optional Checkpoint component in config; if present all components
    should restore from it

See also: [Streamlined Checkpointing Design
Details](Streamlined%20Checkpointing%20Design%20Details)

## Frontier Unbundling

Plan: unbundle as much as possible from inside Frontier, into
independent Processors which markup URI

-   generally: let Frontier be as dumb as possible, just follow
    instructions inside URIs scheduled/finished
-   current decisions in frontier that can be moved out:
    -   canonicalization
    -   disposition decision (success, retry, failure)
    -   uri precedence
    -   politeness delay
    -   queue key
-   frontier would throw error if required guidance isn't present

See also: [Frontier Unbundling Design
Details](Frontier%20Unbundling%20Design%20Details)
