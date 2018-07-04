# Basic Crawl Job Settings

-   [Crawl Limits](#BasicCrawlJobSettings-CrawlLimits)
-   [maxToeThreads](#BasicCrawlJobSettings-maxToeThreads)
-   [metadata.operatorContactUrl](#BasicCrawlJobSettings-metadata.operatorContactUrl)
-   [Robots Honoring
    Policy](#BasicCrawlJobSettings-RobotsHonoringPolicy)

Crawl settings are configured by editing a job's
crawler-beans.cxml file.  Each job has a crawler-beans.cxml that
contains the ﻿[Spring](Spring%20Framework) configuration for the job.

# Crawl Limits

In addition to limits imposed on the scope of the crawl it is possible
to enforce arbitrary limits on the duration and extent of the crawl with
the following settings:

-   **maxBytesDownload** - Stop the crawl after a fixed number of bytes
    have been downloaded.  Zero means unlimited.
-   **maxDocumentDownload** - Stop the crawl after downloading a fixed
    number of documents.  Zero means unlimited.
-   **maxTimeSeconds**- Stop the crawl after a certain number of seconds
    have elapsed.  Zero means unlimited.  For reference there are 3600
    seconds in an hour and 86400 seconds in a day.

To set these values modify the CrawlLimitEnforcer bean.

``` xml
<bean id="crawlLimitEnforcer" class="org.archive.crawler.framework.CrawlLimitEnforcer">
<property name="maxBytesDownload" value="100000000" />
<property name="maxDocumentsDownload" value="100" />
<property name="maxTimeSeconds" value="10000" />
</bean>
```

**Note**

-   These are not hard limits. Once one of these limits is hit it will
    trigger a graceful termination of the crawl job. URIs already being
    crawled will be completed.  As a result the set limit will be
    exceeded by some amount.

# maxToeThreads

The maximum number of toe threads to run. 

If running a domain crawl smaller than 100 hosts, a value approximately
twice the number of hosts should be enough. Values larger then 150-200
are rarely worthwhile unless running on machines with exceptional
resources.

``` xml
<bean id="crawlController" class="org.archive.crawler.framework.CrawlController">
<property name="maxToeThreads" value="50" />
</bean>
```

# metadata.operatorContactUrl

The URI of the crawl initiator.  This setting gives the administrator of
a crawled host a URI to refer to in case of problems.

``` xml
<bean id="simpleOverrides" class="org.springframework.beans.factory.config.PropertyOverrideConfigurer">


<property name="properties">


<value>


   1. This Properties map is specified in the Java 'property list' text format
   2. http://java.sun.com/javase/6/docs/api/java/util/Properties.html#load%28java.io.Reader%29


metadata.operatorContactUrl=http://www.archive.org
metadata.jobName=basic
metadata.description=Basic crawl starting with useful defaults


##..more?..##


</value>
</property>
</bean>
```

# Robots Honoring Policy

1.  **CLASSIC** - Obey all robots.txt rules for the configured
    user-agent.
2.  **IGNORE** - Ignore all robots.txt rules.
3.  **CUSTOM** - Defer to a custom-robots setting.
4.  **MOST\_FAVORED** - Crawl URIs if robots.txt allows any user-agent
    to crawl it.
5.  **MOST\_FAVORED\_SET**- Requires that a set of alternate user-agents
    be supplied.  For each page, if any agent in the set is allowed, the
    page will be crawled.

``` xml
<bean id="robotsHonoringPolicy" class="org.archive.modules.net.RobotsHonoringPolicy">
  <property name="type" value="CLASSIC"/>
</bean>
```

Choosing options 3-5 requires additional settings information.

As of Hertrix 3.1 the robots honoring policy can be set on the
"metadata" bean using the "robotsPolicyName" property.

``` xml
<bean id="metadata" class="org.archive.modules.CrawlMetadata" autowire="byName">
...
    <property name="robotsPolicyName" value="obey"/>
...
</bean>
```

The valid values of "robotsPolicyName" are:

-   obey - Obey robots.txt directives
-   classic - Same as "obey"
-   ignore - Ignore robots.txt directives

The robots honoring policy can also be set by creating a bean that uses
one of the following classes.  The bean must be linked to the "metadata"
bean.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Class Name</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>org.archive.modules.net.FirstNamedRobotsPolicy</p></td>
<td><p>Use an ordered list of User-Agents.  The first User-Agent in the list is the regularly configured User-Agent.  The other User-Agents in the list are those configured in the candidateUserAgents list.  As soon as a matching set of directives is found, these directives are followed.  If none are found, the wildcard directives are used if they exist.<br />
</p></td>
</tr>
<tr class="even">
<td><p>org.archive.modules.net.IgnoreRobotsPolicy<br />
</p></td>
<td><p>Ignore robots.txt directives</p></td>
</tr>
<tr class="odd">
<td><p>org.archive.modules.net.ObeyRobotsPolicy<br />
</p></td>
<td><p>Obey robots.txt directives</p></td>
</tr>
<tr class="even">
<td><p>org.archive.modules.net.CustomRobotsPolicy</p></td>
<td><p>Follow a custom-written robots policy rather than the site's own declarations</p></td>
</tr>
<tr class="odd">
<td><p>org.archive.modules.net.MostFavoredRobotsPolicy</p></td>
<td><p>Follow a most-favored robots policy that allows a URI to be crawled if either the conventionally-configured User-Agent, or any number of alternate User-Agents, are allowed.<br />
</p></td>
</tr>
</tbody>
</table>

The example below shows the use of
the org.archive.modules.net.IgnoreRobotsPolicy policy.

``` xml
<bean id="ignorePolicy" class="org.archive.modules.net.IgnoreRobotsPolicy">
</bean>


<bean id="metadata" class="org.archive.modules.CrawlMetadata" autowire="byName">

        <property name="robotsPolicyName"> <ref bean="ignorePolicy"/> </property>

</bean>
```

Also, as of Heritrix 3.1, robots.txt parsing now tolerates trailing
wildcards in Disallow directives, which is a common deviation from the
original standard.  The wildcard is equivalent to the same path-prefix
without the trailing wildcard.  Also, the handling of overlapping
'Allow' and 'Disallow' directives matches the likely intuitive
understanding of webmasters' and other crawlers.  The more
specific/longer-in-length directives take precedence.
