# Duplication Reduction Processors

# URL-Agnostic Duplication Reduction

To configure url-agnostic deduplication of identical content, add these
toplevel beans to your crawler-beans.cxml:

``` xml
  <!-- optional, will use the main bdb module if omitted, just like old dedup -->
  <bean id="historyBdb" class="org.archive.bdb.BdbModule" autowire-candidate="false">
   <property name="dir" value="history" />
  </bean>

  <bean id="contentDigestHistory" class="org.archive.modules.recrawl.BdbContentDigestHistory">
   <property name="bdbModule">
    <ref bean="historyBdb" />
   </property>
  </bean>
```

And then insert these beans into your disposition chain, sandwiching the
warcWriter:

``` xml
  <bean id="dispositionProcessors" class="org.archive.modules.DispositionChain">
   <property name="processors">
    <list>
==>    <bean class="org.archive.modules.recrawl.ContentDigestHistoryLoader" />
     <!-- write to aggregate archival files... -->
     <ref bean="warcWriter"/>
==>    <bean class="org.archive.modules.recrawl.ContentDigestHistoryStorer" />
     <!-- ...send each outlink candidate URI to CandidateChain,
          and enqueue those ACCEPTed to the frontier... -->
     <ref bean="candidates"/>
     <!-- ...then update stats, shared-structures, frontier decisions -->
     <ref bean="disposition"/>
     <!-- <ref bean="rescheduler" /> -->
    </list>
   </property>
  </bean> 
```

 

    Legacy Duplication Reduction Configuration

Starting in release 1.12.0, a number of Processors can cooperate to
carry forward URI content history between crawls (see
`org.archive.crawler.processor.recrawl` package JavaDocs). This reduces
the amount of duplicate material downloaded or stored in later crawls.
See [Deduping (Duplication
Reduction)](Deduping%20(Duplication%20Reduction)) for *H1* dedupe
configuration details. In *H3*, use the `crawler-beans.cxml` file to
setup deduplication add the following processors as described below.

## Configure persistent URI history storage

These settings should be added to any crawl that is to provide
historical-fetch information for future de-duplication (such as the
first of two crawls, or every crawl of an ongoing series).

(1) Define a named bean for `FetchHistoryProcessor`:

``` xml
<bean id="fetchHistoryProcessor" class="org.archive.modules.recrawl.FetchHistoryProcessor">
 <!-- <property name="historyLength" value="2" /> -->
</bean>
```

(2) Define a named bean for `PersistStoreProcessor`:

``` xml
<bean id="persistStoreProcessor" class="org.archive.modules.recrawl.PersistStoreProcessor">
</bean>
```

(3) Add those processor beans to the relevant processing chains.

The *fetchHistoryProcessor* should be added to the *FetchChain* after
the other fetch processors. The *persistStoreProcessor* should be added
after any writers in the *DispositionChain*. This is best done by using
"ref" tags to refer to the above processor beans inside the *FetchChain*
and *DispositionChain* bean definitions.

For example in a typical FetchChain:

``` xml
<bean id="fetchProcessors" class="org.archive.modules.FetchChain">
  <property name="processors">
   <list>
    <!-- recheck scope, if so enabled... -->
    <ref bean="preselector"/>
    <!-- ...then verify or trigger prerequisite URIs fetched, allow crawling... -->
    <ref bean="preconditions"/>
    <!-- ...fetch if DNS URI... -->
    <ref bean="fetchDns"/>
    <!-- ...fetch if HTTP URI... -->
    <ref bean="fetchHttp"/>
=>    <ref bean="fetchHistoryProcessor" />
    <!-- ...extract oulinks from HTTP headers... -->
    <ref bean="extractorHttp"/>
    <!-- ...extract oulinks from HTML content... -->
    <ref bean="extractorHtml"/>
    <!-- ...extract oulinks from CSS content... -->
    <ref bean="extractorCss"/>
    <!-- ...extract oulinks from Javascript content... -->
    <ref bean="extractorJs"/>
    <!-- ...extract oulinks from Flash content... -->
    <ref bean="extractorSwf"/>
   </list>
  </property>
</bean>
```

And in a typical DispositionChain:

``` xml
<bean id="dispositionProcessors" class="org.archive.modules.DispositionChain">
  <property name="processors">
   <list>
    <!-- write to aggregate archival files... -->
    <ref bean="warcWriter"/>
=>  <ref bean="persistStoreProcessor" />
    <!-- ...send each outlink candidate URI to CandidatesChain,
         and enqueue those ACCEPTed to the frontier... -->
    <ref bean="candidates"/>
    <!-- ...then update stats, shared-structures, frontier decisions -->
    <ref bean="disposition"/>
   </list>
  </property>
</bean>
```

