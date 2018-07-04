# Unresolved Javascript Extraction Issues

Prompted by <https://webarchive.jira.com/browse/LOC-345>

Heritrix
([ExtractorJS](https://webarchive.jira.com/wiki/spaces/Heritrix/pages/4242/ExtractorJS))
has trouble finding the links that are not hardcoded strings in
javascript.

The flip side of that coin is that it extracts strings which the
javascript code does not use as URIs, often resulting in 404s noticed by
webmasters.

As an attempt to define the problem better, this is a place to put
examples where incorrect javascript extraction is an issue.

<https://webarchive.jira.com/browse/LOC-345>

<https://webarchive.jira.com/browse/HER-1300>

<https://webarchive.jira.com/browse/HER-1522>

<https://webarchive.jira.com/browse/HER-1523>

A potential solution: search for location.replace calls and similar
methods of accessing a URL. If the parameters for such a function
involve variables, attempt to resolve them.
