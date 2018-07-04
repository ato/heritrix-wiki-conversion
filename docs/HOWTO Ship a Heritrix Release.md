# HOWTO Ship a Heritrix Release

# Heritrix 1.X

## Background

The continuous build (CruiseControl) box is at:

<http://builds.archive.org:8080/cruisecontrol/buildresults/HEAD-heritrix>

The Heritrix issue tracker is at:

<http://webteam.archive.org/jira/browse/HER>

The Sourceforge project is at:

<http://sourceforge.net/projects/archive-crawler/>

The project homepage is at:

<http://crawler.archive.org>

And of course this wiki's entry page is:

<http://webteam.archive.org/confluence/display/Heritrix>

In a release number X.Y.Z, X is the 'major' release number, Y is the
'minor' release number, and 'Z' is the 'micro' release number.

All official releases have an even 'minor' release number; any build
with an odd 'minor' release number can be assumed to be a developer's
build or something off the continuous build box.

## Getting Started

Before any release, verify that:

-   all tracked issuess targeted for that release are resolved or
    rescheduled for a later release
-   the continuous build box builds successfully, and all automatic unit
    tests pass, both on a local developer box and the build box
-   the lead developer agrees the code is ready for release and has
    reviewed recent commit logs for areas of concern
-   committers have been aware a release is upcoming for a reasonable
    period (days for micro releases; a week+ for minor releases) and
    refrained from making destabilizing changes

(For 'minor' and 'major' releases, other production-scale test crawling
should have already occurred, and an announced 'code freeze' on the
relevant trunk may have been in effect for a week or more.)

Using previous wiki page Release Notes as a template, create a skeleton
wiki page Release Notes for the planned version. Leave the area where a
release date is declared with a 'planned' or 'TK'/'TBD' ('to come' or
'to be determined') notation.

Add notes there of significant changes anyone upgrading should be aware
of, with links to other wiki pages or JIRA issues with more info.

Use the dynamic-inclusion links to pull in a live copy of the 'release
notes' issue list from JIRA.

Add acknowledgement of any new or outside contributors to this release.

## Roll to Official Release Version Numbers

Make a commit to the trunk that sets the official release version number
and links the in-distribution 'release notes' to the full wiki release
notes.

Specifically in h1, this affects the files
'src/articles/releasenotes.xml' and 'project.xml'. In 'project.xml', the
string:

    <currentVersion>1.YODD.Z${version.build.suffix}</currentVersion>

...should change to...

    <currentVersion>1.YEVEN.Z</currentVersion>

When the release is a 'micro' patch release, YEVEN will actually be the
number **before** YODD. (For example, 1.15.3 in development will give
rise to 1.14.3 micro-release.) When the release is a new 'minor'
release, YEVEN will be one larger. (For example, if the work occurring
while the development trunk is labelled '1.15.4' is released as a
'minor' release rather than a 'micro' release, it will become
'1.16.0'.).

Wait for the build box's automatic build and test to complete after this
commit, and verify in commit logs that no other unintended commits were
included.

## 'Smoke Test'

Verify all expected artifacts (.tar.gz, .zip, -src.tar.gz, -src.zip)
were created and have their official distribution names.

Download these each to a remote directory and confirm they expand
without error and create expected directory trees.

For at least the .tar.gz, launch the crawler with a webui. Connect to
the webui and verify visible version identifiers are as expected.

Using the default profile, configure a minimal test crawl of a
several-pages site (&gt;1 page, &lt;100). Launch crawl and verify
expected output in crawl.log and normal termination of crawl when
finished.

## Create Release-Named Branch in SVN

At the SVN repository, copy the 'trunk/heritrix' tree to
release-'branches/heritrix-1.YEVEN.Z/heritrix'. This provides a named
branch exactly matching what went into the build.

## Roll to Development Version Number

Commit back to the trunk a version of 'project.xml' with an updated
development version number:

    <currentVersion>1.YODD.Z${version.build.suffix}</currentVersion>

(After a 'micro' release, YODD returns to its previous value, but Z
should be larger. After a full 'minor' release, YODD increments to a new
higher YODD.)

## Upload to Sourceforge

Sourceforge's instructions are at:

<http://apps.sourceforge.net/trac/sitedocs/wiki/Release%20files%20for%20download>

The 'package' will already exist. Files are uploaded (usually via SFTP
to frs.sourceforge.net using your Sourceforge account) then claimed into
a 'release' via their web app.

Follow the conventions of prior releases. We typically include only
links to the wiki/issue lists in the Sourceforge
release-notes/change-list fields. We do check the 'send notification'
option for people watching the project.

For example, uploading Heritrix 1.14.4:

    # find latest release Build Artifacts on build box
      http://builds.archive.org:8080/cruisecontrol/buildresults/HEAD-heritrix
      05/06/2010 06:14:55 (build.420)
      /0/builds/artifacts/HEAD-heritrix/20100506061455
    # visit build artifacts as ${admin_user}
      ${user}@home$ ssh webteam
      ${user}@webteam$ sudo su ${admin_user}
      ${admin_user}@webteam$ cd /0/builds/artifacts/HEAD-heritrix/20100506061455
    # upload same as previous build artifacts to SourceForge via SFTP
      ${admin_user}@webteam$ sftp iasf-admin,archive-crawler@frs.sourceforge.net
      sftp> cd /home/frs/project/a/ar/archive-crawler/
      sftp> mkdir 1.14.4
      sftp> put heritrix-1.14.4-src.zip
      sftp> put heritrix-1.14.4-src.tar.gz
      sftp> put heritrix-1.14.4.zip
      sftp> put heritrix-1.14.4.tar.gz
    # set release files via SourceForge File Manager
      select Project Admin > File Manager
        /archive-crawler (heritrix 1.x)/
          1.14.4/
      Platform set as default download check boxes
      (select "gear" icon, then Properties for each file)
            heritrix-1.14.4.tar.gz  =>  linux, mac
            heritrix-1.14.4.zip     =>  windows

## Update JIRA

Under 'Administer Project', 'Manage Versions', mark the target release
version as released with the current date.

If a followup 'micro' release is planned before the next 'minor'
release, and it does not yet exist in JIRA versions, add it. (Don't
worry; these are easy to change, reorder, and sweep issues from one to
the other.)

## Announce

Update the wiki release notes with the actual release date.

Update the project wiki front page to list the new release as the
latest, and adjust other wording about upcoming releases accordingly.

Send email to the archive-crawler project list announcing the release,
with links to the release notes and download area.

Commit a change to the 'xdocs/index.xml' file in heritrix trunk which
auto-generates the <http://crawler.archive.org> home page, to include a
news item in the appropriate place announcing the latest release.
(BROKEN NEEDS FIXING: Currently the auto-builds are not uploading the
changed website automatically to crawler.archive.org.)

# Heritrix 3

TK

Very similar but: version numbering follows [Version
Numbering](Version%20Numbering), files to change to reflect new version
number are different; build box (Continuum) is different machine; wiki
release note naming is slightly different.
