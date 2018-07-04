# Mirroring HTML Files Only

Suppose you only want to crawl URIs that match
http://foo.org/bar/\*.html.  Also, you would like to save the crawled
files in a file/directory format instead of saving them in WARC files. 
Also, assume the web server is case-sensitive.  For example,
http://foo.org/bar/abc.html and http://foo.org/bar/ABC.HTML are pointing
to two different resources.

First, create a job with a single seed, http://foo.org/bar/.  Configure
the warcWriter bean so that its class is
org.archive.modules.writer.MirrorWriterProcessor.  This Processor will
store files in a directory structure that matches the crawled URIs.  The
files will be stored in the crawl job's mirror directory.

The following DecideRules should be configured in the rules property of
the scope bean.

1.  RejectDecideRule
2.  SurtPrefixedDecideRule
3.  TooManyHopsDecideRule
4.  PathologicalPathDecideRule
5.  TooManyPathSegmentsDecideRule
6.  NotMatchesFilePatternDecideRule
7.  PrerequisiteAcceptDecideRule

Use the NotMatchesFilePatternDecideRule to keep from crawling any URIs
that don't end with .html.  It is important that this DecideRule be
placed immediately before the PrerequisiteAcceptDecideRule.  Otherwise,
the DNS and robots.txt prerequisites will be rejected since they won't
match the regular expression.

For the NotMatchesFilePatternDecideRule set the following property
values:

1.  decision: REJECT
2.  usePresetPattern: CUSTOM
3.  regexp: .\*(/\|\\.html)$

Note that the regexp will accept URIs that end with a "/" as well as
".html."  If we don't accept the "/" character, the seed URI will be
rejected.  This also allows us to accept URIs like
http://foo.org/bar/dir/, which are likely pointing to an index.html.  A
stricter regexp would be .\*\\.html$, but the seed URI must be changed
if this regexp is used.  Be aware that if Heritrix encounters a URI like
http://foo.org/bar/dir where dir is a directory, the URI will be
rejected since it is missing the terminating slash.

Finally, Heritrix must be configured to differentiate between abc.html
and ABC.HTML.  Do this by removing the LowercaseRule from the
canonicalizationPolicy bean.
