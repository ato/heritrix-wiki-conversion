# Draft REST API

These are old notes. Please see the WADL document
(http://archive-crawler.svn.sourceforge.net/viewvc/\*checkout\*/archive-crawler/branches/aosborne\_restws/restws/src/main/resources/org/archive/crawler/restws/wadl.xml)
for the latest version.

In some sense this is really just a machine-consumable version of the
Web UI.

### Crawler Status

Request:

``` bash
GET /
```

Response: (something like)

``` bash
<engines>
  <engine url="http://crawler/" uptime="321332" />
    <jobs capacity="3" available="2">
     <job name="myjobname-20080101123434" url="http://crawler/jobs/myjobname-20080101123434" status="running" />
     <job name="myotherjobname-2008010123212312" url="http://crawler/jobs/myotherjobname-2008010123212312" status="completed" />
    </jobs>
  </engine>
</engine>
```

We could potentially include other info, like disk usage. Suggestions?

The multiplexer can then aggregate all the status checks for a pool of
crawl engines.

### Job Creation

It seems like it would make management and debugging a lot easier if we
have a meaningful name associated with a job, rather than just a
sequential numerical or timestamp-based ID.

Request:

``` bash
POST /jobs

myjobname
```

  
Response:

``` bash
201 Created
Location: /jobs/myjobname
```

Or if a job with that name already exists:

``` bash
409 Conflict
```

#### Recovering a job?

How to do this is interesting. I guess one option is to allow POSTing of
zip which will initialize the job, instead of creating an empty one.

### Job Status

You can retrieve the status of a crawl:

Request:

``` bash
GET /jobs/myjobname/status
```

  
Response:

``` bash
200 OK

pausing
```

  
You can also pause, stop, checkpoint etc a crawl by PUTting:

``` bash
PUT /jobs/myjobname/status

paused
```

#### Command-completion notifications?

``` bash
PUT /jobs/myjobname/status
Notify: http://someclient/checkpointing-complete mailto:igor@example.com

checkpointing
```

### Notifications

``` bash
POST /jobs/myjobname/notifications

events=paused stopped
action=mailto:igor@example.com http://someapp/crawl-halted

Response:

201 Created
Location: /jobs/myjobname/notifications/17
```

You could then cancel your subscription by doing a DELETE on that URL.

### Sheets

#### Creating/updating a sheet:

Request:

``` bash
PUT /jobs/myjobname/sheets/global
Content-type: text/plain

root=map, java.lang.Object
root:metadata=primary, org.archive.modules.writer.DefaultMetadataProvider
root:metadata:description=string, Basic seeds sites crawl.
root:metadata:robots-honoring-policy=primary, org.archive.modules.net.RobotsHonoringPolicy
root:metadata:robots-honoring-policy:user-agents=list, java.lang.String
root:loggerModule=primary, org.archive.crawler.framework.CrawlerLoggerModule
root:seeds=primary, org.archive.modules.seeds.SeedModuleImpl
root:scope=object, org.archive.modules.deciderules.DecideRuleSequence
root:scope:rules=list, org.archive.modules.deciderules.DecideRule
root:scope:rules:0=object, org.archive.modules.deciderules.RejectDecideRule
```

  
Response:

``` bash
201 Created
```

  

#### Associating SURTs

PUT explicitly sets the SURTs. POST appends new SURTs.

Request:

``` bash
POST /jobs/myjobname/sheets/global/surts
Content-type: text/plain

http://(org,archive,blah,
```

  

#### Deleting a sheet

``` bash
DELETE /jobs/myjobname/sheets/global
```

  

### Seeds

#### Setting the seeds:

Request:

``` bash
PUT /jobs/myjobname/seeds
Content-type: text/plain

http://archive.org/
http://yahoo.com/
```

  

#### Append some seeds:

Request:

``` bash
POST /jobs/myjobname/seeds
Content-type: text/plain

http://example.com/
http://example.org/
```

  

#### Retrieve list of seeds:

Request:

``` bash
GET /jobs/myjobname/seeds
```

  

### Reports

#### Retrieve reports

``` bash
GET /jobs/myjobname/reports/crawl
GET /jobs/myjobname/reports/frontier
GET /jobs/myjobname/reports/seed


List of available reports:
GET /jobs/myjobname/reports

(psuedo-XHTML response?)
```

#### Force report generation

``` bash
POST /jobs/myjobname/reports
```
