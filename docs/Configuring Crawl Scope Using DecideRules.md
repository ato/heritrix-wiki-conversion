# Configuring Crawl Scope Using DecideRules

The crawl scope defines the set of possible URIs that can be captured by
a crawl.  These URIs are determined by DecideRules, which work in
combination to limit or expand the set of crawled URIs.  Each
DecideRule, when presented with an object (most often a URI of some
form) responds with one of three decisions:

-   ACCEPT: the object is ruled in
-   REJECT: the object is ruled out
-   PASS: the rule has no opinion; retain the previous decision

A URI under consideration begins with no assumed status.  Each rule is
applied in turn to the candidate URI.  If the rule decides ACCEPT or
REJECT, the URI's status is set accordingly.  After all rules have been
applied, the URI is determined to be "in scope" if its status is
ACCEPT.  If its status is REJECT it is discarded.

We suggest starting with the rules in our recommended default
configurations and performing small test crawls with those rules.
Understand why certain URIs are ruled in or ruled out under those rules.
Then make small individual changes to the scope to achieve non-default
desired effects. Creating a new ruleset from scratch can be difficult
and can easily result in crawls that can't make the usual minimal
progress that other parts of the crawler expect. Similarly, making many
changes at once can obscure the importance of the interplay and ordering
of the rules.

### DecideRules

