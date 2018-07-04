# Avoiding Too Much Dynamic Content

Suppose you want to only crawl pages from a particular host
(http://www.foo.org/) and you also want to avoid crawling too many pages
of a dynamically generated calendar.  Let us assume the calendar is
accessed by passing a year, month, and day to the calendar directory. 
For example, .

When you create the crawl job you will specify a single seed:
http://www.foo.org/.  By default, your new crawl job will use the
DecideRuleSequence, which will contain a default set of DecideRules. 
One of the default rules is the SurtPrefixedDecideRule, which tells
Heritrix to accept any URI's that match the seed URI's SURT prefix:
http://(org,foo,www,)/. If the URI http://foo.org/ is encountered, it
will be rejected since its SURT prefix, http://(org,foo,) does not match
the seed's SURT prefix.  To allow both foo.org and www.foo.org to be
captured, you could add two seeds: http://www.foo.org/ and
http://foo.org/. To allow every subdomain of foo.org to be crawled, you
can add the seed http://foo.org.  Note the absence of a trailing slash.

Delete the TranclusionDecideRule, since this rule has the potential to
lead Heritrix onto another host.  For example, if a URI returns a 301
response code (move permanently) or 302 (found) response code as well as
a URI that contains a different host name than the seeds, Heritrix would
accept this URI using the TransclusionDecideRule.  Removing this rule
will keep Heritrix from straying off of our www.foo.org host.

The PathologicalPathDecideRule and the TooManyPathSegmentsDecideRule
will allow Heritrix to avoid some types of crawler traps.  The
TooManyHopsDecideRule will keep Heritrix from straying too far from the
seed.  In this way the calendar wont' trap Heritrix in an infinite
loop.  By default the max hops is set to 20, but this value can be
changed by editing the crawler-beans.cxml file.

Alternately, you can add the MatchesFilePatternDecideRule.  Set
usePresetPattern to CUSTOM and set the regexp to something like:
.**foo\\.org(?!/calendar).**\|.\*foo\\.org/calendar?year=200\[56\].\*
