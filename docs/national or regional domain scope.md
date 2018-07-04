# national or regional domain scope

# I'd like to crawl a nation's or region's web content. How should I set up Heritrix?

this is a complex topic possibly requiring deep meditation, however  
for example - if you only want to capture "Hungarian" sites with the  
"hu" TLD, then you could specify "**http://(hu,**" as an allowable
scope  
SURT prefix using `SurtPrefixedDecideRule` in your crawler beans  
CXML file. see:

-   Crawl Scope  
    <https://webarchive.jira.com/wiki/display/Heritrix/Crawl+Scope>
-   SurtPrefixedDecideRule  
    <http://crawler.archive.org/apidocs/org/archive/crawler/deciderules/SurtPrefixedDecideRule.html>

however, this is a highly oversimplified notion of what might  
constitute "Hungarian sites only". you'll want to think about what  
that actually means for a class of URLs. for instance, what about  
sites that are hosted elsewhere but are clearly Hungarian? or hosted  
Hungarian blogs (livejournal, blogger, typepad, etc.)? or hungarian  
social networking sites (facebook, myspace, bebo, flickr, etc.)?

other alternatives for addressing this scoping issue include  
requesting a listing of sites from servers geographically located in  
the country of interest from a service like Alexa Internet or a domain  
registry.

it's also conceivable to write custom modules to try to detect the  
language or geolocation of potential target sites to decide what to  
capture.
