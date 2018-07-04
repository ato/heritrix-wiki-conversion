# Development Notes

Most development effort is now directed at the Heritrix3 line. General
information about 3.x development is available at [Heritrix3](Heritrix3)
. A major theme of the 3.x releases will be enabling adaptive &
continuous revisit crawling at large scale. Upcoming work towards that
goal will include:

-   refactoring and possibly combining the internal uri-history and
    already-included data structures; improving flexibility of frontier
    queues (offering the possibility of long-lived timing queues and
    multiple queues per host/exclusion-grouping)
-   enabling revisit of discovered URIs according to a swappable policy,
    which may take into account desired revisit intervals and detected
    URI change rates on previous visits

Other areas of upcoming attention, though not yet scheduled for specific
target releases, include:

-   improving the usability and documentation of recently-added features
    (duplication-suppression; tunable prioritization) in typical
    operator workflows
-   improving the automated test coverage with simulated crawling,
    especially for non-default feature configurations and
    longer/performance-intensive test runs
-   better crawling of web video content with default configurations
-   a web-services interface as an alternative to JMX for remote-control
    of the crawler
-   new heuristics and knowledge-sharing for trap/spam reduction
-   improved during-crawl queue-oriented reporting, including better
    predictions of completion times
-   improved options for crawling access-controlled
    (password/other-auth) sites
