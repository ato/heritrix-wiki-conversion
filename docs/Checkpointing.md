# Checkpointing

Checkpointing a crawl job writes a representation of the current state
of the job to a directory under the `checkpointsPath`.  The directory is
named after the checkpoint.  Checkpointed state includes serialization
of the main crawl job objects, copies of the current set of bdbje log
files, and other files that represent the state of the crawl.  The
checkpoint directory contains all that is required to recover a crawl. 
Checkpointing also rotates the crawl logs, including the `recover.gz`
log, if enabled.  Log files are NOT copied to the checkpoint directory. 
They are left under the `logs` directory and are distinguished by a
suffix.  The suffix is the checkpoint name.  For example, for checkpoint
`000031` the crawl log would be named `crawl.log.000031`.

To run a checkpoint, click the checkpoint button on the job page of the
WUI or invoke the checkpoint functionality through the REST API.  The
checkpoint may take a long period of time to finish for large crawls
(though Heritrix 3.11 and later are much faster than previous
versions).  While checkpointing, the crawl status will show as
CHECKPOINTING.  When the checkpoint has completed, the crawler will
resume crawling, unless it was in the paused state when the checkpoint
was invoked.  In this case, the crawler will re-enter the paused state.

Recovery from a checkpoint has much in common with the recovery of a
crawl using the `frontier.recovery.log`.

###### Automated Checkpointing

To configure Heritrix to automatically run checkpoints, uncomment or add
to following line to the `logging.properties` file.

`org.archive.crawler.framework.Checkpointer.period=2`

This will install a Timer Thread that will run in hour intervals.  See
`heritrix_out.log` for logging information regarding the Timer Thread.

As of Heritrix 3.1, 'hard' links (where available) will now be used to
collect the BerkeleyDB-JE files required to reproduce the crawler's
state.  Automatic deletion of outdated checkpoint files (the ".DEL"
files) has been reenabled. This eliminates the need to manually delete
unneeded files.  Also, it makes moving or clearing old checkpoints
easier.

###### Re-starting From a Checkpoint

As of Heritrix 3.1, the WUI provides an option to restart a crawl from a
checkpoint.  Follow the steps below to re-start a crawl from a
checkpoint.

1.  Checkpoint the running crawl by clicking the "checkpoint" button.
2.  When the checkpoint ends (a message will be displayed informing the
    operator of this event) terminate the crawl by clicking the
    "terminate" button.
3.  Teardown the job by clicking the "teardown" button.
4.  Re-build the job by clicking the "build" button.  At this point a
    dropdown box should appear under the command buttons.  The dropdown
    box has the names of the previously invoked checkpoints.
    ![](attachments/5735739/15564808.png)
5.  Select a checkpoint from the dropdown.  The selected checkpoint will
    be used to start the newly built job.
6.  Click launch
7.  Click unpause

The job will now begin running from the chosen checkpoint.

## Attachments:

![](images/icons/bullet_blue.gif){width="8" height="8"}
[checkpointuidropdown.png](attachments/5735739/15564808.png)
(image/png)  
