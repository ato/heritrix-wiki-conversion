# collecting streaming content

# Can Heritrix collect streaming audio/video?

Heritrix by default only collects material available by HTTP/HTTPS, DNS,
and FTP. Some 'streaming' media is actually delivered by plain HTTP, and
if the direct URI to the content is discoverable by Heritrix's
link-extraction modules, Heritrix can retrieve the audio/video content
by HTTP. (In some cases where sites obscure the direct link with
Javascript or Flash, manual intervention or extra configuration may be
required to help Heritrix discover the direct URI.)

A paper at [IWAW'06](http://iwaw.europarchive.org/06/) by Nicolas Baly,
"Archiving Streaming Media on the Web, Proof of Concept and First
Results", described extending Heritrix to use MPlayer on Linux to
collect content in a number of streaming protocols. While not included
with official Heritrix releases, some users of Heritrix have adapted
that work into recent releases to collect streaming media.
