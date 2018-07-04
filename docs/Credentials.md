# Credentials

Credentials can be added so that Heritrix can gain access to areas of
Web sites requiring authentication.  Credentials are configured in the
Spring configuration file, `crawler-beans.cxml`.  The following example
shows a configured Credential.

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

One of the settings for a credential is its domain.  It is therefore
possible to create all credentials at a global level.  However, because
this can cause excessive unneeded checking of credentials, it is
recommended that credentials be added to a domain override.  This way,
the credential is only checked when the relevant domain is being
crawled.

Heritrix offers two types of authentication: RFC2617 (BASIC and DIGEST
Auth) and `POST` and `GET` of an HTML form.