Once this is done, URI history information of interest to later crawls
is retained by the crawl's default BDB environment (as managed by
BdbModule, residing on disk in the 'state' directory).

## Configure persistent URI history loading for subsequent crawls

Follow the steps below for any crawl that is to take advantage of
deduplication, such as the second of two crawls, or all crawls in a
series beyond the first.

(1) Define a named bean for `PersistLoadProcessor`:

``` xml
<bean id="persistLoadProcessor" class="org.archive.modules.recrawl.PersistLoadProcessor">
</bean>
```

As configured here, the URI history info will be loaded from the crawl's
default BDB environment (as managed by BdbModule, residing on disk in
the 'state' directory).

(2) If it does not already exist (from above), define a named bean for
`FetchHistoryProcessor`:

``` xml
<bean id="fetchHistoryProcessor" class="org.archive.modules.recrawl.FetchHistoryProcessor">
 <property name="historyLength" value="10" />
</bean>
```

(3) Ensure these processor beans are in the appropriate processing
chains at the right places. Add the `ref` tags for the above processors
to the *FetchChain* bean. Add the *persistLoadProcessor* processor after
the *preconditions* Bean. Add the *fetchHistoryProcessor* after other
fetching beans.

``` xml
<bean id="fetchProcessors" class="org.archive.modules.FetchChain">
  <property name="processors">
   <list>
    <!-- recheck scope, if so enabled... -->
    <ref bean="preselector"/>
    <!-- ...then verify or trigger prerequisite URIs fetched, allow crawling... -->
    <ref bean="preconditions"/>
=>    <ref bean="persistLoadProcessor"/>
    <!-- ...fetch if DNS URI... -->
    <ref bean="fetchDns"/>
    <!-- ...fetch if HTTP URI... -->
    <ref bean="fetchHttp"/>
=>    <ref bean="fetchHistoryProcessor"/>
    <!-- ...extract oulinks from HTTP headers... -->
    <ref bean="extractorHttp"/>
    <!-- ...extract oulinks from HTML content... -->
    <ref bean="extractorHtml"/>
    <!-- ...extract oulinks from CSS content... -->
    <ref bean="extractorCss"/>
    <!-- ...extract oulinks from Javascript content... -->
    <ref bean="extractorJs"/>
    <!-- ...extract oulinks from Flash content... -->
    <ref bean="extractorSwf"/>
   </list>
  </property>
</bean>
```

### *preloadSource* option

If you want to pull persistent URI history from a non-default source,
the `preloadSource` property may be used on the PersistLoadProcessor.
Its value should be the path to another prior crawl's `state` directory,
or a path or URI to another prior crawl's persist log
(`persistlog.txtser.gz`) in the event the PersistLogProcessor was used,
which is not recommended in H3 and not described above.

Preloading scans the old state directory or log at startup, loading the
current crawl's state directory with the history information. This can
be time-consuming step which delays the start of the crawl. Note that
preloadSource must *not* be the current crawl's state directory or an
error will result.

``` xml
<bean id="persistLoadProcessor" class="org.archive.modules.recrawl.PersistLoadProcessor">
 <property name="preloadSource" value="/Users/me/Documents/heritrix-3.0.0-SNAPSHOT/jobs/originalCrawl/state"/>
</bean>
```

OR

``` xml
<bean id="persistLoadProcessor" class="org.archive.modules.recrawl.PersistLoadProcessor">
 <property name="preloadSource" value="file:///Users/me/Documents/heritrix-3.0.0-SNAPSHOT/jobs/originalCrawl/logs/persistlog.txtser.gz"/>
 </bean>
```

## Configuring Other Processors

The above configuration ensures historical fetch information is retained
between crawls. Whether this affects fetching or storing of URIs depends
on settings in other processors, most importantly the FetchHTTP
processor and the WARCWriterProcessor or ARCWriterProcessor.

In the FetchHTTP processor, the *sendIfNoneMatch* and
*sendIfModifiedSince* properties control whether the HTTP If-None-Match
or If-Modified-Since headers are sent on a request if the URI history
information (prior-fetch date or etag info) to support them is present.

Note that by sending these headers, the crawler may receive a '304-Not
Modified' response from the server, with no body content. In this way,
other URIs may not be discovered, and paths followed by the original
crawl not reconsidered for refetching. Thus if you leave
*sendIfNoneMatch* and *sendIfModifiedSince* set as their default 'true'
values on a deduplication-history-enabled crawl, you may wish to use
some other technique to ensure all URIs from the earlier crawls are
reconsidered (such as feeding them all to the crawl at the start).

