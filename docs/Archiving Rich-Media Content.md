# Archiving Rich-Media Content

This section of the Heritrix user guide examines the challenges facing
archivists of rich-media content and offers specific suggestions for
configuring the Heritrix crawler so that it is optimized to handle these
challenges.

Rich-media includes different kinds of advanced Web content that allows
users a greater range of experience than normal text/html Web pages. 
Rich-media encompasses video, animation, images, and audio.  Rich-media
also includes interactive technologies that go beyond basic FORM data
entry.  Examples include Wikis, such as Wikipedia, technologies like
AJAX that provide users with fine grained control over Web content, and
Flash technology, which exposes a vast array of user interface widgets
that allow spatial arrangements of data well beyond the capabilities of
first-generation Web sites.  Rich-media is also characterized by larger
file sizes than normal `text/html` pages.

###### Large File Sizes

Rich-media content, such as Flash and video, is usually much larger than
standard `text/html` pages.  Crawling such content requires large
investments in storage and bandwidth.  To mitigate these issues,
deduplication is recommended for rich-media crawls.  Deduplication
detects previously collected content that is redundant and skips the
download of such content.  Pointers to the duplicate content allow it to
appear in subsequent crawls.  For details see [Configuring Heritrix for
Deduplication](Duplication%20Reduction%20Processors).

###### Links Embedded in Rich-Media

Many rich-media technologies allow links to be embedded in file formats
that are not conducive to link extraction.  When crawling a rich-media
site, it is therefore important to identify if the site has a site-map. 
A site-map is an HTML page that contains links to all the important
pages on the site.  By adding the URI of the site-map as a seed to a
rich-media crawl, links that would not otherwise be extracted will be
archived.

###### Excessive Memory and CPU Usage

Downloading rich-media content can often cause excessive load to be
placed on the crawling computers memory and CPU.  For example,
extracting links from Flash and other rich-media resources requires
extensive data parsing, which is CPU intensive.   Atypical input
patterns can also cause excessive CPU usage when regular expressions
used by Heritrix are run.  It is therefore recommended that rich-media
crawls be allocated more memory and CPU than "normal" crawls.  The
memory allocated to Heritrix is set from the command line.  The
following example shows the command line option to allocate 1 GB of
memory to Heritrix, which should be sufficient for most rich-media
crawls.

``` bash
export JAVA_OPTS=-Xmx1024M
```

Multi-core processors are also recommended for rich-media crawls.

###### Streaming Media

Streaming media is media content delivered sequentially over time to a
media-consumer from a media-producer.  Examples of streaming media
include Internet Radio and TV.  Streaming media is concerned with the
delivery mechanism of the media format and not the format itself.  
Heritrix can capture media streamed over HTTP or FTP, but does not
recognize other streaming protocols such as Real Time Streaming Protocol
(RTSP).  This limitation has generated interest in embedding a media
player in Heritrix that does recognize most streaming formats.  For more
information on embedding a Media Player in Heritrix, see the "Archiving
Streaming Media on the Web Proof of Concept and First Results" article
in the International Web Archiving Workshop 2006 conference paper at
<http://iwaw.europarchive.org/06/PDF/iwaw06-proceedings.pdf>.

###### Social Networking Sites

Many social networking sites make use of rich-media to enhance their
user-experience.  For specific guidelines on archiving social media
sites see [Archiving Social Networking Sites with
Archive-It](https://webarchive.jira.com/wiki/display/ARIH/Archiving+Social+Networking+Sites+with+Archive-It)
.  These instructions apply to the Archive-It application, which is
built on top of Heritrix.
