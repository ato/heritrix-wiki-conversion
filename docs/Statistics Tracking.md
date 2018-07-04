# Statistics Tracking

Any number of statistics tracking modules can be attached to a crawl. 
Currently only one is provided with Heritrix.  The `statisticsTracker`
Spring bean that comes with Heritrix creates the
`progress-statistics.log` file and provides the WUI with data to display
progress information about the crawl.  It is strongly recommended that
any crawl run through the WUI use this bean.
