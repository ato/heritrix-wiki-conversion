# Setting Operator Information

# Heritrix 2.0 Tutorial

## Using the Web User Interface

### Setting Operator Information

By clicking on the "Sheets" link of a profile, you will be taken to the
following screen:

![](attachments/3762/90996903.png)

This screen shows all of the *configuration sheets* for a profile. A
configuration sheet is a list of settings that control the crawl. By
default, there is only one sheet listed. This is the *global* sheet, and
it's the most important. The global sheet is consulted when no
URL-specific configuration information is needed.

Other sheets of settings can be created, and these extra sheets can be
associated with URLs to provide crawl configuration specific to those
URLs. For instance, later in the tutorial we'll be adding a
configuration sheet to make the crawler slow down when crawling
archive.org, so that their web servers are not overburdened by the
crawl.

Note the bold red text that says "validation problems". The profiles
that ship with Heritrix are not fully configured. There are two settings
in the global sheet you will have to change before your crawl will work.
We don't set these for you because they identity you as a person: You
must enter your email address and an URL describing why you're using
Heritrix to crawl the web. This information is provided to web servers
as the engine crawls them. A webmaster who notices an abusive Heritrix
crawl can then work with you to minimize the damage to their site.

Go ahead and click the "Edit" link under the global sheet, so you can
enter your information. You'll be taken to the Sheet Editor for the
global sheet:

![](attachments/3762/90997064.png)

This screen shows you all the settings in a nested list. Discussing
every setting is beyond the scope of this tutorial, so for now let's
just look for the two problematic settings. Scroll down until you see
red:

![](attachments/3762/90996912.png)

This is the first setting you'll need to change. To do so, first click
the "Add" link next to the setting. This adds the setting to the global
sheet; you'll see the text to the right of the opearting-contact-url
label change from "default" to "global". Also the text box should now be
editable.

The other problem setting is right below:

![](attachments/3762/90996992.png)

Again, you want to click the "Add" link next to operator-from to add it
to the global sheet. Now that the two problems settings are overridden
in the global sheet, you can edit them in the sheet edit. Replace
"ENTER-A-CONTACT-HTTP-URL-CRAWL-OPERATOR" with your URL, and replace
"ENTER-A-CONTACT-EMAIL-FOR-CRAWL-OPERATOR" with your email address.

Now scroll down to the bottom of the page, where you'll see a "Submit
Changes" button. Push that to save your changes to the sheet.

*You are not done yet!* When you edit a configuration sheet, the changes
are not actually saved until you *commit* the sheet. We added this extra
step so that you can change multiple settings in a running crawl and
apply all of the changes at the same time.

You'll notice at the very top of the sheet editor, there is a red
exclamation point warning you that your sheet is uncommitted:

![](attachments/3762/90997096.png)

Go ahead and click the "commit" link. This will take you back to the
list of sheets, but you will notice that the red "validation errors"
text has gone away.

At this point, you could click on the Engine ID and launch the profile,
but I want to show how to override settings for particular URLs first.

## Attachments:

![](images/icons/bullet_blue.gif){width="8" height="8"}
[sheets.png](attachments/3762/90996878.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[global.png](attachments/3762/90996852.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[operator-contact-url.png](attachments/3762/90996834.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[operator-from.png](attachments/3762/90996935.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[unsaved.png](attachments/3762/90997096.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[sheets\_alpha2.png](attachments/3762/90996903.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[global\_alpha2.png](attachments/3762/90997064.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[operator-from\_alpha2.png](attachments/3762/90996992.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[operator-contact-url\_alpha2.png](attachments/3762/90996912.png)
(image/png)  
