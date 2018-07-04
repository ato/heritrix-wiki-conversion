# Whois Support

As of Heritrix 3.1, an optional fetcher for domain 'whois' data is
provided. A small set of well-established 'whois' servers are
preconfigured. The fetcher uses an ad-hoc/intuitive interpretation of a
'whois:' scheme URI.

``` xml
<bean id="fetchWhois" class="org.archive.modules.fetcher.FetchWhois">
<property name="specialQueryTemplates">
<map>
<entry key="whois.verisign-grs.com" value="domain %s" />
<entry key="whois.arin.net" value="z + %s" />
<entry key="whois.denic.de" value="-T dn %s" />
</map>
</property>
</bean>
```

To configure a whois seed, enter the seed in the following format:
 whois://hostname/path.  For example, whois://archive.org .  The whois
fetcher will attempt to resolve each host that the crawl encounters
using the topmost assigned domain and the ip address of the url crawled.
So if you crawl <http://www.archive.org/details/texts>, the whois
fetcher will attempt to resolve whois:archive.org and
whois:207.241.224.2. 

At this time, whois functionality is experimental.  The fetchWhois bean
is commented out in the default profile.
