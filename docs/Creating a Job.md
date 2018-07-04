# Creating a Job

You can create a new job using one of three options:

**1. Based on an existing job**

This option allows a new job to be created based on an existing job,
regardless of whether the job has been crawled or not.  This option can
be useful for repeating crawls or recovering crawls that had problems. 
See [Recovery of Frontier State and
frontier.recover.gz](https://webarchive.jira.com/wiki/display/Heritrix/Recovery+of+Frontier+State+and+frontier.recover.gz). 
To base a new job on an existing job, use the "copy" button on the job
page of the parent job.
![](attachments/5735651/5865660.png){.image-center}  
**2. Based on a profile**  
This option allows a new job to be created based on an existing
profile.  To create a job based on a profile, use the "copy" button on
the profile page. ![](attachments/5735651/5865661.png){.image-center}  
**3. With defaults**  
This option creates a crawl job based on the default profile.  To create
a job from the default profile, enter a job name on the Main Console
screen and click the "create" button.
![](attachments/5735651/5865663.png){.image-center}

**Note**

-   Changes made to a profile or job will **not** change a derived job.

<!-- -->

-   Jobs based on the default profile provided with Heritrix are not
    ready to run *as is*.  The `metadata.operatorContactUrl` needs to be
    set to a valid value.

## Attachments:

![](images/icons/bullet_blue.gif){width="8" height="8"}
[copyjob.png](attachments/5735651/5865605.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[createnewjob.png](attachments/5735651/5865660.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[createjobbasedonprofile.png](attachments/5735651/5865661.png)
(image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[mainconsolenewjob.png](attachments/5735651/5865662.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[createnewjobdefault.png](attachments/5735651/5865663.png) (image/png)  