The following table lists the available DecideRules.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Decide Rule</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>AcceptDecideRule</p></td>
<td><p>This DecideRule accepts any URI.</p></td>
</tr>
<tr class="even">
<td><p>ContentLengthDecideRule</p></td>
<td><p>This DecideRule accepts a URI if the content-length is less than the threshold.  The default threshold is 2^63, meaning any document will be accepted.</p></td>
</tr>
<tr class="odd">
<td><p>PathologicalPathDecideRule</p></td>
<td><p>This DecideRule rejects any URI that contains an excessive number of identical, consecutive path-segments.  For example, <br />
http://example.com/a/a/a/a/a/foo.html.</p></td>
</tr>
<tr class="even">
<td><p>PredicatedDecideRule</p></td>
<td><p>This DecideRule applies a configured decision only if a test evaluates to true.</p></td>
</tr>
<tr class="odd">
<td><p>ExternalGeoLocationDecideRule</p></td>
<td><p>This DecideRule accepts a URI if it is located in a particular country.</p></td>
</tr>
<tr class="even">
<td><p>FetchStatusDecideRule</p></td>
<td><p>This DecideRule applies the configured decision to any URI that has a fetch staus equal to the &quot;target-status&quot; setting.</p></td>
</tr>
<tr class="odd">
<td><p>HasViaDecideRule</p></td>
<td><p>This DecideRule applies the configured decision to any URI that has a &quot;via.&quot;  A via is any URI that is a seed or some kind of mid-crawl addition.</p></td>
</tr>
<tr class="even">
<td><p>HopCrossesAssignmentLevelDomainDecideRule</p></td>
<td><p>This DecideRule applies the configured decision to any URI that differs in the portion of its hostname/domain that is assigned/sold by registrars.  The portion is referred to as the &quot;assignment-level-domain&quot; (ALD).</p></td>
</tr>
<tr class="odd">
<td><p>IdenticalDigestDecideRule</p></td>
<td><p>This DecideRule applies the configured decision to any URI whose prior-history content-digest matches the latest fetch.</p></td>
</tr>
<tr class="even">
<td><p>MatchesListRegexDecideRule</p></td>
<td><p>This DecideRule applies the configured decision to any URI that matches the supplied regular expressions.</p></td>
</tr>
<tr class="odd">
<td><p>NotMatchesListRegexDecideRule</p></td>
<td><p>This DecideRule applies the configured decision to any URI that does not match the supplied regular expressions.</p></td>
</tr>
<tr class="even">
<td><p>MatchesRegexDecideRule</p></td>
<td><p>This DecideRule applies the configured decision to any URI that matches the supplied regular expression.</p></td>
</tr>
<tr class="odd">
<td><p>ClassKeyMatchesRegexDecideRule</p></td>
<td><p>This DecideRule applies the configured decision to any URI class key that matches the supplied regular expression.  A URI class key is a string that specifies the name of the Frontier queue into which a URI should be placed.</p></td>
</tr>
<tr class="even">
<td><p>ContentTypeMatchesRegexDecideRule</p></td>
<td><p>This DecideRule applies the configured decision to any URI whose content-type is present and matches the supplied regular expression.</p></td>
</tr>
<tr class="odd">
<td><p>ContentTypeNotMatchesRegexDecideRule</p></td>
<td><p>This DecideRule applies the configured decision to any URI whose content-type does not match the supplied regular expression.</p></td>
</tr>
<tr class="even">
<td><p>FetchStatusMatchesRegexDecideRule</p></td>
<td><p>This DecideRule applies the configured decision to any URI that has a fetch status that matches the supplied regular expression.</p></td>
</tr>
<tr class="odd">
<td><p>FetchStatusNotMatchesRegexDecideRule</p></td>
<td><p>This DecideRule applies the configured decision to any URI that has a fetch status that does not match the suppllied regular expression.</p></td>
</tr>
<tr class="even">
<td><p>HopsPathMatchesRegexDecideRule</p></td>
<td><p>This DecideRule applies the configured decision to any URI whose &quot;hops-path&quot; matches the supplied regular expression.  The hops-path is a string that consists of characters representing the path that was taken to access the URI.  An example of a hops-path is &quot;LLXE&quot;.</p></td>
</tr>
<tr class="odd">
<td><p>MatchesFilePatternDecideRule</p></td>
<td><p>This DecideRule applies the configured decision to any URI whose suffix matches the supplied regular expression.</p></td>
</tr>
<tr class="even">
<td><p>NotMatchesFilePatternDecideRule</p></td>
<td><p>This DecideRule applies the configured decision to any URI whose suffix does not match the supplied regular expression.</p></td>
</tr>
<tr class="odd">
<td><p>NotMatchesRegexDecideRule</p></td>
<td><p>This DecideRule applies the configured decision to any URI that does not match the supplied regular expression.</p></td>
</tr>
<tr class="even">
<td><p>NotExceedsDocumentLengthThresholdDecideRule</p></td>
<td><p>This DecideRule applies the configured decision to any URI whose content-length does not exceed the configured threshold.  The content-length comes from either the HTTP header or the actual downloaded content length of the URI.  As of Heritrix 3.1, this rule has been renamed to ResourceNoLongerThanDecideRule.</p></td>
</tr>
<tr class="odd">
<td><p>ExceedsDocumentLengthThresholdDecideRule</p></td>
<td><p>This DecideRule applies the configured decision to any URI whose content length exceeds the configured threshold.  The content-length comes from either the HTTP header or the actual downloaded content length of the URI.  As of Heritrix 3.1, this rule has been renamed to ResourceLongerThanDecideRule.</p></td>
</tr>
<tr class="even">
<td><p>SurtPrefixedDecideRule</p></td>
<td><p>This DecideRule applies the configured decision to any URI (expressed in SURT form) that begins with one of the prefixes in the configured set. This DecideRule returns true when the prefix of a given URI matches any of the listed SURTs. The list of SURTs may be configured in different ways: the surtsSourceFile parameter specifies a file to read the SURTs list from.  If seedsAsSurtPrefixes parameter is set to true, SurtPrefixedDecideRule adds all seeds to the SURTs list. If alsoCheckVia property is set to true (default false), SurtPrefixedDecideRule will also consider Via URIs in the match.<br />
As of Heritrix 3.1, the &quot;surtsSource&quot; parameter may be any ReadSource, such as a ConfigFile or a ConfigString.  This gives the SurtPrefixedDecideRule the flexibility of the TextSeedModule bean's &quot;textSource&quot; property.</p></td>
</tr>
<tr class="odd">
<td><p>NotSurtPrefixedDecideRule</p></td>
<td><p>This DecideRule applies the configured decision to any URI (expressed in SURT form) that does not begin with one of the prefixes in the configured set.</p></td>
</tr>
<tr class="even">
<td><p>OnDomainsDecideRule</p></td>
<td><p>This DecideRule applies the configured decision to any URI that is in one of the domains of the configured set.</p></td>
</tr>
<tr class="odd">
<td><p>NotOnDomainsDecideRule</p></td>
<td><p>This DecideRule applies the configured decision to any URI that is not in one of the domains of the configured set.</p></td>
</tr>
<tr class="even">
<td><p>OnHostsDecideRule</p></td>
<td><p>This DecideRule applies the configured decision to any URI that is in one of the hosts of the configured set.</p></td>
</tr>
<tr class="odd">
<td><p>NotOnHostsDecideRule</p></td>
<td><p>This DecideRule applies the configured decision to any URI that is not in one of the hosts of the configured set.</p></td>
</tr>
<tr class="even">
<td><p>ScopePlusOneDecideRule</p></td>
<td><p>This DecideRule applies the configured decision to any URI that is one level beyond the configured scope.</p></td>
</tr>
<tr class="odd">
<td><p>TooManyHopsDecideRule</p></td>
<td><p>This DecideRule rejects any URI whose total number of hops is over the configured threshold.</p></td>
</tr>
<tr class="even">
<td><p>TooManyPathSegmentsDecideRule</p></td>
<td><p>This DecideRule rejects any URI whose total number of path-segments is over the configured threshold.  A path-segment is a string in the URI separated by a &quot;/&quot; character, not including the first &quot;//&quot;.</p></td>
</tr>
<tr class="odd">
<td><p>TransclusionDecideRule</p></td>
<td><p>This DecideRule accepts any URI whose path-from-seed ends in at least one non-navlink hop. A navlink hop is represented by an &quot;L&quot;.  Also, the number of non-navlink hops in the path-from-seed cannot exceed the configured value.</p></td>
</tr>
<tr class="even">
<td><p>PrerequisiteAcceptsDecideRule</p></td>
<td><p>This DecideRule accepts all &quot;prerequisite&quot; URIs.  Prerequisite URIs are those whose hops-path has a &quot;P&quot; in the last position.</p></td>
</tr>
<tr class="odd">
<td><p>RejectDecideRule</p></td>
<td><p>This DecideRule rejects any URI.</p></td>
</tr>
<tr class="even">
<td><p>ScriptedDecideRule</p></td>
<td><p>This DecideRule applies the configured decision to any URI that passes the rules test of a <a href="http://jcp.org/en/jsr/proposalDetails?id=223">JSR-223</a> script.  The script source must be a one-argument function called <code>decisionFor</code>.&quot;  The function returns the appropriate DecideResult.  Variables available to the script include <code>object</code> (the object to be evaluated, such as a URI), &quot;self&quot; (the <code>ScriptDecideRule</code> instance), and <code>context</code> (the crawl's <code>ApplicationContext</code>, from which all named crawl beans are reachable).</p></td>
</tr>
<tr class="odd">
<td><p>SeedAcceptDecideRule</p></td>
<td><p>This DecideRule accepts all &quot;seed&quot; URIs (those for which isSeed is true).</p></td>
</tr>
</tbody>
</table>

DecideRules are configured by the bean with id "scope" under the
property named "rules."

## DecideRuleSequence Logging

Enable `FINEST` logging on the class
`org.archive.crawler.deciderules.DecideRuleSequence` to watch each
DecideRule's evaluation of the processed URI. This can be done in
the `logging.properties` file

**logging.properties**

``` bash
org.archive.modules.deciderules.DecideRuleSequence.level = FINEST
```

in conjunction with the `-Dsysprop` VM argument,

    -Djava.util.logging.config.file=/path/to/heritrix3/dist/src/main/conf/logging.properties

## scope crawler-bean

The scope bean section of the `crawler-beans.cxml` file is reproduced
below.

``` xml
<bean id="scope" class="org.archive.modules.deciderules.DecideRuleSequence">

<property name="rules">

<list>
<!-- Begin by REJECTing all... -->
<bean class="org.archive.modules.deciderules.RejectDecideRule">
    </bean>

<!--
 ...then ACCEPT those within configured/seed-implied SURT prefixes...
-->

<bean class="org.archive.modules.deciderules.surt.SurtPrefixedDecideRule">

<!--
 <property name="seedsAsSurtPrefixes" value="true" />
-->
<!-- <property name="alsoCheckVia" value="true" /> -->
<!-- <property name="surtsSourceFile" value="" /> -->

<!--
 <property name="surtsDumpFile" value="surts.dump" />
-->
</bean>

<!--
 ...but REJECT those more than a configured link-hop-count from start...
-->

<bean class="org.archive.modules.deciderules.TooManyHopsDecideRule">
<!-- <property name="maxHops" value="20" /> -->
</bean>

<!--
 ...but ACCEPT those more than a configured link-hop-count from start...
-->

<bean class="org.archive.modules.deciderules.TransclusionDecideRule">
<!-- <property name="maxTransHops" value="2" /> -->
<!-- <property name="maxSpeculativeHops" value="1" /> -->
</bean>

<!--
 ...but REJECT those from a configurable (initially empty) set of REJECT SURTs...
-->

<bean class="org.archive.modules.deciderules.surt.SurtPrefixedDecideRule">
<property name="decision" value="REJECT"/>
<property name="seedsAsSurtPrefixes" value="false"/>
<property name="surtsDumpFile" value="negative-surts.dump"/>
<!-- <property name="surtsSourceFile" value="" /> -->
</bean>

<!--
 ...and REJECT those from a configurable (initially empty) set of URI regexes...
-->

<bean class="org.archive.modules.deciderules.MatchesListRegexDecideRule">
<!-- <property name="listLogicalOr" value="true" /> -->

<!--
 <property name="regexList">
           <list>
           </list>
          </property>
-->
</bean>

<!--
 ...and REJECT those with suspicious repeating path-segments...
-->

<bean class="org.archive.modules.deciderules.PathologicalPathDecideRule">
<!-- <property name="maxRepetitions" value="2" /> -->
</bean>

<!--
 ...and REJECT those with more than threshold number of path-segments...
-->

<bean class="org.archive.modules.deciderules.TooManyPathSegmentsDecideRule">
<!-- <property name="maxPathDepth" value="20" /> -->
</bean>

<!--
 ...but always ACCEPT those marked as prerequisitee for another URI...
-->
<bean class="org.archive.modules.deciderules.PrerequisiteAcceptDecideRule">
    </bean>
</list>
</property>
</bean>
```
