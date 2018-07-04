# WARC (Web ARChive)

# WARC File Format

The WARC file format is a successor to the [ARC
format](ARC%20File%20Format). (The ARC format has been used for many
years to store the Internet Archive's web captures.) Small example ARC
and WARC (v0.17) files from a shallow (~2 hops) Heritrix crawl of the
www.archive.org website are attached to this wiki page. It is easy to
create larger, more representative ARC and WARC files using any recent
release of Heritrix.

[Download
All](../Heritrix/WARC%20(Web%20ARChive) "Download all the latest versions of attachments on this page as single zip file."){.download-all-link}

Compared to ARC, note that WARC adds:

1.  an expandable amount of header info per record
2.  optional new record types for data/metadata other than just HTTP
    responses (which was all that ARC recorded)

# ISO Standard

In May of 2009, a proposed WARC standard was approved as ISO standard
**ISO 28500:2009**, and the latest versions of Heritrix output WARC
files which conform to this standard as described at
<http://bibnum.bnf.fr/WARC/> (latest draft as of November 2008).

## Attachments:

![](images/icons/bullet_blue.gif){width="8" height="8"}
[IAH-20080430204825-00000-blackbook.arc.gz](attachments/4817/90997166.gz)
(application/gzip)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[IAH-20080430204825-00000-blackbook.warc.gz](attachments/4817/90996920.gz)
(application/gzip)  
