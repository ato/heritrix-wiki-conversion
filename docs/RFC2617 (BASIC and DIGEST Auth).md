# RFC2617 (BASIC and DIGEST Auth)

To use the RFC2617 credential, supply a domain, realm, username, and
password.

The way that RFC2617 authentication works in Heritrix is that in
response to a 401 response code (Unauthorized), Heritrix will use a key
made up of the domain plus the realm to do a lookup into its Credential
Store. If a match is found, then the credential is loaded into the
CrawlURI and the CrawlURI is marked for immediate retry.

When the CrawlURI is retried, the found credentials are added to the
request. If the request succeeds with a 200 response code, the
credentials are promoted to the CrawlServer and all subsequent requests
made against the CrawlServer will preemptively volunteer the credential.
If the credential fails with a 401 response code, the URI is no longer
retried.

###### domain

The domain is the canonical root URI of RFC2617; it is the CrawlServer
name or [URI
authority](http://java.sun.com/j2se/1.4.2/docs/api/java/net/URI.html)
(domain plus port if other than port 80). Examples of domains are:
'www.archive.org' or 'www.archive.org:8080'.

###### realm

A realm is defined in
the [RFC2617](http://www.faqs.org/rfcs/rfc2617.html) faq.  The realm
string must exactly match the realm name presented in the authentication
challenge served by the web server.

An RFC2617 credential configuration is illustrated below.

``` xml
<bean id="credential"
class="org.archive.modules.credential.HttpAuthenticationCredential">


<property name="domain">
<value>
domain
</value>
</property>


<property name="realm">
<value>
myrealm
</value>
</property>


<property name="login">
<value>
mylogin
</value>
</property>


<property name="password">
<value>
mypassword
</value>
</property>


</bean>
```

**Note**

-   Only one realm per credential domain is allowed.  See [Logging in
    (HTTP POST, Basic Auth,
    etc.)](http://sourceforge.net/tracker/index.php?func=detail&aid=914301&group_id=73833&atid=539102)
    for more information.
