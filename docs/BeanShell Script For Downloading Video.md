# BeanShell Script For Downloading Video

Here is a Beanshell script that can be used to find video links with
Heritrix. Currently the script only supports youtube. To make this work
it should be added in the extraction phase of the processor chain. I
have tested with Heritrix 2.0.2 with a sheet that limits max-hops on
youtube to 0 and this has allowed getting the front page of Youtube
videos, and it is also viewable in Wayback 1.4.0 proxy mode. The script
will also work with embedded Youtube videos that use "get\_video\_info"
to retrieve video tokens.

Any comments or suggestions for improvements to this script are welcome.

``` bash
// This is a beanshell processor that will allow downloading of vidoes in Heritrix.
// Currently only supports Youtube video pages or embedded youtube video that use "get_video_info".
//
// The script should be added at the extraction part of the processor chain in the Heritrix profile.
//
// NOTE:  The video URIs that are extracted will automatically be added as
// candidate URIs (normally this is done by LinksScoper) to ensure that they are always downloaded.
// This can be changed if needed to instead have them added as outlinks so
// that LinkScoper does a scope check after extraction.
//
// Author:  Adam Taylor (adam dot taylor at lac-bac dot gc dot ca)

import java.io.IOException;
import java.net.URL;
import java.net.URLEncoder;
import java.net.URLDecoder;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.apache.commons.httpclient.URIException;
import org.archive.crawler.datamodel.CrawlURI;
import org.archive.crawler.datamodel.SchedulingConstants;
import org.archive.net.UURI;
import org.archive.net.UURIFactory;
import org.archive.io.ReplayCharSequence;
import org.archive.modules.extractor.Hop;
import org.archive.modules.extractor.Link;
import org.archive.modules.extractor.LinkContext;
import org.archive.modules.fetcher.FetchStatusCodes;

    process(CrawlURI curi) {
        if (curi.toString().matches(".*www\\.youtube\\.com/watch\\?.*")) {

            ReplayCharSequence cs = null;
            cs = curi.getRecorder().getReplayCharSequence();

            Matcher m = Pattern.compile(".*fullscreenUrl.*video_id=([^&]+).*t=([^&]+)").matcher(cs);
            m.find();
            String videoId = m.group(1);
            String token = m.group(2);
            String getVideoUrl = "http://www.youtube.com/get_video?video_id=" + videoId + "&t=" + token + "&el=detailpage&ps=";

            Link getVideoLink1 = new Link (curi.getUURI(), UURIFactory.getInstance(getVideoUrl), LinkContext.EMBED_MISC, Hop.EMBED);
            curi.getOutCandidates().add(curi.createCrawlURI(curi.getBaseURI(), getVideoLink1, SchedulingConstants.HIGH, false));
        }
        if (curi.toString().matches(".*youtube\\.com/swf/l\\.swf.*")) {
            Matcher swfParamMatcher = Pattern.compile(".*swf=([^&]+).*video_id=([^&]+).*eurl=([^&]*).*iurl=([^&]+).*").matcher(curi.toString());
            swfParamMatcher.find();

            String swfUrl = swfParamMatcher.group(1);
            String videoId = swfParamMatcher.group(2);
            String eurl = swfParamMatcher.group(3);
            String iurl = swfParamMatcher.group(4);

            String iurlDecoded = URLDecoder.decode(iurl);
            String swfUrlDecoded = URLDecoder.decode(swfUrl);
            String iurlCrossdomainUrl = "http://" + new URL(iurlDecoded).getHost() + "/crossdomain.xml";
            String youtubeCrossdomainUrl = "http://www.youtube.com/crossdomain.xml";

            String getVideoInfoUrl1 = "http://www.youtube.com/get_video_info?&video_id="
                + videoId
                + "&el=embedded&ps=default&eurl="
                + eurl;

            if (curi.toString().matches(".*hl=[^&]+.*")) {
                Matcher hlMatcher = Pattern.compile(".*hl=([^&]+).*").matcher(curi.toString());
                hlMatcher.find();
                getVideoInfoUrl1 += "&hl=" + hlMatcher.group(1);
            }

            Link getVideoInfoLink1 = new Link (curi.getUURI(), UURIFactory.getInstance(getVideoInfoUrl1), LinkContext.EMBED_MISC, Hop.EMBED);
            Link swfLink = new Link (curi.getUURI(), UURIFactory.getInstance(swfUrlDecoded), LinkContext.EMBED_MISC, Hop.EMBED);
            Link iurlLink = new Link (curi.getUURI(), UURIFactory.getInstance(iurlDecoded), LinkContext.EMBED_MISC, Hop.EMBED);
            Link iurlCrossdomainLink = new Link (curi.getUURI(), UURIFactory.getInstance(iurlCrossdomainUrl), LinkContext.EMBED_MISC, Hop.EMBED);
            Link youtubeCrossdomainLink = new Link (curi.getUURI(), UURIFactory.getInstance(youtubeCrossdomainUrl), LinkContext.EMBED_MISC, Hop.EMBED);

            curi.getOutCandidates().add(curi.createCrawlURI(curi.getBaseURI(), getVideoInfoLink1, SchedulingConstants.HIGH, false));
            curi.getOutCandidates().add(curi.createCrawlURI(curi.getBaseURI(), swfLink, SchedulingConstants.HIGH, false));
            curi.getOutCandidates().add(curi.createCrawlURI(curi.getBaseURI(), iurlLink, SchedulingConstants.HIGH, false));
            curi.getOutCandidates().add(curi.createCrawlURI(curi.getBaseURI(), iurlCrossdomainLink, SchedulingConstants.HIGH, false));
            curi.getOutCandidates().add(curi.createCrawlURI(curi.getBaseURI(), youtubeCrossdomainLink, SchedulingConstants.HIGH, false));
        }

        if (curi.toString().matches(".*youtube\\.com/get_video_info\\?.*")) {
            Matcher videoInfoMatcher = Pattern.compile(".*video_id=([^&]+).*eurl=([^&]*).*").matcher(curi.toString());
            videoInfoMatcher.find();

            String videoId = videoInfoMatcher.group(1);
            String eurl = videoInfoMatcher.group(2);

            ReplayCharSequence cs = null;
            cs = curi.getRecorder().getReplayCharSequence();

            Matcher tokenMatcher = Pattern.compile(".*token=([^&]+).*").matcher(cs);
            tokenMatcher.find();
            String videoToken = tokenMatcher.group(1);

            String getVideoUrl1 = "http://www.youtube.com/get_video?video_id="
                + videoId
                + "&t="
                + videoToken
                + "&eurl="
                + eurl
                + "&el=embedded&ps=default";

            Link getVideoLink1 = new Link (curi.getUURI(), UURIFactory.getInstance(getVideoUrl1), LinkContext.EMBED_MISC, Hop.EMBED);

            curi.getOutCandidates().add(curi.createCrawlURI(curi.getBaseURI(), getVideoLink1, SchedulingConstants.HIGH, false));
        }
    }
```
