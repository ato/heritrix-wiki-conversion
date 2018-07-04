# Main Console Data Elements and Operations

###### rescan

The "rescan" button causes Heritrix to scan the file system for any
changes to the "jobs" directory.  The display is then synchronized with
the file system.

###### create

The "create" button allows you to enter the name of a new crawl job and
create it.  The crawl job will be based on the defaults profile.

###### add

The "add" button allows you to specify a job directory that is not
currently managed by Heritrix.  After entering the path to the new job
directory and clicking "add," Heritrix will allow you to manage the
directory.  For example, you will now be able configure the job using
the crawler-beans.cxml file.

###### status

In the Main Console page, the status of running jobs is displayed, as is
the number of times the job has been launched, and the path to the job's
configuration file.  Whether the job is a profile or not is also
displayed, along with Heritrix memory statistics.

###### Exit Java Process

As of Heritrix 3.1, the "Exit Java Process" button is provided.  This
button, when invoked with the "I'm sure" checkbox selected, will exit
and shutdown the Heritrix software.
