# Fetch Chain Processors

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Processor Name<br />
</p></th>
<th><p>Description<br />
</p></th>
<th><p>Class Name</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>preparer<br />
</p></td>
<td><p>This processor prepares ACCEPTed URIs for enqueing in the Frontier.  It is run again to recheck the scope of URIs before fetching begins.<br />
</p></td>
<td><p> </p></td>
</tr>
<tr class="even">
<td><p>preconditions<br />
</p></td>
<td><p>This processor verifies or triggers the fetching of prerequisite URIs.<br />
</p></td>
<td><p> </p></td>
</tr>
<tr class="odd">
<td><p>fetchDns<br />
</p></td>
<td><p>This processor fetches DNS URIs.<br />
</p></td>
<td><p> </p></td>
</tr>
<tr class="even">
<td><p>fetchHttp<br />
</p></td>
<td><p>This processor fetches HTTP URIs.  As of Heritrix 3.1, the crawler will now properly decode 'chunked' Transfer-Encoding -- even if encountered when it should not be used, as in a response to an HTTP/1.0 request. Additionally, the fetchHttp processor now includes the parameter 'useHTTP11', which if true, will cause Heritrix to report its requests as 'HTTP/1.1'.  This allows sites to use the 'chunked' Transfer-Encoding. (The default for this parameter is false for now, and Heritrix still does not reuse a persistent connection for more than one request to a site.)<br />
fetchHttp also includes the parameter 'acceptCompression', which if true, will cause Heritrix requests to include an &quot;Accept-Encoding: gzip,deflate&quot; header, which offers to receive compressed responses. (The default for this parameter is false for now.)</p></td>
<td><p> </p></td>
</tr>
<tr class="odd">
<td><p>extractorHttp<br />
</p></td>
<td><p>This processor extracts outlinks from HTTP headers.  As of Heritrix 3.1, the extractorHttp processor now considers any URI on a hostname to imply that the '/favicon.ico' from the same host should be fetched.  Also, as of Heritrix 3.1, the &quot;inferRootPage&quot; property has been added to the extractorHttp bean.  If this property is &quot;true&quot;, Heritrix infers the '/' root page from any other URI on the same hostname.  The default for this setting is &quot;false&quot;, which means the pre-3.1 behavior of only fetching the root page if it is a seed or otherwise discovered and in-scope remains in effect. Discovery via these new heuristics is considered to be a new 'I' (inferred) hop-type, and is treated the same in scoping/transclusion decisions as an 'E' (embed).<br />
</p></td>
<td><p>org.archive.modules.extractor.ExtractorHTTP</p></td>
</tr>
<tr class="even">
<td><p>extractorHtml<br />
</p></td>
<td><p>This processor extracts outlinks from HTML content.<br />
</p></td>
<td><p>org.archive.modules.extractor.ExtractorHTML</p></td>
</tr>
<tr class="odd">
<td><p>extractorCss<br />
</p></td>
<td><p>This processor extracts outlinks from CSS content.<br />
</p></td>
<td><p>org.archive.modules.extractor.ExtractorCSS</p></td>
</tr>
<tr class="even">
<td><p>extractorJs<br />
</p></td>
<td><p>This processor extracts outlinks from JavaScript content.<br />
</p></td>
<td><p>org.archive.modules.extractor.ExtractorJs</p></td>
</tr>
<tr class="odd">
<td><p>extractorSwf<br />
</p></td>
<td><p>This processor extracts outlinks from Flash content.</p></td>
<td><p>org.archive.modules.extractor.ExtractorSWF</p></td>
</tr>
<tr class="even">
<td><p>extractorPdf</p></td>
<td><p>This processor extracts outlinks from PDF content.</p></td>
<td><p>org.archive.modules.extractor.ExtractorPDF</p></td>
</tr>
<tr class="odd">
<td><p>extractorXml</p></td>
<td><p>This processor extracts outlinks from XML content.</p></td>
<td><p>org.archive.modules.extractor.ExtractorXML</p></td>
</tr>
</tbody>
</table>

Most extract processors are pre-fconfigured in a job's
`crawler-beans.cxml` configuration file under the "fetchProcessors"
bean. To add a new extractor, such as an XML/RSS extractor, define the
bean and then link it to the "fetchProcessors" bean. An example for the
extractorXml bean is below.

1.  Define the bean for the XML Extractor
    ``` xml
    <bean id="extractorXml" class="org.archive.modules.extractor.ExtractorXML"></bean>
    ```

2.  Link the "extractorXml" bean to the "fetchProcessors" bean
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
    <!-- ************ ...extract outlinks from XML/RSS content.. ********** -->
    <ref bean="extractorXml"/>
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
