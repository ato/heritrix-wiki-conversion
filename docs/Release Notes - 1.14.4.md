# Release Notes - 1.14.4

# Release Notes - 1.14.4 (May 2010)

These are the project wiki Release Notes for the 1.14.4 release.

Release 1.14.4 is a 'micro' release with a number of small bugfixes and
new requested features.

The 1.14.4 release is now available at TK.

## Notable Changes

### Support for FTP transactions in WARC records ([HER-1577](https://webarchive.jira.com/browse/HER-1577))

Heritrix now supports recording full FTP transactions in WARC records.
For each FTP URL retrieved, the control conversation is recorded in a
WARC metadata record with Content-Type: application/ftp;
msgtype=control-conversation, the payload data is recorded in a WARC
resource record with Content-Type: application/ftp;
msgtype=payload-data, and FTP fetch metadata (as well as outlinks) are
recorded in a corresponding WARC metadata record.

### Other WARC corrections ([HER-1659](https://webarchive.jira.com/browse/HER-1659))

Written WARC files now consistently identify as WARC version "1.0"
([HER-1648](https://webarchive.jira.com/browse/HER-1648)) and will grow
to the 1GB size recommended by the specification.

### Windows annoyances fixed ([HER-510](https://webarchive.jira.com/browse/HER-510), [HER-1622](https://webarchive.jira.com/browse/HER-1622), [HER-1625](https://webarchive.jira.com/browse/HER-1625))

Several problems causing errors or problems in using Heritrix on
Windows, related to improper quoting or path-separators, have been
corrected.

### Seeds with Internationalized Domain Names (IDN) better supported ([HER-1711](https://webarchive.jira.com/browse/HER-1711))

Encoding problems which interfered with specification of some
Internationalized Domain Name seeds have been corrected.

### Hosts report expanded to include novel/duplicate bytes/URLs counts ([HER-1650](https://webarchive.jira.com/browse/HER-1650))

Crawl statistics now collect, and the 'Hosts' report includes, counts of
the URLs and total content byte-sizes deemed either 'novel' or
'duplicate' by the duplication-reduction/persist-history mechanisms, if
enabled on a crawl.

### Trailing '\*' tolerated in robots.txt Disallow/Allow rules ([HER-1620](https://webarchive.jira.com/browse/HER-1620))

Heritrix will now tolerate a trailing '\*' wildcard sometimes added by
webmasters (though not necessary) in their robots.txt Disallow/Allow
rules. (Leading or internal wildcards are not yet supported.)

### CachedBdbMap changes, replacement ([HER-1677](https://webarchive.jira.com/browse/HER-1677), [HER-1658](https://webarchive.jira.com/browse/HER-1658), [HER-1705](https://webarchive.jira.com/browse/HER-1705), [HER-1609](https://webarchive.jira.com/browse/HER-1609)

A number of performance, memory-retention, and deadlock-risk issues
occasionally affecting the implementation class CachedBdbMap were
identified. Fixes have been applied, but also the class has been
replaced with a more simple implementation focused specifically on
Heritrix's common use cases, ObjectIdentityBdbCache.

## Additional contributors

In addition to the [usual
suspects](http://crawler.archive.org/team-list.html), this release
includes contributed fixes or functionality from:

-   Paul Baclace
-   Sergey Khenkin

## All Tracked Changes

The following **44** tracked issues are recorded as addressed in this
1.14.4 release:

<https://webarchive.jira.com/secure/ReleaseNote.jspa?projectId=10021&version=10105>

|                                                                                                                                                                                   |                                                                       |                                                                                                                                                                     |          |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
| T                                                                                                                                                                                 | Key                                                                   | Summary                                                                                                                                                             | Status   |
| [![Improvement](https://webarchive.jira.com/secure/viewavatar?size=xsmall&avatarId=12280&avatarType=issuetype){.icon}](https://webarchive.jira.com/browse/HER-1756?src=confmacro) | [HER-1756](https://webarchive.jira.com/browse/HER-1756?src=confmacro) | [improved crawl status reporting: more definitive FINISHED-after-logging of crawling](https://webarchive.jira.com/browse/HER-1756?src=confmacro)                    | Resolved |
| [![Improvement](https://webarchive.jira.com/secure/viewavatar?size=xsmall&avatarId=12280&avatarType=issuetype){.icon}](https://webarchive.jira.com/browse/HER-1754?src=confmacro) | [HER-1754](https://webarchive.jira.com/browse/HER-1754?src=confmacro) | [treat robots.txt non-response as 404 (optionally?)](https://webarchive.jira.com/browse/HER-1754?src=confmacro)                                                     | Resolved |
| [![Bug](https://webarchive.jira.com/secure/viewavatar?size=xsmall&avatarId=12273&avatarType=issuetype){.icon}](https://webarchive.jira.com/browse/HER-1748?src=confmacro)         | [HER-1748](https://webarchive.jira.com/browse/HER-1748?src=confmacro) | [Arc2Warc should generally write WARC "response" records for ARC HTTP responses](https://webarchive.jira.com/browse/HER-1748?src=confmacro)                         | Resolved |
| [![Bug](https://webarchive.jira.com/secure/viewavatar?size=xsmall&avatarId=12273&avatarType=issuetype){.icon}](https://webarchive.jira.com/browse/HER-1710?src=confmacro)         | [HER-1710](https://webarchive.jira.com/browse/HER-1710?src=confmacro) | [on problem loading persist log, close reader](https://webarchive.jira.com/browse/HER-1710?src=confmacro)                                                           | Resolved |
| [![Bug](https://webarchive.jira.com/secure/viewavatar?size=xsmall&avatarId=12273&avatarType=issuetype){.icon}](https://webarchive.jira.com/browse/HER-1705?src=confmacro)         | [HER-1705](https://webarchive.jira.com/browse/HER-1705?src=confmacro) | ['harmless' low-memory-canary causing heap reference leak/OOME](https://webarchive.jira.com/browse/HER-1705?src=confmacro)                                          | Resolved |
| [![Bug](https://webarchive.jira.com/secure/viewavatar?size=xsmall&avatarId=12273&avatarType=issuetype){.icon}](https://webarchive.jira.com/browse/HER-1700?src=confmacro)         | [HER-1700](https://webarchive.jira.com/browse/HER-1700?src=confmacro) | [PersistLogProcessor, PersistLoadProcessor don't fully respect "enabled" property](https://webarchive.jira.com/browse/HER-1700?src=confmacro)                       | Resolved |
| [![Bug](https://webarchive.jira.com/secure/viewavatar?size=xsmall&avatarId=12273&avatarType=issuetype){.icon}](https://webarchive.jira.com/browse/HER-1697?src=confmacro)         | [HER-1697](https://webarchive.jira.com/browse/HER-1697?src=confmacro) | [h1 - what about ftp dedupe?](https://webarchive.jira.com/browse/HER-1697?src=confmacro)                                                                            | Resolved |
| [![Bug](https://webarchive.jira.com/secure/viewavatar?size=xsmall&avatarId=12273&avatarType=issuetype){.icon}](https://webarchive.jira.com/browse/HER-1685?src=confmacro)         | [HER-1685](https://webarchive.jira.com/browse/HER-1685?src=confmacro) | [seed report says "0 NOTCRAWLED" for all seeds](https://webarchive.jira.com/browse/HER-1685?src=confmacro)                                                          | Resolved |
| [![Bug](https://webarchive.jira.com/secure/viewavatar?size=xsmall&avatarId=12273&avatarType=issuetype){.icon}](https://webarchive.jira.com/browse/HER-1683?src=confmacro)         | [HER-1683](https://webarchive.jira.com/browse/HER-1683?src=confmacro) | [inconsistent host classification for dns: urls](https://webarchive.jira.com/browse/HER-1683?src=confmacro)                                                         | Resolved |
| [![Bug](https://webarchive.jira.com/secure/viewavatar?size=xsmall&avatarId=12273&avatarType=issuetype){.icon}](https://webarchive.jira.com/browse/HER-1677?src=confmacro)         | [HER-1677](https://webarchive.jira.com/browse/HER-1677?src=confmacro) | [threads stuck in CachedBdbMap.get/\_getMem](https://webarchive.jira.com/browse/HER-1677?src=confmacro)                                                             | Resolved |
| [![Bug](https://webarchive.jira.com/secure/viewavatar?size=xsmall&avatarId=12273&avatarType=issuetype){.icon}](https://webarchive.jira.com/browse/HER-1675?src=confmacro)         | [HER-1675](https://webarchive.jira.com/browse/HER-1675?src=confmacro) | [FetchStats/CrawlSubstats not tallying fetchResponses correctly; as a result QuotaEnforcer doesn't work](https://webarchive.jira.com/browse/HER-1675?src=confmacro) | Resolved |
| [![Bug](https://webarchive.jira.com/secure/viewavatar?size=xsmall&avatarId=12273&avatarType=issuetype){.icon}](https://webarchive.jira.com/browse/HER-1666?src=confmacro)         | [HER-1666](https://webarchive.jira.com/browse/HER-1666?src=confmacro) | [seed redirect url sometimes not recorded as seed when seed also has a regular link to the redirect url](https://webarchive.jira.com/browse/HER-1666?src=confmacro) | Resolved |
| [![Bug](https://webarchive.jira.com/secure/viewavatar?size=xsmall&avatarId=12273&avatarType=issuetype){.icon}](https://webarchive.jira.com/browse/HER-1662?src=confmacro)         | [HER-1662](https://webarchive.jira.com/browse/HER-1662?src=confmacro) | [should use fully qualified hostname](https://webarchive.jira.com/browse/HER-1662?src=confmacro)                                                                    | Resolved |
| [![Bug](https://webarchive.jira.com/secure/viewavatar?size=xsmall&avatarId=12273&avatarType=issuetype){.icon}](https://webarchive.jira.com/browse/HER-1659?src=confmacro)         | [HER-1659](https://webarchive.jira.com/browse/HER-1659?src=confmacro) | [make default WARC size comply with spec; adjust default pool size for fewer odd-sized (W)ARCs](https://webarchive.jira.com/browse/HER-1659?src=confmacro)          | Resolved |
| [![Bug](https://webarchive.jira.com/secure/viewavatar?size=xsmall&avatarId=12273&avatarType=issuetype){.icon}](https://webarchive.jira.com/browse/HER-1658?src=confmacro)         | [HER-1658](https://webarchive.jira.com/browse/HER-1658?src=confmacro) | [CachedBdbMaps not expunging as expected (especially StatisticsTracker.processedSeedsRecords)](https://webarchive.jira.com/browse/HER-1658?src=confmacro)           | Resolved |
| [![New Feature](https://webarchive.jira.com/secure/viewavatar?size=xsmall&avatarId=12281&avatarType=issuetype){.icon}](https://webarchive.jira.com/browse/HER-1650?src=confmacro) | [HER-1650](https://webarchive.jira.com/browse/HER-1650?src=confmacro) | [novel/duplicate urls/bytes in the host report](https://webarchive.jira.com/browse/HER-1650?src=confmacro)                                                          | Resolved |
| [![Bug](https://webarchive.jira.com/secure/viewavatar?size=xsmall&avatarId=12273&avatarType=issuetype){.icon}](https://webarchive.jira.com/browse/HER-1649?src=confmacro)         | [HER-1649](https://webarchive.jira.com/browse/HER-1649?src=confmacro) | [com.sleepycat.je.DatabaseException when finishing crawl with dump-pending-at-close enabled](https://webarchive.jira.com/browse/HER-1649?src=confmacro)             | Resolved |
| [![Bug](https://webarchive.jira.com/secure/viewavatar?size=xsmall&avatarId=12273&avatarType=issuetype){.icon}](https://webarchive.jira.com/browse/HER-1648?src=confmacro)         | [HER-1648](https://webarchive.jira.com/browse/HER-1648?src=confmacro) | [harmonize declared WARC versions in protocol, warcinfo record metadata](https://webarchive.jira.com/browse/HER-1648?src=confmacro)                                 | Resolved |
| [![Bug](https://webarchive.jira.com/secure/viewavatar?size=xsmall&avatarId=12273&avatarType=issuetype){.icon}](https://webarchive.jira.com/browse/HER-1644?src=confmacro)         | [HER-1644](https://webarchive.jira.com/browse/HER-1644?src=confmacro) | [crawls stopped immediately after starting do not finish / clean up properly](https://webarchive.jira.com/browse/HER-1644?src=confmacro)                            | Resolved |
| [![New Feature](https://webarchive.jira.com/secure/viewavatar?size=xsmall&avatarId=12281&avatarType=issuetype){.icon}](https://webarchive.jira.com/browse/HER-1640?src=confmacro) | [HER-1640](https://webarchive.jira.com/browse/HER-1640?src=confmacro) | [digest ftp content](https://webarchive.jira.com/browse/HER-1640?src=confmacro)                                                                                     | Resolved |

Showing 20 out of 43 issues
