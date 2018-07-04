# BeanShell User Notes

Stack suggested that we should add to the documentation, so for now I'm
recording my (specific) notes on using BeanShell here, and later I can
turn this into something generic hopefully:

Basically I'm doing pseudo-smart crawl where we will manually refetch a
page of links every day – this is a page of links to the "most linked",
"most discussed", etc pages on youtube.

``` bash
import org.archive.crawler.datamodel.*;
import org.archive.net.*;

String linkspage = "http://localhost:8080/docs/articles/youtubelinks.html";


process(CrawlURI curi) {
    // only go through the for loop in some cases, for efficency
    if (curi.toString().matches(".*youtube\\.com/watch\\?.*") ||
        curi.toString().equals(linkspage) ||
        (curi.getVia()!=null && curi.getVia().toString().equals(linkspage)) ||
        curi.getSchedulingDirective()==CrawlURI.HIGH ) {

        for (final Iterator iter = curi.getOutLinks().iterator();
                            iter.hasNext();) {
            CandidateURI link = (CandidateURI) iter.next();
            if (curi.toString().equals(linkspage)) {
                    link.setSchedulingDirective(CrawlURI.HIGH);
                link.setForceFetch(true);   // need to revisit these
                print("youtube.bsh: " + link.toString() + " set high and forcefetch");
            } else if (curi.getVia()!=null && curi.getVia().toString().equals(linkspage) &&
                       link.toString().matches(".*youtube\\.com/watch\\?.*")) {
                link.setSchedulingDirective(CrawlURI.HIGH);
                // possibly want to revisit?
                print("youtube.bsh: " + link.toString() + " set high");
            } else if (link.toString().matches(".*/get_video\\?.*")) {
                //  set all /get_video HIGH
                link.setSchedulingDirective(CrawlURI.HIGH);
                print("youtube.bsh: " + link.toString() + " set high");
            }
        }

    }
}
```

I'll be adding some explanation and expanding this page eventually.
