# Continuous Recrawling Phase C Design Notes

# Phase C Design Notes: Settings & Checkpoint Updates

Stage C is the implementation and testing via realistic crawling of more
sophisticated revisit heuristics.

Plan: implement smarter revisit scheduling

-   allow different revisit min/max for different sites and URL patterns
-   implement simple exponential grow/decay in reaction to observed
    change
-   implement additional HTTP header-based heuristics

Issue: Monitoring progress/coverage & operator adjustments

-   extend queue dynamic analysis to provide warnings if target
    visitation rates unattainable
-   add UI for viewing queue progress rates/expected finish times
-   provide bulk queue edit/reschedule operations

Plan: run 'concrete scenario' for 3 months+

-   use to evaluate performance & usability
