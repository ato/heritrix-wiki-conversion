# Web-based User Interface

After Heritrix has been launched, the Web-based user interface (WUI)
becomes accessible.

The URI to access the Web UI is typically

https://(heritrixhost):8443

The WUI is password protected.  There is no default login for access.  A
username and password must be specified using either the
`-a or -web-admin` command-line option at startup or by setting the
`heritrix.cmdline.admin` system property.  The username and password
will be printed to the console at startup.  As of Heritrix 3.1, the
admin username and password will not be printed to the console at
startup.  Also, as of Heritrix 3.1, if the parameter supplied to the -a
-web-admin command line option is a string beginning with "@", the rest
of the string is interpreted as a local file name containing the
operator login and password.  This adds an additional layer of
protection to the admin username and password.

The initial login page prompts for the username and password.  After
login, your session will time-out after a period of non-use.

Access to the WUI is through HTTPS.  Heritrix is installed with a
keystore containing a self-signed certificate.  This will cause the
Mozilla browser (the recommended browser) to display a prompt, warning
that a self-signed certificate is being used.  Follow the steps below to
login to Heritrix for the first time.

1.  Click on the "I Understand the Risks" link. A button allowing you to
    add a security exception will be displayed. Click on the "Add
    Exception" button.
    ![](attachments/5735602/5865643.png){.image-center}  
    ![](attachments/5735602/5865644.png){.image-center}
2.  A dialog will appear allowing you to confirm the exception by
    clicking "Confirm Security Exception".  
    ![](attachments/5735602/5865591.png){.image-center}
3.  After confirming the exception you will be prompted for the WUI
    username and password.  
    ![](attachments/5735602/5865592.png){.image-center}
4.  After entering the admin username and password, access will be
    granted to the WUI.

## Attachments:

![](images/icons/bullet_blue.gif){width="8" height="8"}
[untrustedcon1.png](attachments/5735602/5865589.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[untrustedcon2.png](attachments/5735602/5865590.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[untrustedcon3.png](attachments/5735602/5865591.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[login.png](attachments/5735602/5865592.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[untrust1.png](attachments/5735602/5865643.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[untrust2.png](attachments/5735602/5865644.png) (image/png)  
