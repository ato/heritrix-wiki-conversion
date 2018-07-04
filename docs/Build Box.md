# Build Box

H1 and H3 builds occur automatically soon after new commits on our
[Jenkins-based build system](https://builds.archive.org:1443/).
Following the link to [Heritrix 3 (distribution
bundles)](https://builds.archive.org:1443/job/Heritrix-3/lastBuild/org.archive.heritrix$heritrix/)
will show the standard distributable bundles of a build.

Builds are also uploaded to our Maven2 repository:

<http://builds.archive.org:8080/maven2/org/archive/heritrix/heritrix/>

Development build version artifact names start with the version number
they're approaching, and end "-SNAPSHOT". The actual development build
products begin with the version number, and include a timestamp. So, for
example, the latest H3 development build at the time of this writing,
approaching a 3.1.0 final release, is made up of the latest-timestamped
files available in the [3.1.0-SNAPSHOT
directory](http://builds.archive.org:8080/maven2/org/archive/heritrix/heritrix/3.1.0-SNAPSHOT/).

Certain exact builds leading up to a final release may be named
"-alpha", "-beta", "-RC1", "-RC2", etc. instead of "-SNAPSHOT" as
necessary. The final release build is simply the version number, with no
suffix, and will also be made available for download at Sourceforge.
