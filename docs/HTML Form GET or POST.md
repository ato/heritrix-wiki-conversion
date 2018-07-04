# HTML Form GET or POST

To use the HTML Form `GET` or `POST` credential, supply a `domain`,
`http-method`, `login-uri`, and `form-items`.

Before a URI is scheduled for crawling, Heritrix looks for
preconditions.  Examples of preconditions include capturing the DNS
record of the server that hosts the URI and fetching the `robots.txt`
file.  The HTML Form credentials are also processed as a precondition. 
If there are HTML Form credentials for a particular CrawlServer in the
Credential Store, the URI specified in the HTML Form credential
`login-uri` field is scheduled as a precondition for the site, after the
DNS and `robots.txt` preconditions.

###### domain

See [RFC2617 (BASIC AND DIGEST
Auth)](https://webarchive.jira.com/wiki/display/Heritrix/RFC2617+%28BASIC+and+DIGEST+Auth%29)
domain.

###### login-uri

The `login-uri` is a relative or absolute URI to which the HTML Form
submits.  It is not necessarily the page that contains the HTML Form;
rather it is the ACTION URI the to which the form submits.

###### form-items

Form-items are a listing of HTML Form key/value pairs. The submit button
usually must be included in the form-items.

An HTML Form `GET` or `POST` credential configuration is illustrated
below. (Note that this bean must appear in the
[CredentialStore](Credential%20Store)'s 'credentials' map, either via a
bean-reference, or by being defined inline there.)

``` xml
<bean id="credential"
   class="org.archive.modules.credential.HtmlFormCredential">

    <property name="domain" value="example.com" />

    <property name="login-uri" value="http://example.com/login"/>

    <property name="form-items">
        <map>
            <entry key="login" value="mylogin"/>
            <entry key="password" value="mypassword"/>
            <entry key="submit" value="submit"/>
        </map>
    </property>
</bean>
```

**Note**

-   For a site with an HTML Form credential, a login is performed
    against all listed HTML Form credential `login-uris` after the DNS
    and `robots.txt` preconditions are fulfilled.  The crawler will only
    view sites that have HTML Form credentials from a `logged-in`
    perspective.  There is no current way for a single Heritrix job to
    crawl a site in an unauthenticated state and then re-crawl the site
    in an authenticated state. (You would have to do this in two
    separately-configured job launches.)
-   The form login is only run once.  Heritrix continues crawling
    regardless of whether the login succeeds. There is no way of telling
    Heritrix to retry authentication if the first attempt is not
    successful.  Neither is there a means for the crawler to report
    success or failed authentications.  The crawl operator should
    examine the logs to determine whether authentication succeeded.
-   Some sites' login forms may have form items with dynamic names, or
    necessary extra hidden fields whose required value changes for each
    visitor. This HtmlFormCredential mechanism has no support for
    successfully submitting such forms.
