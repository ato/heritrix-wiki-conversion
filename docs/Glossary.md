# Glossary

###### Table of contents

-   [Table of contents](#Glossary-Tableofcontents)
-   [Bytes, KB and statistics](#Glossary-Bytes,KBandstatistics)
-   [Checkpointing](#Glossary-Checkpointing)
-   [CrawlURI](#Glossary-CrawlURI)
-   [Dates and Times](#Glossary-DatesandTimes)
-   [Discovered URIs](#Glossary-DiscoveredURIs)
-   [Discovery Path](#Glossary-DiscoveryPath)
-   [Frontier](#Glossary-Frontier)
-   [Host](#Glossary-Host)
-   [Crawl Job](#Glossary-CrawlJob)
-   [Link Hop Count](#Glossary-LinkHopCount)
-   [Pending URIs](#Glossary-PendingURIs)
-   [Profile](#Glossary-Profile)
-   [Politeness](#Glossary-Politeness)
-   [Queue States](#Glossary-QueueStates)
-   [Queued URIs](#Glossary-QueuedURIs)
-   [Regular Expressions](#Glossary-RegularExpressions)
-   [SHA1](#Glossary-SHA1)
-   [Server](#Glossary-Server)
-   [Spring](#Glossary-Spring)
-   [SURT](#Glossary-SURT)
-   [SURT Prefix](#Glossary-SURTPrefix)
-   [Toe Threads](#Glossary-ToeThreads)

###### Bytes, KB and statistics

  

Heritrix adheres to the following conventions for displaying byte and
bit amounts:

  

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Legend</p></th>
<th><p>Type</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>B</p></td>
<td><p>Bytes</p></td>
</tr>
<tr class="even">
<td><p>KB Kilobytes</p></td>
<td><p>1 KB = 1024 B</p></td>
</tr>
<tr class="odd">
<td><p>MB Megabytes</p></td>
<td><p>1 MB = 1024 KB</p></td>
</tr>
<tr class="even">
<td><p>GB Gigabytes</p></td>
<td><p>1 GB = 1024 MB</p></td>
</tr>
<tr class="odd">
<td><p>b</p></td>
<td><p>bits</p></td>
</tr>
<tr class="even">
<td><p>Kb Kilobits</p></td>
<td><p>1 Kb = 1000 b</p></td>
</tr>
<tr class="odd">
<td><p>Mb Megabits</p></td>
<td><p>1 Mb = 1000 Kb</p></td>
</tr>
<tr class="even">
<td><p>Gb Gigabits</p></td>
<td><p>1 Gb = 1000 Mb</p></td>
</tr>
</tbody>
</table>

  

This also applies to all logs.

  

###### Checkpointing

  

Heritrix checkpointing is heavily influenced by Mercator checkpointing. 
In [one of the papers on
Mercator](http://citeseer.nj.nec.com/najork01highperformance.html),
checkpointing is described this way:  "Checkpointing is an important
part of any long-running process such as a web crawl. By checkpointing
we mean writing a representation of the crawler's state to stable
storage that, in the event of a failure, is sufficient to allow the
crawler to recover its state by reading the checkpoint and to resume
crawling from the exact state it was in at the time of the checkpoint.
By this definition, in the event of a failure, any work performed after
the most recent checkpoint is lost, but none of the work up to the most
recent checkpoint. In Mercator, the frequency with which the background
thread performs a checkpoint is user-configurable; we typically
checkpoint anywhere from 1 to 4 times per day."

  

See
[Checkpointing](https://webarchive.jira.com/wiki/display/Heritrix/Checkpointing)
for a discussion of the Heritrix implementation.

  

###### CrawlURI

  

A URI and its associated data such as the parent URI and number of
links.

  

###### Dates and Times

  

All times in Heritrix are GMT, assuming the clock and timezone on the
local system are correct.  This means that all dates/times in logs are
GMT, all dates and times shown in the WUI are GMT, and any times or
dates entered by the user must be in GMT.

  

###### Discovered URIs

  

A discovered URI is any URI that has been confirmed to be within
"scope."  This includes URIs that have been processed, are being
processed, and have finished processing.  It does not include URIs that
have been "forgotten."  Forgotten URIs are URIs deemed out of scope
during fetch.  This is most likely due to the operator changing the
scope definition.

  

Note: Since the same URI can be fetched multiple times (at least in most
Frontiers), the number of discovered URIs may be somewhat lower then the
combined queued, in process, and finished items.  This is due to
duplicate URIs being queued and processed.  The variance is likely to be
especially high in Frontiers implementing "revisit" strategies.

  

###### Discovery Path

  

Each URI has a discovery path.  The path contains one character for each
link or embed followed from the seed.

  

The character legend is as follows:

  

-   R - Redirect
-   E - Embed
-   X - Speculative embed (aggressive JavaScript link extraction)
-   L - Link
-   P - Prerequisite (such as DNS lookup or robots.txt)
-   I - As of Heritrix 3.1.  Not necessarily in the source material, but
    deduced by convention (such as /favicon.ico)

  

The discovery path of a seed is an empty string.

  

###### Frontier

  

A Frontier is a pluggable module in Heritrix that maintains the internal
state of the crawl.  See
[Frontier](https://webarchive.jira.com/wiki/display/Heritrix/Frontier).

  

###### Host

  

A host can serve multiple domains or a domain can be served by multiple
hosts.  For our purposes, a host is the same as the hostname in a URI. 
DNS is not considered because it is volatile and may be unavailable. 
For example, if multiple URIs point to the same ip address, they are
considered three different logical hosts (at the same level of the
URI/HTTP protocol).

  

Conforming HTTP proxies behave similarly.  They would not consider a URI
and a IP address interchangeable.

  

This is not ideal for politeness because it applies politeness rules to
the physical host rather than the logical host.

  

###### Crawl Job

  

In order to run a crawl, a configuration must be created. In Heritrix
such a configuration is called a **crawl job**.  A crawl job is based on
the [Spring](http://www.springsource.org/) framework.  The job uses
Spring beans as configuration objects that define the crawl.

  

###### Link Hop Count

  

This is the number of links followed from the seed to reach a URI. 
Seeds have a link hop count of zero.  Link hop count is equal to the
count of `L's` in a URIs discovery path.

  

###### Pending URIs

  

This is the number of URIs that are waiting for detailed processing.  It
is also the number of discovered URIs that have not been inspected for
scope or duplicates.  Depending on the implementation of the Frontier
this might always be zero.  It may also be an adjusted number that
accounts for duplicates.

  

###### Profile

  

A profile is a template for a crawl job.  It contains all the
configurations in a crawl job, but it is not considered "crawlable." 
Heritrix will not allow you to directly crawl a profile.  Only jobs
based on profiles can be crawled.

  

A common example of a profile configuration is leaving the
`metadata.operatorContactUrl` property undefined to force the operator
to input a valid value.  This applies to the default profile that comes
with Heritrix.  Other examples would be to leave the seed list empty or
not specify a mandatory processor.

  

Profiles can be used as templates by leaving their configuration
settings in an invalid state.  In this way, an operator is forced to
choose his or her settings when creating a job from a profile.  This can
be  advantageous when an administrator must configure many different
crawl jobs to accommodate his or her crawling policy.

  

###### Politeness

  

Politeness refers to attempts by the crawler software to limit the load
on a site it is crawling.  Without politeness restrictions the crawler
might overwhelm smaller sites and even cause moderately sized sites to
slow down significantly.  Unless you have express permission to crawl a
site aggressively, you should apply strict politeness rules to any
crawl.

  

###### Queue States

| State      | Meaning                                                                  |
|------------|--------------------------------------------------------------------------|
| ready      | Queues ready to emit a URL now.                                          |
| in-process | Queues that have emitted a URL that is currently being processed.        |
| snoozed    | Due to the crawl delay, or waiting before retries.                       |
| active     | Total in-process + ready + snoozed                                       |
| inactive   | Queues currently not being considered (due to queue rotation).           |
| ineligible | Inactive queues where the queue precedence exceeds the precedence floor. |
| retired    | Disabled for some reason, e.g. that queue has hit it's allocated quota.  |
| exhausted  | Queues that are now empty.                                               |

###### Queued URIs

  

The number of URIs queued and waiting for processing.  Queued URIs
include any URIs that failed to be fetched but will be retried.

  

###### Regular Expressions

  

All regular expressions in Heritrix are Java regular expressions.

  

Java regular expressions differ from those used in other programming
languages, like Perl.  For detailed information on Java regular
expressions see the Java API description of the
`java.util.regex.Pattern` class.

  

###### SHA1

  

The Secure Hash Algorithm (SHA) used by Heritrix to encrypt files.

  

###### Server

  

A server is a service on a host.  There may be more than one service on
a host.  Different services are usually differentiated by port number.

  

###### Spring

  

Spring is a Java application framework used by Heritrix.  Crawl jobs are
based on Spring components, known as "beans."  In order to view the
Spring beans of a crawl configuration, use the [Browse
Beans](https://webarchive.jira.com/wiki/display/Heritrix/Browse+Beans)
functionality.

  

###### SURT

  

SURT stands for Sort-friendly URI Reordering Transform.  It is a
transformation applied to URIs that makes their left-to-right
representation better match the natural hierarchy of domain names.

  

A URI &lt;scheme://domain.tld/path?query&gt; has a SURT form of
&lt;scheme://(tld,domain,)/path?query.

  

Conversion to SURT form also involves making all characters lowercase
and changing the https scheme to http.  Further, the "/" character after
a URI authority component will only appear in SURT form if it appears in
plain URI form.  An example of a URI authority component is the third
slash in a regular HTTP URI.  This convention proves important when
using real URIs as a shorthand for SURT prefixes.

  

SURT form URIs are typically not used to specify exact URIs for
fetching.  Rather, SURT form is useful when comparing or sorting URIs. 
URIs in SURT format sort into natural groups.  For example, all
"archive.org" URIs will be adjacent, regardless of subdomains such as
"books.archive.org" or "movies.archive.org."

  

Most importantly, a SURT form URI, or a truncated version of a SURT form
URI can be used as a SURT prefix.  A SURT prefix will often correspond
to all URIs within a common area of interest.  For example, the prefix
http://(is, will be shared by all URIs in the `.is` top-level domain.

  

###### SURT Prefix

  

A URI in SURT form, especially if truncated, may be of use as a  "SURT
prefix," a shared prefix string of all SURT form URIs in the same area
of interest.  For example, the prefix http://(is., will be shared by all
SURT form URIs in the `.is` top-level domain.  The prefix
http://(org,archive.www,)/movies will be shared by all URIs at
www.archive.org with a path beginning with /movies. 
http://(org,archive.www,)/movies is also a valid full SURT form URI.

  

A collection of sorted SURT prefixes is an efficient way to specify a
desired crawl scope.  For example, any URI whose SURT form starts with
any of the prefixes should be included.

  

A small set of conventions can be used to calculate an "implied SURT
prefix" from a regular URI, such as a URI supplied as a crawl seed. 
These conventions are:

  

1.  Convert the URI to its SURT form.
2.  If there are at least three slashes ("/") in the SURT form, remove
    everything after the last slash.  For example,
    http://(org,example,www,)/main/subsection/ is unchanged. 
    http://(org,example,www,)/main/subsection is truncated to
    http://(org,example,www,)/main/.  http://(org.example,www,)/ is
    unchanged and http://(org,example,www) is unchanged.
3.  If the resulting form ends in an off-parenthesis (")"), remove the
    off-parenthesis.  Each of the above examples except the last one is
    unchanged.  The last one http://(org,example,www,) becomes
    http://(org,example,www,.

  

This allows many seed URIs, in their usual form, to imply the most
useful SURT prefixes for crawling related URIs.  The presence or absence
of a trailing "/" on URIs without further path-info is a subtle
indicator as to whether subdomains of the supplied domain should be
included.

  

For example, seed http://www.archive.org/ will become SURT form and
supplied SURT prefix http://(org,archive,www,)/, and is the prefix of
all SURT form URIs on www.archive.org.  However, any subdomain URI like
http://homepages.www.archive.org/directory would be ruled out because
its SURT form http://(org,archive,www,homepages,)/directory does not
begin with the full SURT prefix, including the ")" deduced from the
seed.

  

\[*Note: this paragraph only applies to H1* \] In contrast, seed
http://www.archive.org (note the lack of trailing slash) will become
SURT form http://(org,archive,www,) and implied SURT prefix
http://(org,archive,www, (note lack of trailing parenthesis).  This will
be the prefix of all URIs on www.archive.org as well as any subdomain
URIs likehttp://homepages.www.archive.org/directory because the full
SURT prefix appears in subdomain URI SURT forms.

  

###### Toe Threads

  

When crawling, Heritrix employs a configurable number of Toe Threads to
process URIs.  Each of these threads will request a URI from the
[Frontier](https://webarchive.jira.com/wiki/display/Heritrix/Frontier),
apply the set of Processors to it, and finally report it as completed to
the Frontier.
