# Sheets

Sheets provide the ability to replace default settings on a per domain
basis.  Sheets are collections of overrides.  They contain alternative
values for object properties that should apply in certain contexts.  The
target is specified as an arbitrarily-long property-path, which is a
string describing how to access the property starting from a beanName in
a BeanFactory.

Sheets allow settings to be overlaid with new values that apply by top
level domains (com, net, org, etc), by second-level domains (yahoo.com,
archive.org, etc.), by subdomains (crawler.archive.org,
tech.groups.yahoo.com, etc.), and leading URI paths
(directory.google.com/Top/Computers/, etc.). There is no limit for how
long the domain/path prefix which specifies overlays can go; the [SURT
Prefix](Glossary_5735753.html#Glossary-Glossary-SURTPrefix) syntax is
used.

Creating a new sheet involves configuring the `crawler-beans.cxml` file,
which contains the Spring configuration of a job. 

For example, if you have explicit permission to crawl certain domains
without the usual polite rate-limiting, then a Sheet can be used to
create a less polite crawling policy that is associated with a few such
target domains.  The configuration of such a Sheet for the domains
example.com and example1.com are shown below. This example allows up to
5 parallel outstanding requests at a time (rather than the default 1),
and eliminates any usual pauses between requests

**Important note:** Unless a target site has given you explicit
permission to crawl extra-aggressively, the typical Heritrix defaults,
which limit the crawler to no more than one outstanding request at a
time, with multiple-second waits between requests, and longer waits when
the site is responding more slowly, are the safest course. Less-polite
crawling can result in your crawler being blocked entirely by
webmasters. Finally, even with permission, be sure your crawler's
User-Agent string includes a link to valid crawl-operator contact
information so you can be alerted to, and correct, any unintended
side-effects.

``` xml
<!-- SHEETOVERLAYMANAGER: manager of sheets of contextual overlays
Autowired to include any SheetForSurtPrefix or
SheetForDecideRuled beans -->
<bean id="sheetOverlaysManager" autowire="byType"
class="org.archive.crawler.spring.SheetOverlaysManager">
</bean>


<bean class='org.archive.crawler.spring.SurtPrefixesSheetAssociation'>
<property name='surtPrefixes'>
<list>
<value>
http://(com,example,www,)/
</value>
<value>
http://(com,example1,www,)/
</value>
</list>
</property>
<property name='targetSheetNames'>
<list>
<value>lessPolite</value>
</list>
</property>
</bean>


<bean id='lessPolite' class='org.archive.spring.Sheet'>
<property name='map'>
<map>
<entry key='disposition.delayFactor' value='0.0'/>
<entry key='disposition.maxDelayMs' value='0'/>
<entry key='disposition.minDelayMs' value='0'/>
<entry key='queueAssignmentPolicy.parallelQueues' value='5'/>
</map>
</property>
</bean>
```

The Sheet named `lessPolite` in the example defines overlays for various
politeness properties.  The Sheet is associated with domains by adding a
`org.archive.crawler.spring.SurtPrefixesSheetAssociation` bean.  This
bean contains the domains for which the overlays will be applied.

The performance penalty for using overlays is minor, as extra steps
early in URI processing decorate the URI with all applicable overlays at
once.
