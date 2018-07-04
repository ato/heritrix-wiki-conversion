# Adding URIs mid-crawl

(This is written for Heritrix 1.14.x; procedures for H2/H3 will vary.)

### Via Operator Web UI

There are two primary ways to add URIs to a crawl after it has begun
with the Web UI: changing the seed source file (seeds.txt) and
triggering a rescan, or using the 'import URIs' option from the
'View/Edit Frontier' page (only available in paused crawls).

#### Seeds edits

The seeds file is by default reread after any settings change (even
small unrelated changes); you can change this via the scope's
'reread-seeds-on-reconfig' setting.

(You can edit smallish seed files in the textarea at the bottom of all
other editable settings. Large seed files are awkward or impossible to
edit via the Web UI's text area; in such a case you can still edit the
file on disk via other methods.)

Rescanning the seeds file triggers an attempted rescheduling of all
contained URIs. However, those URIs that have already been scheduled
will not be rescheduled. Thus, only URIs new to the seeds file will be
newly scheduled. (And if, for some reason those new URIs were already
scheduled by some other discovery-path, they won't be rescheduled.)

Scopes which are defined in terms of seeds are also by default rebuilt
from seeds on settings changes. (So if using such a scope, you would
generally not want to remove original seeds even though they are already
scheduled -- otherwise your scope could be redefined to exclude the
corresponding sites.)

#### Import URIs

When the crawler is paused, a 'View or Edit Frontier' link will appear
in the console. The corresponding page offers an 'import URIs' form.

This form expects a file path local to the crawler; the file may be in
any of the three formats listed (a URI per line, a crawl.log, or an
uncompressed recovery log). If the supplied format includes 'hops-path'
and 'via' information, the imported URIs will share that information. If
the 'force revisit' box is checked, the supplied URIs will be
force-scheduled, even if they were previously scheduled.

None of the import-URI options cause URIs to be treated as seeds or
change the scope in any way. (For example, you could force-schedule an
out-of-scope URI -- but if you still have the default 'Preselector'
processor that rechecks scope, it would still be rejected from crawling
when its turn comes up.)

### Via JMX

The [JMX remote-control
interface](http://crawler.archive.org/articles/user_manual/outside.html#mon_com)
includes
[importUri](http://crawler.archive.org/apidocs/org/archive/crawler/admin/CrawlJob.html#importUri(java.lang.String,%20boolean,%20boolean,%20boolean))and
[importUris](http://crawler.archive.org/apidocs/org/archive/crawler/admin/CrawlJob.html#importUris(java.lang.String,%20java.lang.String,%20boolean,%20boolean))
operations on the CrawlJob bean that mimic the WebUI's import URIs
function. An example:

[JMX importUris
example](http://tech.groups.yahoo.com/group/archive-crawler/message/2438)
