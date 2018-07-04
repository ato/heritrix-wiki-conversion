# Issue best practices

## include the revision number when pasting commit comments in issues

this makes it easy to review changes in FishEye, and at some point
(hopefully) changesets may be [automagically
linked](http://confluence.atlassian.com/display/JIRASTUDIO/Creating+Links)
when using the appropriate format. here's a good example from
[HER-1760](https://webarchive.jira.com/browse/HER-1760):

    Noah Levitt added a comment - 2010-07-21 02:04
    Committed possible fix suggested by Gordon. 

    ------------------------------------------------------------------------ 
    r6919 | nlevitt | 2010-07-20 19:03:30 -0700 (Tue, 20 Jul 2010) | 6 lines 
    Changed paths: 
       M /trunk/heritrix/src/java/org/archive/crawler/admin/CrawlJobHandler.java 

    Possible fix from Gordon for [HER-1760] deadlock starting new job 
    * CrawlJobHandler.java 
        terminateCurrentJob() - if startingNextJob thread exists, wait for it to 
        finish, to avoid competing for the lock on 
        CrawlController.registeredCrawlStatusListeners 

in the [issue
comment](https://webarchive.jira.com/browse/HER-1760?focusedCommentId=25196&page=com.atlassian.jira.plugin.system.issuetabpanels%3Acomment-tabpanel#action_25196),
"r6919" could/should be linked to the FishEye changeset as it
(currently) is in this wiki page.
