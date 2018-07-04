# Potential Cleanup-Refactorings

## org.archive.util org.archive.crawler.util

-   merge small Util classes to fewer larger ones?
-   do we need both a org.archive.util.IoUtils and
    org.archive.crawler.util.IoUtils?
-   do we need separate IoUtils and FileUtils
-   should the package be shrunk or split to subpackages?
    -   move blooms to subpackage?
    -   move SURT classes to URI-related package?

## ALists and generic data structures - JSON?

CrawlURIs need a flexible generic serializable data structure for
arbitrary markup by loosely-coordinated extensions. This has been AList
but our discmofort with it has caused us to deprecate still-useful
direct accessors.

Should we try another structure constrained to have a convenient
serialization format-- perhaps JSON? JSON+Objects? YAML?

## Spring cleaning ideas

-   evaluate for refactoring all classes &gt;1000 lines?

## Misc

-   deprecate SupplementaryLinksScoper – subsumed by mappers, main  
    LinksScoper's logging?
-   reconcile dash-underscore\_CamelCase conventions?

## against meaningful toString()

In places (specifically around the UURI/CrawlURI classes) we've
overridden Object.toString() to return a more 'naked' representation of
a object, and then relied on that toString() for functionality.

Unfortunately, given toString()'s special role as default
string-ification of any object and use through debugging
logs/itnerfaces, this hides useful info – like the class of anything
that reports a toString() URI.

I would prefer any meaningful string-version of an object to be accessed
via other methods, retaining toString() in its default implementation or
some other rich, debugging-centric rendering that can be adjusted
fearlessly without impacting application functionality.

## banish all JS dependencies from web UI

OK to use JS, should never be necessary for UI to be usable

## generalize stats-tracking

allow tallies (and rates?) of generic named quanitites – not only the
static set of values defined in interface methods
