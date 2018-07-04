# handling web forms

# How does Heritrix handle web forms?

Heritrix does not in general fill out web forms. However, it does
include a facility for logging into sites, via either a form POST or
HTTP Basic/Digest authentication, before collecting other URIs at that
site.

Heritrix can also be configured to retrieve the URIs that are the target
ACTION of forms (which in some cases simulates an empty-form submit) and
to try strings that might plausibly be URIs found in form VALUE
attributes (often consulted by client-side code or server-side scripts
to dispatch form submits to a new URI). Each of these techniques
sometimes finds valuable content, while other times generates invalid
requests against a target site.

Forms submitted via GET (such as simple query forms) also have a
fixed-URI representation, which the crawler may discover as outlinks
from other pages, or the crawl operator may feed to the crawler as seed
URIs. So in some cases the crawler collects content equivalent to a form
submission, without actually composing a form intentionally.
