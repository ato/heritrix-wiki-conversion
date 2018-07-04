# Configuring Jobs and Profiles

Creating crawl jobs ([Creating a
Job](https://webarchive.jira.com/wiki/display/Heritrix/Creating+a+Job))
and profiles ([Creating a
Profile](https://webarchive.jira.com/wiki/display/Heritrix/Creating+a+Profile))
is the first step in the process of using Heritrix to crawl the Web. 
Configuring jobs and profiles is a more complicated process.  The
following section applies equally to configuring crawl jobs and
profiles.

**Note**

-   To edit a running crawl see [Editing a Running a
    Job](https://webarchive.jira.com/wiki/display/Heritrix/Editing+a+Running+Job)
    for more information.

Configuring a job or profile involves editing the `crawler-beans.cxml`
file.  This file is a [Spring](http://www.springsource.org/)
configuration file.  The Spring framework is used to define the
properties of jobs and profiles.  Each job is defined by Spring "beans"
that hold configuration data for the job.  This section covers
configuring common properties of a crawl job or profile and describes
the various sections of the `crawler-beans.cxml` file.

The first section of the `crawler-beans.cxml` file allows the operator
to override any simple bean property, such as
`metadata.operatorContactUrl`.  For example, you could set Heritrix to
ignore cookies with the following configuration override.

**Override Ignore Cookies Property**

``` xml
<!-- overrides from a text property list -->
<bean id="simpleOverrides" class="org.springframework.beans.factory.config.PropertyOverrideConfigurer">
<property name="properties">
<value>

# This Properties map is specified in the Java 'property list' text format
# http://java.sun.com/javase/6/docs/api/java/util/Properties.html#load%28java.io.Reader%29

metadata.operatorContactUrl=http://www.archive.org
metadata.jobName=basic
metadata.description=Basic crawl starting with useful defaults
ignoreCookies=true

##..more?..##

</value>
</property>
</bean>
```

For longer or more complicated overrides, the "longerOverrides" bean is
available.  It is used to override properties that have multiple values
or that can be overridden with a bean.  For example, you could configure
multiple seeds with the following configuration.

**Overriding seed values**

``` xml
<bean id="longerOverrides" class="org.springframework.beans.factory.config.PropertyOverrideConfigurer">

<property name="properties">

<props>
<prop key="seeds.textSource.value">

# URLS HERE
http://www.myhost1.net
http://www.myhost2.net
http://www.myhost3.net/pictures

    </prop>
</props>
</property>
</bean>
```
