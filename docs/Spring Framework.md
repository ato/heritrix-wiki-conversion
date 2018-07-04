# Spring Framework

The Heritrix software is based on the
[Spring](http://www.springsource.org/) Java framework.  The Spring
framework defines a construct called a bean.  A bean is a configurable
component that consists of properties (such as the email address of the
Heritrix operator) and references to other beans. Configuring Heritrix
is accomplished by configuring beans.  A bean is represented as an XML
element in the Spring configuration files.  An example of a bean is
shown below.

**fetchProcessors Spring Bean**

``` xml
<bean id="fetchProcessors" class="org.archive.modules.FetchChain">
<property name="processors">
<list>
<!-- re-check scope, if so enabled... -->
<ref bean="preselector"/>
<!--
...then verify or trigger prerequisite URIs fetched, allow crawling...
-->
<ref bean="preconditions"/>
<!-- ...fetch if DNS URI... -->
<ref bean="fetchDns"/>
<!-- <ref bean="fetchWhois"/> -->
<!-- ...fetch if HTTP URI... -->
<ref bean="fetchHttp"/>
<!-- ...extract outlinks from HTTP headers... -->
<ref bean="extractorHttp"/>
<!-- ...extract outlinks from HTML content... -->
<ref bean="extractorHtml"/>
<!-- ...extract outlinks from CSS content... -->
<ref bean="extractorCss"/>
<!-- ...extract outlinks from Javascript content... -->
<ref bean="extractorJs"/>
<!-- ...extract outlinks from Flash content... -->
<ref bean="extractorSwf"/>
</list>
</property>
</bean>
```

This bean consists of an unique identifier (fetchProcessors) and a list
of properties that are references to other beans.  An example of a
configuration change would be to place the XML extractor bean ahead of
the HTTP extractor bean so that content such as RSS feeds can be
crawled.  The fetchProcessors bean after this configuration change is
shown below.

**fetchProcessors Bean with extractorXML**

``` xml
<bean id="fetchProcessors" class="org.archive.modules.FetchChain">
<property name="processors">
<list>
<!-- re-check scope, if so enabled... -->
<ref bean="preselector"/>
<!--
...then verify or trigger prerequisite URIs fetched, allow crawling...
-->
<ref bean="preconditions"/>
<!-- ...fetch if DNS URI... -->
<ref bean="fetchDns"/>
<!-- <ref bean="fetchWhois"/> -->
<!-- ...fetch if HTTP URI... -->
<ref bean="fetchHttp"/>
<!-- ...extract outlinks from HTTP headers... -->
<ref bean="extractorHttp"/>
<!-- ...extract outlinks from XML... -->
<ref bean="extractorXML"/>
<!-- ...extract outlinks from HTML content... -->
<ref bean="extractorHtml"/>
<!-- ...extract outlinks from CSS content... -->
<ref bean="extractorCss"/>
<!-- ...extract outlinks from Javascript content... -->
<ref bean="extractorJs"/>
<!-- ...extract outlinks from Flash content... -->
<ref bean="extractorSwf"/>
</list>
</property>
</bean>
```
