# Avoiding False Requests When Processing Certain Types of Content

As of Heritrix 3.1, improvements have been made to the crawler's ability
to determine if a string is a valid URI.  These improvements can provide
better link extraction from content such as unparsed/uninterpreted
Javascript. However, this technique can be error-prone, causing problems
or annoyance on target Web sites.  This functionality can be disabled in
Heritrix 3.1 for a full crawl or on a site-by-site basis.  To disable
remove the "extractorJs" bean reference from the "fetchProcessors" bean
and set the "extractionHtml" bean's "extractJavascript" and
"extractValueAttributes" properties to false.

1.  Remove the "fetchProcessors" bean's reference to "extractorJs".
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
    <!-- ****** <ref bean="extractorJs"/> ****** -->
    <!-- ...extract outlinks from Flash content... -->
    <ref bean="extractorSwf"/>
    </list>
    </property>
    </bean>
    ```

2.  Set the "extractionHtml" bean's "extractJS" and
    "extractValueAttributes" settings to false.
    ``` xml
    <bean id="extractorHtml" class="org.archive.modules.extractor.ExtractorHTML">
    <property name="extractJavascript" value="false" />
    <property name="extractValueAttributes" value="false" />
    </bean>
    ```
