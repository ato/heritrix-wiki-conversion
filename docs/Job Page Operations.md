# Job Page Operations

###### Edit

This operation allows you to edit the `crawler-beans.cxml` file.  The
`crawler-beans.cxml` file contains the Spring configuration of the crawl
job.  Editing this file is the standard way to configure a job or
profile.

###### Build

This operation builds the Spring Java classes that are configured
through the `crawler-beans.cxml` file.  Before a job is run it must be
built.

###### Launch

This operation launches a crawl job.  Before being launched a job must
be built.  Once the job is launched it will be in either a paused state
or running state.  If it is in a paused state the "unpause" button must
be clicked to start the crawl.  As of Heritrix 3.1, if a checkpoint or
multiple checkpoints has/have been run, a checkpoint can be selected
from the ﻿[checkpoint dropdown](Job%20Page%20Data%20Elements) box.  The
job can then be restarted at the checkpoint by clicking "launch".

###### Pause

This operation pauses a running crawl.

###### Unpause

This operation unpauses a paused crawl.

###### Checkpoint

This operation writes the current state of the crawl to storage.  During
the time the crawl is being checkpointed it is paused and no URIs will
be crawled.  Checkpointing is useful if a crawl must be stopped and then
restarted at a later time.

###### Terminate

This operation stops a crawl. 

###### Teardown

This operation will discard the job's current Spring Java classes and
allows a new Spring configuration to be built.  Any change to the
`crawler-beans.cxml` file after the "Build" button has been invoked
requires a teardown and another build to be run.

###### Copy

This operation allows you to copy the current job configuration to a new
job or profile.

###### Scripting Console

This link displays an input form that can be used to input and execute
script commands.  The script commands can be used to control the
behavior of a crawl job.  Various scripting languages are available such
as AppleScript and ECMAScript.  Examples of scripts can be found ﻿﻿here.

###### Browse Beans

This link displays the hierarchy of Spring beans that make up a crawl
job.  The properties and associations of each bean can be viewed or
edited by clicking on the bean.
