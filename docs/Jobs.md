# Jobs

A job (sometimes referred to as a crawl job) is a configuration that
defines the way a crawl is executed.  A job contains information such as
the seeds to crawl, the operator's email address, and other
configuration information that determines how seed data is accessed and
stored.  A crawl is an executed instance of a job.  

In Heritrix, a job is based on the Spring Framework.  Spring beans
represent the attributes of a job.  The snippet below shows a Spring
bean that is part of a job configuration (Spring beans are defined in
XML format).  The bean has a property that is set to the URIs of the
seeds to crawl.

``` xml
<bean id="longerOverrides" class="org.springframework.beans.factory.config.PropertyOverrideConfigurer">
<property name="properties">
<props>
      <prop key="seeds.textSource.value"># URLS HERE http://example.example/example</prop>
</props>
</property>
</bean>
```
