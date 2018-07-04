# Preserve toString()

(We are actually really bad in this regard.)

Method toString has a special role in describing objects, including in
expert/developer/debugging contexts. When overriding toString(), it
should be to better describe the object, and should avoid making an
object look like objects of other types. In particular, toString()'s
form should be neither simplified nor extended in ways that other code
is depending on parsing to deliver functionality.

In places (specifically around the UURI/CrawlURI classes) we've
overridden Object.toString() to return a more 'naked' representation of
a object, and then relied on that toString() for functionality.

Unfortunately, this hides useful info - like the class of anything that
reports a plain URI string for toString().

If a object needs a lay user display string, a method for that specific
purpose (eg 'toDisplayString') should be used. If an object needs a
functionally important String representation, as say reduced to a format
with its own logic and perhaps only interpretable with extra context,
another specific method name should be used (eg 'toURIString' or
'toCustomString').

This retains toString() in its descriptive role, either in its default
implementation or some other rich, debugging-centric rendering. This
also means toString() can be extended fearlessly without risking
application functionality. (In fact, that's a good test for any planned
use of toString() – if the value returned changed arbitrarily, woudl any
functionality break? If so, toString() is being misused.)
