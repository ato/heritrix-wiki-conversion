# Launching and Monitoring the Crawl

# Heritrix 2.0 Tutorial

## Launching and Monitoring the Crawl

### Readying the Job

So far we've been editing the basic\_seeds\_profile. To turn a profile
into a job, click the "Copy" link next to the profile's name on the
Engine Screen. This will give you an opportunity to enter a name for the
job; by default the job's name will be the same as the profile's, with a
timestamp added at the end.

### Launch and Start

To begin a crawl, click the 'Launch' option on the ready job in the jobs
list of the Engines Screen.

The crawl will be initialized. (If there are errors in your
configuration, you may get a error dump page; if so , you will need to
back up, fix your settings sheets, and try a fresh launch.)

If you are shown the Crawl Engine Console, you will see your job in a
'PREPARED' state. Click the 'Start' link to actually begin crawling.

### Monitoring via Console

The Crawl Engine Console shows crawl rates and progress, and offers
links to viewing the crawl Logs and Reports. Estimations of time
remaining are very crude and guaranteed to be a gross underestimate.

### Termination of Crawl

A crawl will automatically terminate when all valid, discovered URIs are
successfully crawled (or proven uncrawlable after the configured retry
policies). Often crawls that seem to making little to no progress have
reached a stage where all URIs remaining to be crawled are in a
slow-retry mode (as when a server is unresponsive) or when all URIs
remain on a small number of deep servers, so threads remain mostly idle
respecting politeness limits.

To manually terminate a crawl, use the 'Terminate' link in the console's
Job area.
