# Multiple Machine Crawling

Multi-machine crawls can be performed using the hashCrawlMapper to
assign URIs to different machines based on their hostnames.

First add the following bean:

``` bash
<bean id="hashCrawlMapper">
         <property name="enabled" value="true" />
         <property name="localName" value="0" />
         <property name="diversionDir" value="diversions" />
         <property name="checkUri" value="true" />
         <property name="checkOutlinks" value="false"/>
         <property name="rotationDigits" value="10" />

         <!-- Number of crawlers being used in the multi-machine setup-->
         <property name="crawlerCount" value="7" />
 </bean>
```

Call the bean in the CandidateProcessor's chain:

``` bash
<bean id="candidateProcessors">
  <property name="processors">
   <list>
<!-- apply scoping rules to each individual candidate URI... -->
 <ref bean="candidateScoper"/>
<!-- Check URIs for crawler assignment -->
 <ref bean="hashCrawlMapper"/>
```

All crawlers will receive the same initial list of seeds. The only value
which should change between different crawlers is "localName".

When the crawl starts, the "diversions" directory will start to fill
with .divert files. Each .divert file will be named
$timestamp-$localname\_currentmachine-to-$localname\_assignedmachine.

Crawl operators must set up a process where the the URIs contained in
.divert files are copied from each crawler to their assigned crawlers
and queued into the active crawl. For example, converting the .divert
file into the format expected by the action directory as a .schedule
file would be sufficient.
