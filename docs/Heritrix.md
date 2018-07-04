# Heritrix

![](attachments/2800/16416894.gif)

-   [Introduction](#Heritrix-Introduction)
-   [Browse the wiki](#Heritrix-Browsethewiki)
-   [Webmasters!](#Heritrix-Webmasters!)
-   [Downloads](#Heritrix-Downloads)
-   [License](#Heritrix-License)
-   [Latest Releases](#Heritrix-LatestReleases)
    -   [Heritrix 3.2.0 (Jan 2014)](#Heritrix-Heritrix3.2.0(Jan2014))
    -   [Heritrix 1.14.4 (May 2010)](#Heritrix-Heritrix1.14.4(May2010))
-   [Documentation](#Heritrix-Documentation)
-   [Mailing lists](#Heritrix-Mailinglists)
-   [Development](#Heritrix-Development)

# Introduction

This is the public wiki for the Heritrix archival crawler project.

Heritrix is the Internet Archive's open-source, extensible, web-scale,
archival-quality web crawler project.

Heritrix (sometimes spelled heretrix, or misspelled or mis-said as
heratrix/heritix/ heretix/heratix) is an archaic word for heiress (woman
who inherits). Since our crawler seeks to collect and preserve the
digital artifacts of our culture for the benefit of future researchers
and generations, this name seemed apt.

All topical contributions to this wiki (corrections, proposals for new
features, new FAQ items, etc.) are welcome! Register using the link near
the top-right corner of this page. 

# Browse the wiki

Collapse all

[Expand all](#){.plugin_pagetree_expandall}   [Collapse
all](#){.plugin_pagetree_collapseall}

# Webmasters!

Heritrix is designed to respect the robots.txt exclusion directives and
META robots tags, and collect material at a measured, adaptive pace
unlikely to disrupt normal website activity.

If you notice our crawler behaving poorly – The Internet Archive uses
archive.org\_bot as User Agent when crawling – please send us email at
archive-crawler-agent@lists.sourceforge.net.

(If you see a different User-Agent in your logs that still says
'heritrix', it may be someone else using this open-source software. In
such a case, even if we can't directly change how your site is crawled,
we are happy to help you interpret your logs and identify, contact, or
block the source of any troublesome crawling.)

# Downloads

Heritrix 3.2.0:
<http://builds.archive.org/maven2/org/archive/heritrix/heritrix/3.2.0/>

Heritrix 3.x latest stable development snapshot:
<https://builds.archive.org/job/Heritrix-3/lastStableBuild/org.archive.heritrix$heritrix/>

Heritrix 1.14.4:
<http://sourceforge.net/projects/archive-crawler/files/archive-crawler%20%28heritrix%201.x%29/1.14.4/>

# License

Heritrix is free software; you can redistribute it and/or modify it
under the terms of the Apache License, Version 2.0:
<http://www.apache.org/licenses/LICENSE-2.0>. Some individual source
code files are subject to or offered under other licenses.

For more details see
<https://raw.github.com/internetarchive/heritrix3/master/dist/LICENSE.txt>

# Latest Releases

### Heritrix 3.2.0 (Jan 2014)

Heritrix 3.2.0 final release is now available. See the following Release
Notes page on the project wiki for full details: [Release Notes -
Heritrix 3.2.0](Release%20Notes%20-%20Heritrix%203.2.0)

Binary (-dist) and source (-src) distributions are available at:
<http://builds.archive.org/maven2/org/archive/heritrix/heritrix/3.2.0/>

As always, problem reports, ideas, fix/feature contributions, and other
kinds of feedback are all welcome here on the list and on the project
wiki and JIRA issue tracker:

Heritrix Wiki: [Heritrix](Heritrix)  
Heritrix JIRA: <http://webarchive.jira.com/browse/HER>

### Heritrix 1.14.4 (May 2010)

Heritrix release 1.14.4 is now available at Sourceforge:
<https://sourceforge.net/projects/archive-crawler/files/>

This is a 'micro' release with small bug fixes and improvements. Online
release notes for 1.14.4 with a list of issues addressed are available
at: [Release Notes - 1.14.4](Release%20Notes%20-%201.14.4)

Project bug/issue tracking For Heritrix is in a JIRA-based system:
<http://webteam.archive.org/jira/browse/HER>  
The project wiki with documentation, project planning, design notes, and
more is at: [Heritrix](Heritrix)

If you register to report/comment on JIRA issues, that same login will
work for wiki edits and comments, and we welcome people to 'be bold' in
adding/updating/improving project wiki pages.

# Documentation

For starting with Heritrix3, the [Heritrix 3.0 and 3.1 User
Guide](Heritrix%203.0%20and%203.1%20User%20Guide) provides
getting-started and reference information.

Javadoc API documentation, which also serves as the canonical
documentation for crawl operators on configuration of built-in modules:

-   [Heritrix 3.2.0
    javadoc](http://builds.archive.org/javadoc/heritrix-3.2.0)
-   [Heritrix 3.x development snapshot
    javadoc](http://builds.archive.org:8080/javadoc/heritrix-3.x-snapshot)

<!-- -->

-   [Heritrix 1.14.4
    javadoc](http://builds.archive.org:8080/javadoc/heritrix-1.14.4)
-   [Heritrix 1.x development snapshot
    javadoc](http://builds.archive.org:8080/javadoc/heritrix-1.x-snapshot)

The 1.x-based [Heritrix User Manual](index) covers getting started with
Heritrix and many advanced topics. This User Manual is generally focused
on Heritrix 1.X versions, not fully updated for 1.12/1.14 or the larger
changes in 2.0/3.0, but provides a reasonable basis for getting started
with Heritrix, especially 1.14.4.

There is a FAQ from the 1.x era:
<http://archive-crawler.sourceforge.net/faq.html>

The [Knowledge Base](Knowledge%20Base) contains topical articles
documenting parts of the crawler and common problems or usage scenarios.

For developers, the 1.x-based [Heritrix Developer Manual](index)
provides a guide to extending and customizing Heritrix code for your own
purposes, though of course the source code itself, which is fairly
well-commented, is the best guide.

For future documentation improvements, we have a [Documentation
Wishlist](Documentation%20Wishlist).

[An Introduction to
Heritrix](https://webarchive.jira.com/wiki/download/attachments/5441/Mohr-et-al-2004.pdf)
provides more detailed information on the structure and design of
Heritrix.

Some very-old info can still be gleaned from the old wiki
(http://web.archive.org/web/\*/http://crawler.archive.org/cgi-bin/wiki.pl?HomePage).

# Mailing lists

Heritrix discussion: <http://groups.yahoo.com/group/archive-crawler/>

Heritrix source code commits:
<https://lists.sourceforge.net/lists/listinfo/archive-crawler-cvs>

# Development

As of October 2011, immediately following the 3.1.0 release, the
Heritrix 3 source repository is hosted at github:
<https://github.com/internetarchive/heritrix3>

Older source code can be found in sourceforge svn:
<http://sourceforge.net/scm/?type=svn&group_id=73833>

Heritrix JIRA bug/feature/issue tracking:
<http://webarchive.jira.com/browse/HER>

## Attachments:

![](images/icons/bullet_blue.gif){width="8" height="8"}
[heritrix-logo.gif](attachments/2800/16416894.gif) (image/gif)  
