# Version Numbering

# Heritrix Version Numbering

This reflects the version numbering convention to be used starting just
before the 3.0.1 release.

H3 and up version numbers are of the form X.Y.Z or X.Y.Z-SUFFIX.

## Numbers

X is an integer major version number. As of 2010, the latest major
version number is '3'. If the major version number changes, there have
been major changes in functionality and operation which may require
significant adaptation of processes and other related software which
uses Heritrix or its outputs.

Y is an integer minor version number. As of October 2010, under the
major version "3", the largest minor version number is "0". (Though,
some development builds under the old version numbering scheme were
numbered "3.1.1-SNAPSHOT".) Increments to the minor release number occur
when notable new functionality has been added, but prior processes and
software should continue to work, with only small changes as detailed in
release notes.

Z is an integer micro/patch version number. Before the 3.0.1 release,
the largest micro version number under "3.0" in an official release was
"0" (for "3.0.0"). (Work in progress was named with a "1" micro number,
originally "3.1.1-SNAPSHOT" under the older conventions but now simply
"3.0.1-SNAPSHOT".) Increments to the micro version number occur when an
official release includes bugfixes and minor new functionality. We try
to maintain compatibility of configuration formats and even checkpoints
between micro-release-increments, though some adaptation may be required
as described in release notes.

(Any of these X,Y,Z numbers is not limited to the range 0-9, and the
ordering is based on the full number, not the leading digit. So "8.10.0"
comes after "8.9.99" – because "10" in the middle is greater than "9".)

## Suffixes

If a version has a SUFFIX of "SNAPSHOT" – for example, "3.0.1-SNAPSHOT"
– it is one of the development builds from our automatic continuous
build service in preparation for the version listed. (That is, many
"3.0.1-SNAPSHOT" builds will precede the single official "3.0.1"
release.) A "-SNAPSHOT" build had received only minimal automatic
testing and may have serious known bugs. Such builds are recommended
only for experts and developers who can troubleshoot many problems
themselves. (TODO: determine how -SNAPSHOT builds are distinguished once
unpacked from the timestamp/build-number that appears on their
distribution packaging.)

Other suffixes of "alpha", "beta", "rc1", "rc2", etc. indicate
ever-closer-to-release specific development versions leading up to the
named version. Each suffix (unlike "SNAPSHOT") will be a unique build.
Each connotes more confidence in the build's suitability for production
use. Advanced users are encouraged to try these releases, especially the
'rc' release-candidates, to get an early look at new features and test
anything unique about their crawls to allow any discovered problems to
be found before final release.
