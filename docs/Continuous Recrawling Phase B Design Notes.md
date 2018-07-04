# Continuous Recrawling Phase B Design Notes

# Phase B Design Notes: URI History and Queue Updates

General idea: expand core capabilities of default Frontier so that it
can do revisits simply via passed-in guidance from outside optional
components.

Plan: expand options for alreadyIncluded structure

-   move outside frontier if possible
-   implement Mercator-style merging-lists version
-   add option to store history (or at least queue/queueKey) in
    merging-list; allows efficient random-access to enqueued URIs

Plan: Enhance queueing features:

-   add a disk/BDB-backed DelayedQueue-like WorkQueue that can be mixed
    with classic queues; only releases URIs at configured future times
-   resolution of DelayWorkQueue is intentionally crude (~day) to avoid
    random inserts everywhere
-   each classic queue becomes the 'ASAP' queue for the same host/etc;
    an optional 'future' queue can be added
-   implement a mutual-exclusion process for related queues (same
    domain, same IP) to prevent simultaneous issuance of URIs; acquire
    named permits, wait for permit to become available (FIFO)
-   reconcile budget-rotation with precedence
-   have session-budgets cause precedence promotion/demotion rather than
    'deactivation'; or
-   evaluate eliminating budgets in favor of more sophisticated,
    large-range precedence-policies

Plan: introduce queue progress heuristics/predictions

-   collect progress stats on rates of discovery, completion
-   create credible estimates of queue-completion times

Plan: implement naive toy revisit policy

-   fixed-revisit interval as test of queue/frontier capabilities

Stage B will likely generate an early-alpha-quality test release of
eventual 2.4.
