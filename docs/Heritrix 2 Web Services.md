# Heritrix 2 Web Services

# Heritrix 2 Web Services (Ideas)

Note: Only the Web UI and JMX RMI interfaces current exist, the rest is
under discussion.  
![](attachments/4493/90996975.png)  
 

## HTTP JMX bridge

The JMX bridge will provide a very thin wrapper allow access to all JMX
operations and attributes to HTTP clients. Its purpose is to provide a
fallback for complex or infrequently used operations that may not be
available through the simpler RESTful interface.

 The current plan is to start with the [MX4J
HttpAdaptor](http://mx4j.sourceforge.net/docs/ch05.html) and replace the
serialization code so that it supports open MBean CompositeData types.
Alex is experimenting with this in the
[aosborne\_webservice](http://archive-crawler.svn.sourceforge.net/viewvc/archive-crawler/branches/aosborne_webservice/)
branch.

## RESTful interface

See also [Draft REST API](Draft%20REST%20API)

The RESTful interface will provide a simplified interface for
controlling a crawl engine. It will be aimed (initially) at small-scale
crawls by scripts and curation tools like Archive-It, WCT and PANDAS.

### Features

#### Get Engine Status

-   Busy/available
-   Estimated time until available?
-   Current job information? (see Get Job Status)

#### Start New Job

-   Ideally: Be able to POST a bundle or a URL to a bundle that
    completely describes a crawl job (config, seeds etc).

<!-- -->

-   Also need to be able to recover an existing job.

#### Get Job Status

Erik proposed the ability to get the job status in a similar format to
the Start New Job order, so that it would be easy to rerun a job etc.

#### Modify Job

-   New settings
-   Add new URLs/seeds

#### Control Job

-   Pause/Resume
-   Kill
-   Checkpoint
-   Generate reports

Notification (or poll) when command is complete?  

#### Get New Files (or callback notification)

Allow scripts to poll or register for a callback notification when an
ARC or log file is completed and closed. They can then move the files to
a more permanent storage system, start Nutch indexing etc etc.

#### Job Completion

-   Poll/notification
-   Ability to retrieve a list of URLs to job output artifacts (logs,
    ARCs, reports etc)
-   How long do we keep around finished job info?

### Notifications

-   Change of status (eg paused, stopped, started, cancelled)
-   ARC completed

The most obvious implementation option seems to be registering for a
notification by supplying the crawler with a URL, which it will POST to
when the event occurs.

## Multiplexer (HCC 2)

The engine multiplexer will be the Heritrix 2 counterpart to
[HCC](http://crawler.archive.org/hcc/). Current thinking is that the
multiplexer should be very lightweight. It will maintain a list of
available crawl engines and will point (either through redirection or
proxying) clients to an available crawler.

### Features

#### List Engines

#### Start Job Anywhere / Get Available Engine?

#### Find Job

#### Broadcast Config Changes (Profile/Modification)

  

## File Service

A useful feature would be the ability to access log files and ARC files
remotely.  In the interests of simple configuration, perhaps just have
the jobs directory read-only mounted on the Heritrix crawler HTTP
server. For more complex systems you could just run some external
WebDAV/Samba/FTP/NFS/whatever daemon and have Heritrix generate
appropriate URLs to it. One suggested feature was an API to update the
manifest when ARCs and logs are ingested into an external repository and
removed from the local disk.

## Attachments:

![](images/icons/bullet_blue.gif){width="8" height="8"}
[heritrix\_ws.png](attachments/4493/90996975.png) (image/png)  
