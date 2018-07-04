# Create a Sheet of Overrides

# Heritrix 2.0 Tutorial

## Using the Web User Interface

### Create a Sheet of Overrides

If you've been following along, you should be on the Sheets screen for
the `basic_seed_sites` profile. Click on the "Add Single Sheet" link,
and you should see the following screen:

![](attachments/3773/90997199.png)

I want to use this sheet to slow down crawling on `archive.org` sites,
so let's enter "Slowly" as the name for the new sheet and hit submit.
You'll then be taken to a sheet editor for the new sheet. This has all
the same settings as the global sheet.

Before you can change a setting in this new sheet, you first have to add
the setting to the sheet. This is a simple matter of clicking the "Add"
link next to the setting. Similarly, clicking the "Remove" link will
remove a setting from a sheet. Not all settings will have "add" or
"remove" links - some settings can't be changed by sheets, and are only
available in the global sheet. Other settings (the settings at the very
top of the screen, before "root") are *bootstrap settings*, which were
used to initialize the settings system itself. Bootstrap settings can't
be modified anywhere, not even in the global sheet.

If you want to know the exact reason why you can't add a particular
setting, you should click the "details" link. This will provide
additional information about the setting, including any information
regarding its restrictions.

The setting we want to override is called "min-delay-ms" - it specifies
the minimum amount of time for the engine to wait before making another
request to a previously visited server.

![](attachments/3773/90997198.png)

Click on the "Add" link beneath the setting, and two important changes
will occur:

![](attachments/3773/90997036.png)

First, the text field can now be edited, and we can bump up the setting
from a 3-second delay to a 30-second delay. (The `min-delay-ms` setting
is measured in milliseconds.) The second change is that the gray text
next to the setting's name has changed from "global" to "Slowly" - this
is telling you that the setting has become a part of the Slowly sheet.

Change the value from 3000 to 30000, then scroll down to the bottom of
the page and click "Submit Changes". Remember, *you have to commit the
sheet before your changes take effect!* Click "commit" next to the sheet
name at the top of the screen, and you should be take back to the sheet
list.

You're now ready to associate URLs with your new configuration sheet.

## Attachments:

![](images/icons/bullet_blue.gif){width="8" height="8"}
[newsheet.png](attachments/3773/90997199.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[30000.png](attachments/3773/90997036.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[min-delay-ms.png](attachments/3773/90997198.png) (image/png)  
