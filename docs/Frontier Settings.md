# Frontier Settings

###### Politeness

A combination of several settings control the politeness of the
Frontier.  It is important to note that at any given time only one URI
from any given host is processed.  The following politeness rules impose
additional wait time between the end of processing one URI and the start
of the next one.

-   **delayFactor** - This setting imposes a delay between the fetching
    of URIs from the same host.  The delay is a multiple of the amount
    of time it took to fetch the last URI downloaded from the host.  For
    example, if it took 800 milliseconds to fetch the last URI from a
    host and the `delayFactor` is 5 (a very high value), then the
    Frontier will wait 4000 milliseconds (4 seconds) before allowing
    another URI from that host to be processed.
-   **maxDelayMs**- This setting imposes a maximum upper limit on the
    wait time created by the `delayFactor`.  If set to 1000
    milliseconds, then the maximum delay between URI fetches from the
    same host will never exceed this value.
-   **minDelayMs**- This setting imposes a minimum limit on politeness. 
    It takes precedence over the value calculated by the `delayFactor`. 
    For example, the value of `minDelayMs` can be set to 100
    milliseconds.  If the `delayFactor` only generates a 20 millisecond
    wait, the value of `minDelayMs` will override it and the URI fetch
    will be delayed for 100 milliseconds. 
    ``` xml
    <bean id="disposition" class="org.archive.crawler.postprocessor.DispositionProcessor">
    <property name="delayFactor" value="5.0" />
    <property name="maxDelayMs" value="30000" />
    <property name="minDelayMs" value="3000" /></bean>
    ```

###### Retry Policy

The Frontier can be used to limit the number of fetch retries for a
URI.  Heritrix will retry fetching a URI because the initial fetch error
may be a transitory condition.

-   **maxRetries** - This setting limits the number of fetch retries
    attempted on a URI due to transient errors.
-   **retryDelaySeconds** - This setting determines how long the wait
    period is between retries.

``` xml
<bean id="frontier"
   class="org.archive.crawler.frontier.BdbFrontier">

  <property name="retryDelaySeconds" value="900" />
  <property name="maxRetries" value="30" />

 </bean>
```

###### Bandwidth Limits

The Frontier allows the user to limit bandwidth usage.  This is done by
holding back URIs when bandwidth usage has exceeded certain limits. 
Because bandwidth usage limitations are calculated over a period of
time, there can still be spikes in usage that greatly exceed the limits.

-   **maxPerHostBandwidthUsageKbSec** - This setting limits the maximum
    bandwidth to use for any host.  This setting limits the load placed
    by Heritrix on the host.  It is therefore a politeness setting.
    ``` xml
    <bean id="disposition" class="org.archive.crawler.postprocessor.DispositionProcessor">
    <property name="maxPerHostBandwidthUsageKbSec" value="500" />
    </bean>
    ```

###### Extractor Parameters

As of Heritrix 3.1, the Frontier's behavior with regard to link
extraction can be controlled by the following parameters.

-   **extract404s** - This setting allows the operator to avoid
    extracting links from 404 (Not Found) pages.  The default is true,
    which maintains the pre-3.1 behavior of extracting links from 404
    pages.
    ``` xml
    <bean id="frontier" class="org.archive.crawler.frontier.BdbFrontier">
    <property name="extract404s" value="true" />
    </bean>
    ```

-   **extractIndependently** - This setting encourages extractor
    processors to always perform their best-effort extraction, even if a
    previous extractor has marked a URI as already-handled.  Set the
    value to true for best-effort extraction.  The default is false,
    which maintains the pre-3.1 behavior.
    ``` xml
    <bean id="frontier" class="org.archive.crawler.frontier.BdbFrontier">
    <property name="extractIndependently" value="false" />
    </bean>
    ```
