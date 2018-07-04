# Streamlined Checkpointing Design Details

# Goals

## Avoid full, slow pause

-   split URI processing into two phases: that which is transient (can
    be thrown away as long as URI is retried) and that which changes
    persistent stats or structures (which should complete to consistency
    before checkpoint proceeds)
-   step right after laggy network fetch is threshold between phases
-   initiating checkpoint requires exclusive lock on a
    frontier-atomic-mutation-lock that is usually available to multiple
    threads
-   allow holding URIs after fetch - semi-paused crawler - so checkpoint
    can occur as soon as all needing-persistence processing finishes
    (but without waiting for any fetches to complete)

## Improve Speed

-   using running on-disk structures that can just be frozen/bookmarked,
    rather than requiring fresh dump/copy. (eg: like LVM snapshots)
-   move as much simply copying outside crawler process: checkpoint is
    mostly manifest of files to restore crawl; it's up to operator to
    copy those elsewhere if desired

## Improve Robustness across code changes

-   each object responsible for own checkpointing
-   deemphasize serialization; perform most component-state-saving to a
    loose textual format (JSON or XML) for easier
    restore-to-altered-code or offline hand-editting
-   optional Checkpoint component in config; if present all components
    should restore from it
-   wiring is transient – always comes from configuration

# General approach

Each crawler component with checkpointable state will implement a
distinguished interface that both allows a request they checkpoint their
state, and an (optional) startState property.

When a checkpoint is triggered/requested, they will write their state to
the provided location (possibly including pointers to pre-existing
in-crawl files that make up part of their state).

When a crawl is started, **if** the startState property is configured,
they will perform an additional load-from-disk of their state.