Both ARCWriterProcessor and WARCWriterProcessor have a property
*skipIdenticalDigests*. By default this is false. If true, any fetch
whose content has an identical digest value as the previous fetch will
be skipped completely for writing purposes. For ARCWriterProcessor, this
means the ARC record will not be written, and nothing else will be
written in its place. Similarly for WARCWriterProcessor, no records of
any type will be written. Only the crawl.log will record that the fetch
occurred.

WARCWriterProcessor has additional properties for more sophisticated
duplication handling. The *writeRevisitForIdenticalDigests* property, by
default true, will write a reduced-size (no content-body) WARC 'revisit'
record in lieu of a 'response' record when a repeat digest is detected
by consulting the history information. (Note that if
*skipIdenticalDigests* above was true, not even this will be written –
as all writing will has already been skipped.) If false, a full
'response' record (with all the duplicate content) will still be
written, even with a repeat digest value.

The *writeRevisitForNotModified* property, default true, will write a
WARC 'revisit' record in lieu of a 'response' record when '304-Not
Modified' responses are received. If false, a normal 'response' record
is written.

## Advanced: using a non-default history BDB environment

Crawls may wish to store persistent URI history information to a
different place than the default BDB environment ('state') directory.
Motivations for such a choice might include:

1.  spreading crawl disk IO to another place
2.  keeping history info distinct from other more transient crawl info
    (queues, in-crawl state) to make it easier to analyze or migrate
    separately

To do this, the first step is to define more than one BdbModule in the
crawl configuration, and giving this second BdbModule a distinct bean
name and environment *dir*. It also must be excluded from consideration
for Spring auto-wiring (so that only a single BdbModule serves that
purpose). For example:

``` xml
<bean id="historyBdb"
  class="org.archive.bdb.BdbModule" autowire-candidate="false">
  <property name="dir" value="history" />
 </bean>
```

Then, have the other PersistLoadProcessor and/or PersistStoreProcessor
explicitly refer to this BdbModule by name, rather than simply accepting
the autowired default. For example:

``` xml
<bean id="persistLoadProcessor" class="org.archive.modules.recrawl.PersistLoadProcessor">
  <property name="bdbModule">
    <ref bean="historyBdb"/>
  </property>
</bean>
<bean id="persistStoreProcessor" class="org.archive.modules.recrawl.PersistStoreProcessor">
 <property name="bdbModule">
    <ref bean="historyBdb"/>
  </property>
</bean>
```

You could also load past history from a different environment than the
new info is stored to if you want to keep each cycle distinct.

## Considerations when designing a crawl using duplication-reduction

Duplication reduction at its current level offers two major potential
benefits when repeating a crawl: savings of bandwidth, and savings of
storage space.

In order for there to be bandwidth savings, the *sendIfNoneMatch* and/or
*sendIfModifiedSince* options must be enabled. Then, servers may report
that there's been no significant change since the version previously
fetched – saving the time and bandwidth expenditure of sending redundant
content.

However, this changes the information available to the followup crawl.
It will no longer see the content, and thus no longer discover the
oulinks from that page, to be reconsidered on their own. So, if the only
path to a changed page is via an unchanged page which, due to a '304-Not
Modified' response, is never link-extracted in the followup crawl, the
changed page will never be considered for recrawling and thus the change
will not be discovered and archived. Thus it is important that if using
these bandwidth-reduction, conditional-GET features, the operator
manually ensure all URIs of interest from the first crawl are enqueued
to the followup crawl (either as seeds or some other addition during the
crawl).

Because of this complication, many crawls may want to only use
digest-based duplication-reduction. This offers no bandwidth savings:
all URIs are fetched again. But, when the strong digest of the content
is unchanged, the content is either not rewritten, or only rewritten in
a abbreviated form (such as a WARC 'revisit' record). This approach
entails setting the *sendIfModifiedSince* and *sendIfNoneMatch*
properties of FetchHTTP to false.

A future improvement to these features may carry discovered outlink
information forward as part of URI history, so that outlinks can be
'virtually discovered' even when a '304-Not Modified' means no
extractable copy of the unchanged content is available to the crawler.

## Attachments:

![](images/icons/bullet_blue.gif){width="8" height="8"}
[crawler-beans.cxml](attachments/5735743/92766372.cxml)
(application/octet-stream)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[crawler-beans.cxml](attachments/5735743/92766371.cxml)
(application/x-upload-data)  
