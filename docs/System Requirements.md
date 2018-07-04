# System Requirements

### Heritrix requires the following prerequisites.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>System Requirement<br />
</p></th>
<th><p>Description<br />
</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Linux distribution<br />
</p></td>
<td><p>Running Heritrix requires a Linux distribution.  Heritrix may run on other platforms, but this option is not supported.<br />
</p></td>
</tr>
<tr class="even">
<td><p>Java Runtime Environment (JRE) 1.6<br />
</p></td>
<td><p>Heritrix requires JRE 1.6.  JRE 1.6 can be downloaded at: <a href="http://www.javasoft.com/">http://www.javasoft.com</a> or <a href="http://www.ibm.com/java" class="uri">http://www.ibm.com/java</a>.  Note that Java 6 update 23 and update 24 (and possibly later) cannot be used with Heritrix 3.0 or earlier due to a bug in the JRE's GZIP functionality, which Heritrix relies on to read ARCs/WARCs.  As of Hertirix 3.1, this issue is fixed.<br />
</p></td>
</tr>
<tr class="odd">
<td><p>Hardware<br />
</p></td>
<td><p>The default Java heap for Heritrix is 256MB RAM, which is usually suitable for crawls that range over hundreds of hosts.  Assign more of your available RAM to the heap if you are crawling thousands of hosts or experience Java out-of-memory problems.  You can use the JAVA_OPTS variable to configure memory.  See ﻿<a href="Heritrix%20Configuration">Heritrix Configuration</a>.<br />
</p></td>
</tr>
</tbody>
</table>

All free/open-source libraries necessary to run Heritrix are included in
the distribution.  See
[dependencies](http://crawler.archive.org/dependencies.html) for a
complete list.  Licenses for all libraries are listed in the
dependencies section of the raw project.xml or on SourceForge.  Each
release comes in four flavors, packaged as `.tar.gz` or `.zip` and
including source or not.
