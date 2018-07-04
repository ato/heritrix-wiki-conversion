# Release Notes - 1.14.3

# Release Notes - 1.14.3 (March 2009)

These are the project wiki Release Notes for the 1.14.3 release.

Release 1.14.3 is a 'micro' release with a number of small bugfixes and
new requested features.

The 1.14.3 release is now available at [the archive-crawler Sourceforge
project](https://sourceforge.net/project/showfiles.php?group_id=73833&package_id=73980&release_id=665587).

## Notable Changes

### Option to read persisted URI history at crawl start ([HER-1586](https://webarchive.jira.com/browse/HER-1586))

The PersistLoadProcessor has a new setting, 'preload-source', which may
be a local path to a persisted URI history log (as written by
PersistLogProcessor on a previous crawl), a URI to a similar log, or a
local path to a prior crawl state directory with URI history info (as
stored by PersistStoreProcessor on a previous crawl). At crawl start,
this history info will be preloaded for consultation by the
duplication-reduction features, if activated. See [Feature Notes -
1.12.0](Feature%20Notes%20-%201.12.0) for more details about
duplication-reduction options.

### BDB-JE environments (crawl 'state' directories) now use 'shared cache' by default ([HER-1594](https://webarchive.jira.com/browse/HER-1594))

Previously, each crawl's BerkeleyDB-JE environment used its own
in-memory cache. Unless changed to something smaller than the default
60% of all Java heap memory, this would cause problems for running
simultaneous crawls in the same Java VM. (And if changed to a smaller
number, cache memory might not be used efficiently between crawls.) A
recent feature of BDB-JE allows all open environments to share the same
cache allotment. We now activate this option by default.

If you launch multiple simultaneous crawls in the same Java VM – which
is only common where Heritrix is embedded in a larger crawl scheduling
system – you should now allow each crawl to specify a
'bdb-cache-percentage' equal to the total you'd like all crawls to
share. (When opening multiple environments with a shared-cache, the
cache adopts the size specified by the most-recently-opened
environment.)

## Additional contributors

In addition to the [usual
suspects](http://crawler.archive.org/team-list.html), this release
includes contributed fixes or functionality from:

-   Siznax
-   Christian Dehning

## All Tracked Changes

The following 14 tracked issues are recorded as addressed in this 1.14.3
release:

<http://webteam.archive.org/jira/secure/ReleaseNote.jspa?projectId=10021&styleName=Html&version=10090>

type

key

summary

status

Unable to locate JIRA server for this macro. It may be due to
Application Link configuration.
