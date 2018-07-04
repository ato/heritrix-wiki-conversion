# Only Store Successful HTML Pages

Suppose you want to only capture the first 50 pages encountered from a
set of seeds and archive only those pages that return a 200 response
code and a text/html mime type.  Additionally, you only want to look for
links in HTML resources.

In order to examine only HTML documents for links, you will need to
remove the following extractors that tell Hertirix to look for links in
style sheets, JavaScript, and Flash files:

-   ExtractorCss
-   ExtractorJs
-   ExtractorSwf

Leave the ExtractorHttp since it is useful for locating resources that
can only be found using a redirect (301 or 302 response code).

You can limit the number of URIs downloaded by setting the
maxDocumentsDownload property on the crawlLimiter bean.  Setting the
value to 50 will probably not provide the intended results.  Since each
DNS response and robots.txt file is counted in the number, you should
set the value to 50 \* number of seeds \* 2.
