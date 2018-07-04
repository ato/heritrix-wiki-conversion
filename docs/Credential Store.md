# Credential Store

The Credential Store contains the http or form login information.  It
must be configured in the `crawler-beans.cxml` file.

This is an example of an empty CredentialStore:

``` xml
<bean id="credentialStore"
      class="org.archive.modules.credential.CredentialStore">
</bean>
```

However, for it to work, its 'credentials' map property must be filled
with suitable Credential instances. For example, if you have an
HtmlFormCredential bean defined elsewhere with id 'formCredential', then
the following will result in a CredentialStore including that
Credential:

``` xml
<bean id="credentialStore"
       class="org.archive.modules.credential.CredentialStore">
 <property key="credentials">
  <map>
   <entry key="formCredential" value-ref="formCredential" />
  </map>
 </property>
</bean>
```
