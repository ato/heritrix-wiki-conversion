# When taking a snapshot Heritrix renames crawl.log

When taking a snapshot of a crawl, Heritrix will rename the crawl.log
file.  For example, the default file 'crawl.log' will be named
crawl.logXXX where XXX is a combination of a sequential id and a
timestamp.  This may cause issues if you are, for example, using a
script to monitor log entries by explicitly referencing  'crawl.log'.
