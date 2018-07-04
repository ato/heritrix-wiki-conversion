# How To Crawl

-   [Requirements](#HowToCrawl-Requirements)
-   [Work Area and Files](#HowToCrawl-WorkAreaandFiles)
-   [Configuration](#HowToCrawl-Configuration)
-   [Run the Crawl](#HowToCrawl-RuntheCrawl)
-   [Check Crawl Status](#HowToCrawl-CheckCrawlStatus)
-   [WARC Output Files](#HowToCrawl-WARCOutputFiles)
-   [Add WARCs to the Archive](#HowToCrawl-AddWARCstotheArchive)
-   [Troubleshooting](#HowToCrawl-Troubleshooting)

> Crawl before you walk. – C. Darwin

# Requirements

To run a web crawl with Heritrix, you'll need the code (Java class
files), config files, and adequate system resources:

-   at least 4 GB of RAM
-   enough local disk space for all the output WARC files
-   as few competing processes as possible

# Work Area and Files

This examples in this document are based on crawls run in a VM
named `blub-dev`, with files named `blub_`...*something*. Use your own
naming conventions.

``` text
blub@blub-dev:/1$ df -h
Filesystem Size Used Avail Use% Mounted on
udev 2.0G 4.0K 2.0G 1% /dev
tmpfs 396M 5.1M 391M 2% /run
/dev/vda1 28G 5.8G 21G 22% /
none 4.0K 0 4.0K 0% /sys/fs/cgroup
none 5.0M 0 5.0M 0% /run/lock
none 2.0G 0 2.0G 0% /run/shm
none 100M 0 100M 0% /run/user
/dev/vdb1 126G 41G 86G 33% /1
nfs-home:/home 7.1T 6.1T 990G 87% /home
```

The `/1` directory has lots of space. We created a directory
called `/1/crawling` and copied Heritrix code and config files,
originally created by John Lekashman for crawls of Cuban sites.

``` bash
# cd /1
# mkdir crawling
# chown blub.users crawling
^D
$ cd /1/crawling
$ cp /home/lekash/blub.crap/* .
$ tar xvf cuba00000.tar
$ mv cuba0000 blub_test
```

We need a standard repo or other source of these code and config files.

# Configuration

The `README` is not required, but is useful to document details of the
crawl that are not specified in configuration files.

``` bash
$ cd blub_test
$ vi README
```

Now let's modify our configuration for this crawl.

``` bash
$ mv cuba test_config
$ cd test_config
```

First we need a *seed* text file of URLs that will be the crawl origins.
In this case, we created the file `mcloud_seeds.txt` from the RSS
file <https://core.mediacloud.org/static/mc_20160317.rss>:

``` bash
$ head mcloud.seeds.txt
http://feeds.washingtonpost.com/c/34656/f/636663/s/4e55a97b/sc/7/l/0L0Swashingtonpost0N0Cblogs0Cright0Eturn0Cwp0C20A160C0A30C170Cwe0Ecant0Edefend0Edemocracy0Eby0Eelecting0Ea0Ethug0C/story01.htm
http://feeds.washingtonpost.com/c/34656/f/636663/s/4e56fd0f/sc/7/l/0L0Swashingtonpost0N0Cblogs0Cright0Eturn0Cwp0C20A160C0A30C170Ca0Elot0Eof0Erepublicans0Eare0Ein0Elindsey0Egrahams0Eshoes0C/story01.htm
http://www.news.com.au/sport/nrl/five-things-you-need-to-know-about-new-nrl-ceo-todd-greenberg/story-fndujljl-1227793059847?from=public_rss
http://www.abc.es/opinion/abci-secta-201603180423_noticia.html
...
```

Now we edit the config values:

``` bash
$ mv cuba.cxml blub_test.cxml
$ vi blub_test.cxml
```

The Heritrix configuration is a complex combination of XML syntax and
Java bean names. The choices depend on how wide and deep your crawl
should be, whether to check duplicate files, and so on. This example is
a fairly constrained crawl.

Edit the values shown below, and leave the other lines as is:

``` bash
# (editable settings in blub_test.cxml)
 
# these will be displayed on the crawl dashboard:
metadata.jobName = blub_test
metadata.description = mediacloud_crawl
 
# output WARC file name prefix, by convention <= 6 chars, ALL CAPS:
warcwriter.prefix = MCLOUD
 
# Java write threads:
warcwriter.poolMaxActive = 6
 
# the "seed" file of URLs:
<property name="path" value="mcloud.seeds.txt">
 
# include this to enable deduplication:
<import resource="hq-beans.xml">
 
# set the hop count (how far to crawl):
<bean class="org.archive.modules.deciderules.TooManyHopsDecideRule">
    <property name="maxHops" value="1" />
</bean>
 
# SURTs (normalized URLs) to avoid (this was one of the copied files):
<bean class="org.archive.modules.deciderules.surt.SurtPrefixedDecideRule">
      <property name="surtsSourceFile" value="negative-surts.txt">
```

Rename and edit this file:

``` bash
$ mv hq-beans.xml.0 hq-beans.xml
$ vi hq-beans.xml
```

    Comment out the uriUniqFilter, hqclient, and hqpersist beans:

 

``` bash
<!--
<bean id="uriUniqFilter"
      class="org.archive.modules.hq.OnlineCrawlMapper">
  <property name="nodeNo" value="0"/>
  <property name="totalNodes" value="4"/>
  <property name="discoveredBatchSize" value="500"/>
  <property name="feedBatchSize" value="80"/>
  <property name="localUniqFilter">
    <bean class="org.archive.crawler.util.BloomUriUniqFilter">
      <property name="bloomFilter">
        <bean class="org.archive.util.BloomFilter64bit">
          <constructor-arg value="250000000"/>
          <constructor-arg value="30"/>
        </bean>
      </property>
    </bean>
  </property>
</bean>
-->
 
<!-- headquarter client adapter used by HttpPersistProcessor and OnlineCrawlMapper -->
<!--
<bean id="hqclient" class="org.archive.modules.hq.HttpHeadquarterAdapter">
</bean>
-->

<!-- finished submitter to be included in disposition chain -->
<!--
<bean id="hqpersist" class="org.archive.modules.hq.HttpPersistProcessor">
</bean>
-->
```

# Run the Crawl

If all goes well, this will work:

``` bash
$ ./startup.sh
```

A web dashboard will now be accessible at port 9443 on the same host
(get the auth name and password from `ps -ef | grep java`):

![](attachments/145326115/145326119.png?height=250){height="250"}

Click on the **test\_config** link, then the blue **build** button at
the top. It should say **Job Is Ready**. Then click the blue **launch**
button. It should display a sequence of status strings after Job Is
Active: `NASCENT`, then `PREPARING`, then `PAUSED`. Click the blue
`unpause` button to (finally!) start the crawl.

The pause function depends on configuration settings that default to
`True`:

`<!-- <property name="pauseAtStart" value="true" /> -->`  
`<!-- <property name="pauseAtFinish" value="true" /> -->`

# Check Crawl Status

Refresh your browser to update the dashboard:

![](attachments/145326115/145326122.png?height=250){height="250"}

This shows how many URLs have been processed and how many are pending,
URL processing rates, thread status, and other data.

# WARC Output Files

WARC files are written by default to the `warcs` subdirectory. Each WARC
is stuffed with about a gigabyte of data before another is created:

``` bash
$ ls -l warcs
total 41005888
-rw-r--r-- 1 blub users 1161204614 Jun  9 21:37 MCLOUD-20160609210332357-00000-5421~blub-dev.us.archive.org~9443.warc.gz
-rw-r--r-- 1 blub users 1064202832 Jun  9 21:56 MCLOUD-20160609210332359-00001-5421~blub-dev.us.archive.org~9443.warc.gz
-rw-r--r-- 1 blub users 1520977725 Jun  9 21:52 MCLOUD-20160609210332360-00002-5421~blub-dev.us.archive.org~9443.warc.gz
-rw-r--r-- 1 blub users 1011777223 Jun  9 21:24 MCLOUD-20160609210332361-00003-5421~blub-dev.us.archive.org~9443.warc.gz
-rw-r--r-- 1 blub users 1000574144 Jun  9 21:52 MCLOUD-20160609210332362-00004-5421~blub-dev.us.archive.org~9443.warc.gz
-rw-r--r-- 1 blub users 1000005845 Jun  9 21:51 MCLOUD-20160609210332363-00005-5421~blub-dev.us.archive.org~9443.warc.gz
-rw-r--r-- 1 blub users 1000015034 Jun  9 22:15 MCLOUD-20160609212455312-00006-5421~blub-dev.us.archive.org~9443.warc.gz
-rw-r--r-- 1 blub users 1000020459 Jun  9 22:36 MCLOUD-20160609213753231-00007-5421~blub-dev.us.archive.org~9443.warc.gz
-rw-r--r-- 1 blub users 1399930055 Jun  9 22:46 MCLOUD-20160609215107987-00008-5421~blub-dev.us.archive.org~9443.warc.gz
-rw-r--r-- 1 blub users 1292349285 Jun  9 23:37 MCLOUD-20160609215207090-00009-5421~blub-dev.us.archive.org~9443.warc.gz
-rw-r--r-- 1 blub users 1000039653 Jun  9 23:32 MCLOUD-20160609215226776-00010-5421~blub-dev.us.archive.org~9443.warc.gz
-rw-r--r-- 1 blub users 1000014926 Jun  9 22:29 MCLOUD-20160609215649483-00011-5421~blub-dev.us.archive.org~9443.warc.gz
-rw-r--r-- 1 blub users 1000021659 Jun 10 01:31 MCLOUD-20160609221555291-00012-5421~blub-dev.us.archive.org~9443.warc.gz
-rw-r--r-- 1 blub users 1000055761 Jun 10 02:23 MCLOUD-20160609222931584-00013-5421~blub-dev.us.archive.org~9443.warc.gz
-rw-r--r-- 1 blub users 1000005175 Jun 10 02:18 MCLOUD-20160609223645636-00014-5421~blub-dev.us.archive.org~9443.warc.gz
-rw-r--r-- 1 blub users 2119870356 Jun 10 00:56 MCLOUD-20160609224628152-00015-5421~blub-dev.us.archive.org~9443.warc.gz
-rw-r--r-- 1 blub users 1462329740 Jun 10 03:29 MCLOUD-20160609233227602-00016-5421~blub-dev.us.archive.org~9443.warc.gz
-rw-r--r-- 1 blub users 1551420349 Jun 10 01:45 MCLOUD-20160609233722737-00017-5421~blub-dev.us.archive.org~9443.warc.gz
-rw-r--r-- 1 blub users 1000022245 Jun 10 05:31 MCLOUD-20160610005626706-00018-5421~blub-dev.us.archive.org~9443.warc.gz
-rw-r--r-- 1 blub users 1704015803 Jun 10 05:38 MCLOUD-20160610013124232-00019-5421~blub-dev.us.archive.org~9443.warc.gz
-rw-r--r-- 1 blub users 1511938554 Jun 10 02:58 MCLOUD-20160610014557756-00020-5421~blub-dev.us.archive.org~9443.warc.gz
-rw-r--r-- 1 blub users 1364297055 Jun 10 08:02 MCLOUD-20160610021836348-00021-5421~blub-dev.us.archive.org~9443.warc.gz
-rw-r--r-- 1 blub users 1013434840 Jun 10 08:21 MCLOUD-20160610022319581-00022-5421~blub-dev.us.archive.org~9443.warc.gz
-rw-r--r-- 1 blub users 1815742049 Jun 10 06:20 MCLOUD-20160610025853439-00023-5421~blub-dev.us.archive.org~9443.warc.gz
-rw-r--r-- 1 blub users 1000058523 Jun 10 05:40 MCLOUD-20160610032921930-00024-5421~blub-dev.us.archive.org~9443.warc.gz
-rw-r--r-- 1 blub users 1096104506 Jun 10 10:18 MCLOUD-20160610053126093-00025-5421~blub-dev.us.archive.org~9443.warc.gz
-rw-r--r-- 1 blub users 1325952334 Jun 10 09:10 MCLOUD-20160610053804044-00026-5421~blub-dev.us.archive.org~9443.warc.gz
-rw-r--r-- 1 blub users 1004554334 Jun 10 15:06 MCLOUD-20160610054041702-00027-5421~blub-dev.us.archive.org~9443.warc.gz
-rw-r--r-- 1 blub users 1006686502 Jun 10 07:13 MCLOUD-20160610062044379-00028-5421~blub-dev.us.archive.org~9443.warc.gz
-rw-r--r-- 1 blub users 1262064822 Jun 10 09:47 MCLOUD-20160610071347444-00029-5421~blub-dev.us.archive.org~9443.warc.gz
-rw-r--r-- 1 blub users 1346247746 Jun 10 12:31 MCLOUD-20160610080214994-00030-5421~blub-dev.us.archive.org~9443.warc.gz
-rw-r--r-- 1 blub users 1000015074 Jun 10 18:00 MCLOUD-20160610082131840-00031-5421~blub-dev.us.archive.org~9443.warc.gz
-rw-r--r-- 1 blub users  936592729 Jun 10 18:11 MCLOUD-20160610091017844-00032-5421~blub-dev.us.archive.org~9443.warc.gz.open
-rw-r--r-- 1 blub users  832670771 Jun 10 18:11 MCLOUD-20160610094801606-00033-5421~blub-dev.us.archive.org~9443.warc.gz.open
-rw-r--r-- 1 blub users  670126053 Jun 10 18:11 MCLOUD-20160610101843380-00034-5421~blub-dev.us.archive.org~9443.warc.gz.open
-rw-r--r-- 1 blub users  337385272 Jun 10 18:11 MCLOUD-20160610123108719-00035-5421~blub-dev.us.archive.org~9443.warc.gz.open
-rw-r--r-- 1 blub users  162329199 Jun 10 18:11 MCLOUD-20160610150641246-00036-5421~blub-dev.us.archive.org~9443.warc.gz.open
-rw-r--r-- 1 blub users   14747939 Jun 10 18:11 MCLOUD-20160610180030443-00037-5421~blub-dev.us.archive.org~9443.warc.gz.open
```

# Add WARCs to the Archive

First, you need a collection to house your WARCs. If you need a new one,
ask someone (currently Jeff or Alexis) to make one for you. Then edit
`dtmon.cfg` with values for (at least) `crawljob`, `job_dir`,
`xfer_dir`, `description`, `operator`, and `collections`:

``` bash
# dtmon.cfg  - draintasker "simple" config file
#
# * params must begin in col1, so preceding by anything
#   effectively causes the parameter to be ignored
# * this file is read everytime it is needed, so your
#   changes effect existing processes
# * please be verbose in your description_effort
#   required keywords: CRAWLHOST, CRAWLJOB, START_DATE, END_DATE
#
# siznax 2010

crawljob:           blub_test
job_dir:            warcs
xfer_dir:           sink

sleep_time:         300
max_size:           10
# WARC_naming      1 # {TLA}-{timestamp}-{serial}-{fqdn}.warc.gz
WARC_naming:        2 # {TLA}-{timestamp}-{serial}-{PID}~{fqdn}~{port}.warc.gz
block_delay:        120   # blocking
max_block_count:    120   # total blocking time = delay x count
retry_delay:        2400 # non-blocking

# ALL CAPS strings in the description below are substituted:
description:        Internet Archive crawldata from Media Cloud, captured by CRAWLHOST:CRAWLJOB from START_DATE to END_DATE.
 
# Operator's email
operator:           blub@archive.org
 
# These collections need to be precreated:
collections: # may have multiple, each on its own line
  - mediacloud

title_prefix:       Webwide Crawldata
creator:            Internet Archive
sponsor:            Internet Archive
contributor:        Internet Archive
scanningcenter:     sanfrancisco

derive:          1
compact_names:   1# Same as the parent directory:
```

Now run `draintasker` to get your output WARCs into petabox collections.
There is some confusing documentation on draintasker:

[Draintasker  
](https://webarchive.jira.com/wiki/spaces/BOT/pages/4620451/Draintasker+Documentation)[Draintasker
Definitions  
](https://webarchive.jira.com/wiki/spaces/BOT/pages/6423168/Draintasker+Definitions)[Draintasker
Use
Cases](https://webarchive.jira.com/wiki/spaces/BOT/pages/6423170/Draintasker+Use+Cases)[Draintasker
Config](https://webarchive.jira.com/wiki/spaces/BOT/pages/6423157/Draintasker+Config)[Draintasker
Execution](https://webarchive.jira.com/wiki/spaces/BOT/pages/6423161/Draintasker+Execution)[Draintasker
Operations](https://webarchive.jira.com/wiki/spaces/BOT/pages/6423172/Draintasker+Operations)[Draintasker
Processing](https://webarchive.jira.com/wiki/spaces/BOT/pages/6423164/Draintasker+Processing)[Draintasker
Output](https://webarchive.jira.com/wiki/spaces/BOT/pages/6423166/Draintasker+Output)

Some of those docs plus trial and error revealed the following steps.

First, create a `~/.ias3cfg` file. Get the values of` access_key` and
`secret_key` from your `~/.config/internetarchve.yml` file. (Don't use
quotes around the key string values).

``` bash
access_key = ...
secret_key = ...
```

Next:

``` bash
$ cd /1/crawling/blub_test/site
$ touch warcs/DRAINME
$ ../draintasker/dtmon.py -L dtmon.log dtmon.cfg &
```

Files are taken from the `warc` directory and processed into the `sink`
directory.

# Troubleshooting

Input Files

*`blub_test.cxml`* -- heritrix crawl config file  
`dtmod.cfg` – draintasker config file  
`hq-beans.xml` – heritrix ?  
`negative-surts.txt `– surts to avoid crawling, for one reason or
another  
*`seeds.txt `*– URL seed file

Output Files

`negative-surts.dump` --  
`reports/frontier-summary-report.txt` --  
`warcs/*.warc.gz.open` --  
`warcs/*warc.gz`  --

Log Files

`job.log` --  
`logs/alerts.log` --  
`logs/crawl.log` --  
`logs/nonfatal-errors.log` --  
`logs/progress-statistics.log` --  
`logs/runtime-errors.log` --  
`logs/uri-errors.log` --  
  
 

 

## Attachments:

![](images/icons/bullet_blue.gif){width="8" height="8"} [Screen Shot
2016-06-10 at 10.57.46 AM.png](attachments/145326115/145326119.png)
(image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"} [Screen Shot
2016-06-10 at 11.08.21 AM.png](attachments/145326115/145326122.png)
(image/png)  
