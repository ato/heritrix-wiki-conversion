# Release Notes - 1.14.2

# Release Notes - 1.14.2 (November 2008)

These are the project wiki Release Notes for the 1.14.2 release.

Release 1.14.2 is a 'micro' release with a number of small bugfixes.

The 1.14.2 release is available at [the archive-crawler Sourceforge
project](https://sourceforge.net/project/showfiles.php?group_id=73833&package_id=73980&release_id=638940).

## Notable Changes

### WARC 'metadata' records MIME type matches spec ([HER-1541](https://webarchive.jira.com/browse/HER-1541))

WARC 'metadata' records are now written with the MIME type matching the
format definition in the 0.18 specification, 'application/warc-fields'.
(The data format is unchanged, and any 'text/anvl' content written by
earlier releases may be interpreted as 'application/warc-fields'
content.)

### A bottleneck in StatisticsTracker.saveSourceStats has been removed ([HER-1553](https://webarchive.jira.com/browse/HER-1553))

If crawling with the 'source-tag-seeds' option enabled, collecting the
hosts-per-source reporting information would begin to take an inordinate
amount of unnecessary serialization effort several days into a crawl.
The redundant work has been skipped, greatly improving performance when
this option is enabled. (The option is by default off.)

## All Tracked Changes

The following 7 tracked issues are recorded as addressed in this 1.14.2
release:

<http://webteam.archive.org/jira/secure/ReleaseNote.jspa?projectId=10021&styleName=Html&version=10082>

type

key

summary

status

Unable to locate JIRA server for this macro. It may be due to
Application Link configuration.
