# Job Page

Heritrix 3.0/3.1 introduces the ability to run multiple jobs
simultaneously on the same crawler instance.  In Heritrix 1.x, only one
job could be run at a time.  Other jobs were queued behind the running
job. The only limit effecting the number of jobs that can be run
simultaneously in Heritrix 3.0/3.1 is the amount of memory allocated to
the Java heap.  If many crawls are run, the Java heap may at some point
be exhausted. This will result in an `OutOfMemory` error that will abort
the running crawls.

Once a crawl job has been created and properly configured it can be
run.  To start a crawl the user must go to the job page by clicking the
specific job in the WUI. 
![](attachments/5735668/5865608.png){.image-center}

## Attachments:

![](images/icons/bullet_blue.gif){width="8" height="8"}
[job.png](attachments/5735668/5865658.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[job.png](attachments/5735668/5865608.png) (image/png)  
