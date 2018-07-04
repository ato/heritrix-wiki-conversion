# Facebook and Twitter Scroll-down

Configuration for capturing the stuff that gets loaded when you scroll
past the end of the page on facebook and twitter using the new
[ExtractorMultipleRegex](http://builds.archive.org:8080/javadoc/heritrix-3.x-snapshot/org/archive/modules/extractor/ExtractorMultipleRegex.html)

### Twitter

Configure extractors at top level:

``` xml
        <bean id="extractorTwitterScrollOne" class="org.archive.modules.extractor.ExtractorMultipleRegex">
                <property name="enabled" value="false"/>
                <property name="uriRegex" value="^https?://(?:www\.)?twitter\.com/([^/]+)/?(?:\?.*)?$"/>
                <property name="contentRegexes">
                        <map>
                                <entry key="maxId" value="data-max-id=&quot;(\d+)&quot;"/>
                        </map>
                </property>
                <property name="template">
                        <value>/i/profiles/show/${uriRegex[1]}/timeline/with_replies?include_available_features=1&amp;include_entities=1&amp;max_id=${maxId[1]}</value>
                </property>
        </bean>
        <bean id="extractorTwitterScrollFurther" class="org.archive.modules.extractor.ExtractorMultipleRegex">
                <property name="enabled" value="false"/>
                <property name="uriRegex" value="^https?://(?:www\.)?twitter\.com/i/profiles/show/([^/]+)/timeline/with_replies\?include_available_features=1&amp;include_entities=1&amp;max_id=\d+$"/>
                <property name="contentRegexes">
                        <map>
                                <entry key="maxId" value="&quot;max_id&quot;:&quot;(\d+)&quot;"/>
                        </map>
                </property>
                <property name="template">
                        <value>/i/profiles/show/${uriRegex[1]}/timeline/with_replies?include_available_features=1&amp;include_entities=1&amp;max_id=${maxId[1]}</value>
                </property>
        </bean>
```

Insert into fetch chain:

``` html/xml
                                <ref bean="extractorHtml"/>
                                <ref bean="extractorCss"/>
                                <ref bean="extractorJs"/>
+                                <ref bean="extractorTwitterScrollOne"/>
+                                <ref bean="extractorTwitterScrollFurther"/> 
                        </list>
                </property>
```

Use sheets to enable for relevant urls:

``` xml
        <bean id="twitterScrollOne" class="org.archive.spring.Sheet">
                <property name="map">
                        <map>
                                <entry key="extractorTwitterScrollOne.enabled" value="true"/>
                        </map>
                </property>
        </bean>
        <bean class="org.archive.crawler.spring.SurtPrefixesSheetAssociation">
                <property name="surtPrefixes">
                        <list>
                                <value>http://(com,twitter,)/</value>
                                <value>http://(com,twitter,www,)/</value>
                        </list>
                </property>
                <property name="targetSheetNames">
                        <list>
                                <value>twitterScrollOne</value>
                        </list>
                </property>
        </bean>
        <bean id="twitterScrollFurther" class="org.archive.spring.Sheet">
                <property name="map">
                        <map>
                                <entry key="extractorTwitterScrollFurther.enabled" value="true"/>
                                <entry key="extractorTwitterScrollOne.enabled" value="false"/>
                        </map>
                </property>
        </bean>
        <bean class="org.archive.crawler.spring.SurtPrefixesSheetAssociation">
                <property name="surtPrefixes">
                        <list>
                                <value>http://(com,twitter,)/i/profiles/show/</value>
                                <value>http://(com,twitter,www,)/i/profiles/show/</value>
                        </list>
                </property>
                <property name="targetSheetNames">
                        <list>
                                <value>twitterScrollFurther</value>
                        </list>
                </property>
        </bean>
```

### Facebook

Configure extractor at top level:

``` xml
        <bean id="extractorFacebookScroll" class="org.archive.modules.extractor.ExtractorMultipleRegex">
                <property name="enabled" value="false"/>
                <property name="uriRegex" value="^https?://(?:www\.)?facebook\.com/[^/?]+$"/>
                <property name="contentRegexes">
                        <map>
                                <entry key="jsonBlob" value="\[&quot;TimelineContentLoader&quot;,&quot;registerTimePeriod&quot;,[^,]+,[^,]+,[^,]+,\{(&quot;profile_id&quot;:[^}]+)\},false,null,(\d+),"/>
                                <entry key="ajaxpipeToken" value="&quot;ajaxpipe_token&quot;:&quot;([^&quot;]+)&quot;"/>
                                <entry key="timeCutoff" value="&quot;setTimeCutoff&quot;,[^,]*,\[(\d+)\]\]"/>
                        </map>
                </property>
                <property name="template">
                        <value>/ajax/pagelet/generic.php/ProfileTimelineSectionPagelet?ajaxpipe=1&amp;ajaxpipe_token=${ajaxpipeToken[1]}&amp;no_script_path=1&amp;data=${java.net.URLEncoder.encode('{' + jsonBlob[1] , 'UTF-8')},&quot;time_cutoff&quot;%3A${java.net.URLEncoder.encode(timeCutoff[1] , 'UTF-8')},&quot;force_no_friend_activity&quot;%3Afalse%7D&amp;__user=0&amp;__a=1&amp;__adt=${jsonBlob[2]}</value>
                </property>
        </bean>
```

Insert into fetch chain:

``` xml
                                <ref bean="extractorCss"/>
                                <ref bean="extractorJs"/>
                                <ref bean="extractorTwitterScrollOne"/>
                                <ref bean="extractorTwitterScrollFurther"/>
+                                <ref bean="extractorFacebookScroll"/>
                        </list>
                </property>
```

Use sheets to enable for relevant urls:

``` xml
        <bean id="enableFacebookScroll" class="org.archive.spring.Sheet">
                <property name="map">
                        <map>
                                <entry key="extractorFacebookScroll.enabled" value="true"/>
                        </map>
                </property>
        </bean>
        <bean class="org.archive.crawler.spring.SurtPrefixesSheetAssociation">
                <property name="surtPrefixes">
                        <list>
                                <value>http://(com,facebook,</value>
                        </list>
                </property>
                <property name="targetSheetNames">
                        <list>
                                <value>enableFacebookScroll</value>
                        </list>
                </property>
        </bean>
```
