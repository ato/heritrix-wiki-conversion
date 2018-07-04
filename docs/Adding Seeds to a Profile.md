# Adding Seeds to a Profile

# The Heritrix 2.0 Tutorial

## Using the Web User Interface

### Adding Seeds to a Profile

When you click on the "Seeds" link under a profile's name on [The Engine
Screen](The%20Engine%20Screen), you'll see the following screen:

![](attachments/3759/90996977.png)

This text area contains the seeds for your crawl. If you don't enter any
seeds, the crawl job won't last very long. The crawler starts crawling
these web pages, extracts any hyperlinks it finds, and then crawls those
linked sites. Note that the `basic_seed_sites` profile will *only* crawl
the sites you list as seeds. If `http://crawler.archive.org` linked to
`http://www.cnn.com`, for instance, the crawler would not attempt to
crawl all of `cnn.com` as well, since it was not specified as a seed.

Above I've entered three of my favorite websites to crawl. I'll be using
these three sites to demonstrate how to override configuration settings
using sheets, so you should use these three sites for your first crawl,
too.

## Attachments:

![](images/icons/bullet_blue.gif){width="8" height="8"}
[seeds.png](attachments/3759/90997246.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[seeds\_alpha2.png](attachments/3759/90996977.png) (image/png)  
