# crawl manifest

An example crawl manifest file from Heritrix 1.15:

**crawl-manifest.txt**

L+ /1/crawldata/CRAWL-03-16-2010/logs/crawl.log  
L+ /1/crawldata/CRAWL-03-16-2010/logs/runtime-errors.log  
L+ /1/crawldata/CRAWL-03-16-2010/logs/local-errors.log  
L+ /1/crawldata/CRAWL-03-16-2010/logs/uri-errors.log  
L+ /1/crawldata/CRAWL-03-16-2010/logs/progress-statistics.log  
C+ /0/jobs/CRAWL-03-16-2010/order.xml  
C+ /0/jobs/CRAWL-03-16-2010/settings/com/youtube/settings.xml  
C+ /0/jobs/CRAWL-03-16-2010/seeds.txt  
R+ /1/crawldata/CRAWL-03-16-2010/hosts-report.txt  
R+ /1/crawldata/CRAWL-03-16-2010/mimetype-report.txt  
R+ /1/crawldata/CRAWL-03-16-2010/responsecode-report.txt  
R+ /1/crawldata/CRAWL-03-16-2010/seeds-report.txt  
R+ /1/crawldata/CRAWL-03-16-2010/crawl-report.txt  
R+ /1/crawldata/CRAWL-03-16-2010/processors-report.txt

L+ items are log files  
C+ items are config files  
R+ items are report files

The crawl manifest is generated upon clicking "terminate" for a job in
the Heritrix web UI. It may take some time to create (20 minutes?) so be
patient and don't shut down Heritrix too soon.
