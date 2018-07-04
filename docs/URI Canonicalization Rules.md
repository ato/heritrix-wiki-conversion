# URI Canonicalization Rules

Heritrix keeps track of duplicate URIs so it does not crawl redundant
content.  However, URIs can be composed in multiple ways even though the
page pointed to by the URIs is identical.  For example, the page
http://www.archive.org/index.html is the same page as
http://WWW.ARCHIVE.ORG. To address this issue, Heritrix canonicalizes
URIs before they are compared for de-duplication.  Canonicalization
involves the application of a series of rules.  For example, one
canonicalization rule transforms all URIs to lowercase.  Another rule
strips the 'www' prefix from domains.

The `canonicalizationPolicy` bean allows you to specify canonicalization
rules and the order in which they are run.

To log the canonicalization process, add the line:

    org.archive.modules.canonicalize.RulesCanonicalizationPolicy.level = FINER

to `conf/logging.properties`.

Canonicalization rules are NOT run if the URI being checked is the
result of a redirect.  This is done for the following reason.  Assume a
canonicalization rule is in place that equates http://www.archive.org to
http://archive.org.  If the crawler encounters http://archive.org, but
the server at archive.org re-directs it to http://www.archive.org/,
Heritrix will think http://www.archive.org has already been crawled. 
This problem is avoided by ignoring canonicalization rules for
re-directs.

 

Changing URI Canonicalization affects Wayback too

Please note that, if you decide to modify the URI Canonicalisation
rules, this can also affect the playback experience. You should ensure
the Wayback and Heritrix configurations are consistent, otherwise the
Wayback engine may not be able to resolve the URLs in the web pages to
the corresponding canonicalized resource.

 

###### URI Canonicalization Rule Use Case: Stripping Site Specific Session Ids

In this use case we assume a site is returning URIs with a session ID
key of cid.  For example, .  Assume the session id is always 32
characters.  Also, assume, the cid always appears at the end of the
URI.  This presents a problem because the same URI will be repeatedly
captured due to the different session ids.

The solution is to add a second URI canonicalization policy derived from
the default.  The new policy will include a regular expression rule that
filters out the session id.  This rule is then attached to a sheet
overlay.  A sheet overlay is a way to override properties of beans based
on different sets of values.  The sheet overlay that is created will be
configured so that it only applies to URIs with a specific domain.  The
example below shows the Spring configuration used to achieve this
effect.

This is already in the default cxml:

``` xml
 <!-- SHEETOVERLAYMANAGER: manager of sheets of contextual overlays
      Autowired to include any SheetForSurtPrefix or
      SheetForDecideRuled beans -->
 <bean id="sheetOverlaysManager" autowire="byType"
  class="org.archive.crawler.spring.SheetOverlaysManager">
 </bean>
```

This is commented out in the default cxml, and needs to be uncommented:

``` xml
 <!-- CANONICALIZATION POLICY -->
 <bean id="canonicalizationPolicy"
  class="org.archive.modules.canonicalize.RulesCanonicalizationPolicy">
  <property name="rules">
   <list>
    <bean class="org.archive.modules.canonicalize.LowercaseRule" />
    <bean class="org.archive.modules.canonicalize.StripUserinfoRule" />
    <bean class="org.archive.modules.canonicalize.StripWWWNRule" />
    <bean class="org.archive.modules.canonicalize.StripSessionIDs" />
    <bean class="org.archive.modules.canonicalize.StripSessionCFIDs" />
    <bean class="org.archive.modules.canonicalize.FixupQueryString" />
   </list>
  </property>
 </bean>
```

And something like this needs to be added:

``` xml
 <bean id="altCanonicalizationPolicy"
  class="org.archive.modules.canonicalize.RulesCanonicalizationPolicy"
  parent="canonicalizationPolicy" autowire-candidate="false">
  <property name="rules">
   <list merge="true">
    <bean class="org.archive.modules.canonicalize.RegexRule">
     <property name="regex" value="^(.+)(?:cid=0-9a-zA-Z{32})?$"/>
    </bean>
   </list>
  </property>
 </bean>

 <bean class='org.archive.crawler.spring.SurtPrefixesSheetAssociation'>
  <property name='surtPrefixes'>
   <list>
    <value>http://(z,y,</value>
   </list>
  </property>
  <property name='targetSheetNames'>
   <list>
    <value>canonicalizationPolicySheet</value>
   </list>
  </property>
 </bean>
 
 <bean id='canonicalizationPolicySheet' class='org.archive.spring.Sheet'>
  <property name='map'>
   <map>
    <entry key='preparer.canonicalizationPolicy'>
     <ref bean='altCanonicalizationPolicy'/>
    </entry>
   </map>
  </property>
 </bean>
```

To see the rule in operation, set the logging level for
`org.archive.crawler.url.Canonicalizer` in `logging.properties`.  Study
the output and adjust your regex accordingly.
