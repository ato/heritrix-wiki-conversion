# A Quick Guide to Running Your First Crawl Job

The Main Console page is displayed after you have installed Heritrix and
logged into the WUI. ![](attachments/5735610/5865593.png){.image-center}

1.  Enter the name of the new job in the text box with the "Create new
    job with recommended starting configuration" label.  Then click
    "create." ![](attachments/5735610/5865640.png){.image-center}  
    The new job will be displayed in the list of jobs on the Main
    Console page.  The job will be based on the profile-defaults profile
    in Hertitrix 3.0. As of Heritrix 3.1, the profile-defaults profile
    has been eliminated. See [Profiles](Profiles) for more
    information.  
    ![](attachments/5735610/5865595.png){.image-center}
2.  Click on the name of the new job and you will be taken to the job
    page.  
    ![](attachments/5735610/5865596.png){.image-center}  
    The name of the configuration file, crawler-beans.cxml, will be
    displayed at the top of the page.  Next to the name is an "edit"
    link. 
3.  Click on the "edit" link and the contents of the configuration file
    will be displayed in an editable text area.
    ![](attachments/5735610/5865597.png){.image-center}
4.  At this point you must enter several properties to make the job
    runnable. 
    1.  First, add a valid value to the metadata.operatorContactUrl
        property, such as <http://www.archive.org>.
        ![](attachments/5735610/5865650.png){.image-center}
    2.  Next, populate the `<prop>` element of the `longerOverrides`
        bean with the seed values for the crawl.  A test seed is
        configured for reference.  When done click "save changes" at the
        top of the page. For more detailed information on configuring
        jobs see [Configuring Jobs and
        Profiles](Configuring%20Jobs%20and%20Profiles).
        ![](attachments/5735610/5865651.png){.image-center}
5.  From the job screen, click "build."  This command will build the
    Spring infrastructure needed to run the job. In the Job Log the
    following message will display: "INFO JOB instantiated."
    ![](attachments/5735610/5865652.png){.image-center}
6.  Next, click the "launch" button.  This command launches the job in
    "paused" mode.  At this point the job is ready to run.
    ![](attachments/5735610/5865653.png){.image-center}
7.  To run the job, click the "unpause" button.  The job will now begin
    sending requests to the seeds of your crawl.  The status of the job
    will be set to "Running."  Refresh the page to see updated
    statistics. ![](attachments/5735610/5865654.png){.image-center}  
    **Note**

-   A job will **not** be modified if the profile or job it was based on
    is changed.

<!-- -->

-   Jobs based on the default profile are not ready to run *as-is*.  The
    `metadata.operatorContactUrl` must be set to a valid value.

Detailed information about evaluating the progress of a job can be found
at [Job Analysis](Job%20Analysis).

## Attachments:

![](images/icons/bullet_blue.gif){width="8" height="8"}
[mainconsole.png](attachments/5735610/5865639.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[addjob.png](attachments/5735610/5865594.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[mainconsolenewjob.png](attachments/5735610/5865647.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[job.png](attachments/5735610/5865648.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[cxmledit.png](attachments/5735610/5865649.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[cxmloperator.png](attachments/5735610/5865599.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[cxmloperator.png](attachments/5735610/5865598.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[cxmlseeds.png](attachments/5735610/5865600.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[build2.png](attachments/5735610/5865601.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[launch.png](attachments/5735610/5865602.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[unpause.png](attachments/5735610/5865603.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[mainconsole.png](attachments/5735610/5865593.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[newjob.png](attachments/5735610/5865641.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[newjob.png](attachments/5735610/5865640.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[mainconsolenewjob.png](attachments/5735610/5865595.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[job.png](attachments/5735610/5865596.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[cxmledit.png](attachments/5735610/5865597.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[cxmleditoperator.png](attachments/5735610/5865650.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[cxmledit2.png](attachments/5735610/5865651.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[jobbuilt.png](attachments/5735610/5865652.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[joblaunched.png](attachments/5735610/5865653.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[jobunpaused.png](attachments/5735610/5865654.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[cxmleditoperator\[1\].png](attachments/5735610/52461572.png)
(image/png)  
