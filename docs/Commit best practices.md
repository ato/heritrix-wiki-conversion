# Commit best practices

## specify issue, files modified, and summary

-   specify related issue number and title
-   optionally precede first line with "Fix for" or the like
-   specify source file changed, preceded by \*
-   summarize changes to each source file, preceded (usually) 4 spaces

for example, changeset r6912

    [HER-1796] H3: interval rescheduling becomes erratic after URI rescheduled more than maxRetries times
    * CrawlURI.java
        improve comments for fetchAttempts methods
        (resetForRescheduling) added to clear per-scheduling state
    * WorkQueueFrontier.java
        call resetForRescheduling just before scheduling-at-specific-time
    * FrontierJournal.java, AbstractFrontier.java
        renamings: prefer 'reenqueue' instead of 'reschedule' for describing simple (non-timed) retries
