# Aaron Binns's first impressions

# Download and Installation

I figured I'd start at the beginning and visit SourceForge to find the
Heritrix tarball.

    http://sourceforge.net/projects/archive-crawler/

It looks like a typical SourceForge page, and following the download
links I was able to grab the tarball

    http://downloads.sourceforge.net/archive-crawler/heritrix-2.0.0-RC1-heritrix.tar.gz

## Tarball name

One thing that struck me as a little bit odd was the name of the
tarball:

    heritrix-2.0.0-RC1-heritrix.tar.gz

the word "heritrix" is in there twice. Now, I know this sounds picky,
but I wondered why it was there twice. I know some large-scale projects,
like Apache, have a over-arching project name and a more specific name,
like

    apache-httpd-2.2.2.tar.gz

but in the case of Heritrix, I couldn't figure out what the repeated
name was supposed to indicate, if anything.

## Unpacking

Once I stopped obsessing about the name, I went ahead and unpacked the
tarball

    $ tar xzf heritrix-2.0.0-RC1-heritrix.tar.gz
    tar: A lone zero block at 83998

Note the message from `tar`. This seems benign enough as I couldn't find
any obviously corrupted or truncated files. Also, when I started using
Heritrix, I didn't run into any errors that seemed to be related to
corrupted/truncated files.

I also tested the gzipped file to make sure that wasn't the problem

    $ gzip -vt heritrix-2.0.0-RC1-heritrix.tar.gz
    heritrix-2.0.0-RC1-heritrix.tar.gz:      O

In case it has anything to do with the version of `tar` I'm using:

    $ tar --version
    tar (GNU tar) 1.19

Even though the tarball name is a bit odd (I know, still obsessed), the
directory name created by the unpacking was as expected:

    heritrix-2.0.0-RC1

and the contents followed common Unix conventions:

    $ ls -Fl heritrix-2.0.0-RC1/
    -rw-r--r-- 1 user user 27479 Dec  6 15:47 LICENSE.txt
    -rw-r--r-- 1 user user  3146 Dec  6 15:47 README.txt
    drwxr-xr-x 2 user user   632 Jan  9 13:12 bin/
    drwxr-xr-x 3 user user   224 Jan  9 13:12 conf/
    drwxr-xr-x 3 user user    72 Dec  6 18:21 extras/
    drwxr-xr-x 4 user user   136 Nov 27 13:46 jobs/
    drwxr-xr-x 2 user user  1504 Jan  9 13:12 lib/

Sweet.

# Poking Around

When installing a new package, I usually poke around to familiarize
myself with the various sub-dirs and files contained therein. As I
mentioned above, Heritrix looks to follow the common Unix conventions: a
`bin` directory with some executables; `conf` with properties files; and
`lib` with the Java libraries (`.jar` files). Ok, looks all good, let's
check out the binaries.

## Binaries

The `bin` directory contains:

    $ ls -Fl bin
    /tmp/htx/heritrix-2.0.0-RC1 $ ls -Fl bin/
    -rwxr-xr-x 1 user user   820 Nov 27 13:46 arcreader*
    -rwxr-xr-x 1 user user   918 Nov 27 13:46 arcreader.cmd*
    -rwxr-xr-x 1 user user 21847 Nov 27 13:46 cmdline-jmxclient-0.10.5.jar*
    -rwxr-xr-x 1 user user  1308 Nov 27 13:46 dependencies.xsl*
    -rwxr-xr-x 1 user user   897 Nov 27 13:46 extractor*
    -rwxr-xr-x 1 user user   772 Nov 27 13:46 extractor.cmd*
    -rwxr-xr-x 1 user user  1078 Nov 27 13:46 foreground_heritrix*
    -rwxr-xr-x 1 user user  1271 Nov 27 13:46 foreground_heritrix.cmd*
    -rwxr-xr-x 1 user user  5918 Nov 29 13:00 heritrix*
    -rwxr-xr-x 1 user user 11314 Nov 27 13:46 heritrix.cmd*
    -rwxr-xr-x 1 user user  4172 Nov 27 13:46 hoppath.pl*
    -rwxr-xr-x 1 user user   866 Nov 27 13:46 htmlextractor*
    -rwxr-xr-x 1 user user   743 Nov 27 13:46 htmlextractor.cmd*
    -rwxr-xr-x 1 user user  1335 Nov 27 13:46 jmxclient*
    -rwxr-xr-x 1 user user  5270 Nov 27 13:46 make_reports.pl*
    -rwxr-xr-x 1 user user  2495 Nov 27 13:46 manifest_bundle.pl*
    -rwxr-xr-x 1 user user  3021 Nov 27 13:46 xdocToTxt.xsl*

For the most part, it's pretty straightforward. Most of the names seem
to be pretty obvious as to what they do: `heritrix`, `arcreader`,
`htmlextractor`, etc.

Some of them have two forms: Unix shell script and Windows shell script.

    -rwxr-xr-x 1 user user  5918 Nov 29 13:00 heritrix*
    -rwxr-xr-x 1 user user 11314 Nov 27 13:46 heritrix.cmd*

That's pretty typical of Java applications. Sometimes I see packages
arranged with separate Unix and Windows bin directories, which can be
nice for Windows users so they aren't confused by the Unix binaries,
which won't run on their system – unless they are using Cygwin, in which
case they are likely already hip to the difference in shell scripts.

### Complaint: non-binaries

I did wonder why there were non-binaries in the `bin` directory, such
as:

    -rwxr-xr-x 1 user user 21847 Nov 27 13:46 cmdline-jmxclient-0.10.5.jar*
    -rwxr-xr-x 1 user user  1308 Nov 27 13:46 dependencies.xsl*
    -rwxr-xr-x 1 user user  3021 Nov 27 13:46 xdocToTxt.xsl*

I can't say this is wrong, so much as unconventional. IMO, only binaries
(and helper scripts) should go  
in bin. Ya know, things you can run from the command-line.

Also, the `jmxclient` doesn't have a Windows script equivalent. And why
is the accompanying `cmdline-jmxclient-0.10.5.jar` in the `bin`
directory and not in lib with all the rest of the `jar` files?

### The rest of the directories

Compared to `bin` the rest of the directories aren't that interesting to
a first-time user. They all contain what's expected based on their
names. I notice that `conf/jobs` mirrors `jobs`, which suggests a
sensible relationship between a job and its configuration.

## README

Yep, I usually save the `README.txt` file for last. It might sound
strange, but it seems that the trend in recent years is for README files
to follow a rather uninformative template, filled with license (usually
GPL) information and other stuff that doesn't really have much to do
with actually running the software.

In fact, I usually run the most obvious binary with `--help` first to
see what kind of help message it gives. But we'll get to that in a
minute.

Fortunately for Heritrix, the `README.txt` file is actually useful. It
specifically mentions a few things that I didn't try the first time
around. More on that below.

# Running Heritrix, Part 1

Here's where I ran into my first real "what?" momement with Heritrix.

Even though the `README.txt` mentions using the `-a` command-line
option, my first inclination is to execute

       
    ./bin/heritrix --help

and see what are all the options.

    heritrix-2.0.0-RC1 $ ./bin/heritrix --help
    which: no java in (/usr/local/bin:/usr/bin:/bin:/opt/bin)
    Cannot find JAVA. Please set JAVA_HOME or your PATH.

Ok, fair enough, I need to set-up Java.

Lets set-up Java and try again

    heritrix-2.0.0-RC1 $ export JAVA_HOME=/opt/jdk-1.5.0_09-linux-i586
    heritrix-2.0.0-RC1 $ ./bin/heritrix --help
    WARNING: No $HERITRIX_HOME/conf/jmxremote.password found.
    WARNING: Disabling remote JMX.
    Wed Jan  9 15:09:42 PST 2008 Starting heritrix./bin/heritrix: line 184: [: ne: binary operator expected
    ../bin/heritrix: line 183: kill: (15139) - No such process
    ./bin/heritrix: line 184: [: ne: binary operator expected
    ../bin/heritrix: line 183: kill: (15139) - No such process
    ./bin/heritrix: line 184: [: ne: binary operator expected
    ../bin/heritrix: line 183: kill: (15139) - No such process
    ./bin/heritrix: line 184: [: ne: binary operator expected
    .

Hmm, that doesn't look so good. Now only did I not get any useful help
message, the error messages just seem to continue ad infinitum. I killed
it with ^C.

## Bashisms?

Now, I did remember an email on the Heritrix mailing list that I thought
mentioned errors similar to these being caused by bash-specific syntax
being used in the shell script. Now even though I'm using bash as my
regular shell, maybe the script is invoking a different, or limited form
of bash as the shell, which is puking on the syntax? Looking at the top
of the script

    heritrix-2.0.0-RC1 $ head bin/heritrix
    #!/usr/bin/env sh

Hmm, we're invoking `sh`, not `bash` explicitly. Often `sh` is often a
symlink to `bash`, such as

    $ ls -Fla /bin/sh
    lrwxrwxrwx 1 root root 4 Dec 29 12:55 /bin/sh -> bash*

and when `bash` runs, it checks how it was invoked and supports a
limited shell syntax. Maybe that's the problem?

Nope. I changed the shell script to

    #!/usr/bin/env bash

and the same problem.

## It worked before, didn't it?

Then I remembered that before the holidays, I tried one of the pre-RC1
snapshots. I didn't run into this problem then, so maybe there are
changes to the bin/heritrix script that are the cause.

Yep. Check it

    $ diff heritrix-2.0.0-RC1/bin/heritrix heritrix-2.0.0-SNAPSHOT/bin/heritrix
    169d168
    <     HERITRIX_PID=$!
    183,194d181
    <         kill -0 $HERITRIX_PID
    <         if [ $? ne 0 ]
    <         then
    <             echo
    <             echo "ERROR: JVM terminated without running Heritrix."
    <             echo "This could be due to invalid JAVA_OPTS or JMX_PORT, etc."
    <             echo "See heritrix_out.log for more details."
    <             echo "Here are its last three lines: "
    <             echo
    <             tail -3 $stdouterrlog
    <             break
    <         fi

Where the earlier snapshot was
`heritrix-2.0.0-20071024.165839-74-heritrix.tar.gz`.

So, I commented-out those diffs and ran `bin/heritrix --help again`:

    $ ./bin/heritrix --help
    WARNING: No $HERITRIX_HOME/conf/jmxremote.password found.
    WARNING: Disabling remote JMX.
    Wed Jan  9 15:46:52 PST 2008 Starting heritrix......................

Hmm, the dots just keep going, about one per second. Warnings about JMX
being disabled (fine with me), but no help info. Unexpected this is.

Eventually I killed it with ^C.

## Log files instead of standard out?

But what's this? Some log files in the Heritrix installation directory

    $ ls -Fla *.log
    -rw-r--r-- 1 user user    0 Jan  9 15:46 heritrix_dmesg.log
    -rw-r--r-- 1 user user 5224 Jan  9 15:46 heritrix_out.log

Ok, I guess the `heritrix_dmesg.log` is for "system" messages much like
the Linux kernel. No surprise it's empty. But what's in the
`heritrix_out.log` file?

    $ cat heritrix_out.log
    Wed Jan  9 15:09:41 PST 2008 Starting heritrix
    Linux darkstar 2.6.23-gentoo-r3-Plovdiv #1 SMP Tue Jan 8 18:22:05 PST 2008 x86_64 AMD Athlon(tm) 64 X2 Dual Core Processor 4600+ AuthenticAMD GNU/Linux
    java version "1.5.0_09"
    Java(TM) 2 Runtime Environment, Standard Edition (build 1.5.0_09-b03)
    Java HotSpot(TM) Server VM (build 1.5.0_09-b03, mixed mode)
    JAVA_OPTS= -Xmx256m
    core file size          (blocks, -c) 0
    data seg size           (kbytes, -d) unlimited
    scheduling priority             (-e) 0
    file size               (blocks, -f) unlimited
    pending signals                 (-i) 16381
    max locked memory       (kbytes, -l) 32
    max memory size         (kbytes, -m) unlimited
    open files                      (-n) 1024
    pipe size            (512 bytes, -p) 8
    POSIX message queues     (bytes, -q) 819200
    real-time priority              (-r) 0
    stack size              (kbytes, -s) 8192
    cpu time               (seconds, -t) unlimited
    max user processes              (-u) 16381
    virtual memory          (kbytes, -v) unlimited
    file locks                      (-x) unlimited
    usage: Heritrix
     -a,--webui-admin            Specifies the authorization password which
                             must be supplied to access the webui. Required if launching the webui.
     -j,--jobs-dir               The jobs directory.  Defaults to ./jobs
     -u,--no-engine              Do not run the crawl engine; only run the
                             admin web UI.
     -r,--run-job                Specify a ready job or a profile name to
                             launch at launch.  If you specify a profile name, the profile will first
                             be copied to a new ready job, and that ready job will be launched.
     -w,--webui-war-path         The path to the Heritrix webui WAR.  Ignored
                             if -n is specified.
     -h,--heritrix-properties    The full path to the heritrix properties file
                             (eg, conf/heritrix.properties).  If present, this file will be used to
                             configure Java logging.  Defaults to ./conf/heritrix.properties
     -b,--webui-bind-hosts       A comma-separated list of hostnames for the
                             webui to bind to.  Ignored if -r is not specified.
     -p,--webui-port             The port the webui should listen on.  Ignored
                             if -r is not specified.
     -n,--no-web-ui              Do not run the admin web user interface; only
                             run the crawl engine.  If set, the crawl engine will need to be controlled
                             via JMX or a remote web UI.

Hey, that's just the info I was expecting to see on the terminal!

## Complaint: command-line behavior

That's my first real complaint. The command-line behavior of Heritrix is
rather unconventional, especially with respect to `-h/--help`. IMO all
well-behaved Unix binaries as least print something (however minimal) to
standard out when invoked with the `-h` or `--help` arguments. It's good
etiquette.

I realize that it is desirable to have the help information printed by
the Java program, not separated out in the script. However, it would be
nice if the script would at least check for `h` and `-help` and if
either are present, invoke the Java program accordingly to make it print
the help information to the terminal.

# RTFM

Ok, since I ran headlong into all the sharp corners of Heritrix the
first time around, let's take a break and read some of the
documentation.

## README

Like I said above, I usually don't put muck stock in the README files
distributed with most open source packages nowadays. If there is a HOWTO
then I'll usually go for that first.

But, the Heritrix `README.txt` is pretty useful. First off, it points us
to some online documentation. Perhaps a HOWTO or tutorial can be found
there.

It mentions the use of `-a` to set a password for the web UI, but
doesn't mention if this is the only argument required to launch the web
UI. Perhaps some description of the various modes would be useful: web
UI only, crawler engine only, web UI and crawler. My guess would be that
most first-timers (like myself) want the web UI and crawler since we'll
be crawling from a single machine.

### Complaint: Missing CR

A minor complaint really: `README.txt` is missing a CR/LF at the end of
the file.

## Online

The README sends us here for the most up-to-date information

    http://webteam.archive.org/confluence/display/Heritrix/Home

so let's check it out.

Since I'm testing the 2.0.0-RC1 release, the two links of interest on
the main project wiki page are to the 2.0.0 beta release and another
link to a 2.0.0 page.

    http://webteam.archive.org/confluence/display/Heritrix/2.0.0-beta+Release+Notes
    http://webteam.archive.org/confluence/display/Heritrix/2.0.0

Since I'm not using a "beta release" exactly – it's 2.0.0-RC1 remember –
let's check out the second link.

Hmm, not a whole lot of useful info for the first-timer, but there a
link to the release notes for the release candidate.

    http://webteam.archive.org/confluence/display/Heritrix/2.0.0-RC1+Release+Notes

Maybe that's the ticket.

Well, the release candidate page isn't all the helpful at first. Sure,
the information on migrating from Heritrix 1.x is probably very useful
to Heritrix veterans, but since I'm a newbie, I'm not migrating from
Heritrix 1.x.

But, wait, what's this? A Getting Started section. And linked in it is a
Tutorial.

    http://webteam.archive.org/confluence/display/Heritrix/2.0+Tutorial

Sweet.

## Tutorial

Ok, here we go, this is the good stuff.

In my opinion, as a newbie, this is the most important and useful
document. Without it, I doubt I would have been able to setup a crawl,
or at least not nearly as fast as I did. You can pretty much follow this
tutorial step-by-step and successfully crawl a site using one of the two
provided job templates.

### Suggestion: Emphasize tutorial

Add something to the README, or even add a HOWTO document to the
distribution package, which strongly suggests that first-timers read
through the tutorial first.

# Running Heritrix, Part 2

Well, now that I've edumacated myself on Heritrix, let's try again. For
the most part, I follow the instructions in the tutorial.

But first, let's remove the log files created from the first (failed)
attempt at running Heritrix

    heritrix-2.0.0-RC1 $ rm *.log

Now, I want to run Heritrix in "web UI" mode as I plan to only run it on
my machine and not in a distributed system of crawlers. Also, I want to
use the web UI rather than JMX to configure, run and monitor the crawl.
Why use the web UI rather than JMX? I just think the web UI will be
easier to use.

## Launching Heritrix in web UI mode

Following the advice in from the `--help` info, the README.txt and the
tutorial, I started Heritrix with

    heritrix-2.0.0-RC1 $ ./bin/heritrix -a admin
    WARNING: No $HERITRIX_HOME/conf/jmxremote.password found.
    WARNING: Disabling remote JMX.
    Wed Jan  9 21:40:04 PST 2008 Starting heritrix...
    No JNDI context.
    Engine registered at org.archive.crawler:instance=11985823,jmxport=-1,name=Engine,type=org.archive.crawler.framework.Engine,host=darkstar.example.com
    Web UI listening on localhost:8080.

Looks good. The web UI is listening on localhost:8080

Since I'm doing this on my Linux box behind a firewall, I'm not all that
concerned about the security.

## Heritrix Web UI

Since the tutorial documents the step-by-step process of setting up a
job via the web UI, including screenshots, I'm not going to repeat all
of that here.

I basically follow the tutorial, up to the point of selecting one of the
pre-defined jobs to use as a template. Hmm, which one...

# Examine the site to be crawled

Before setting-up a job, let's step back for a minute and think about
the site I want to crawl. The site is

    http://findarticles.com

Poking around the site, you can see that it's organized by section: art,
autos, business, health, etc. Looking at a human-friendly sitemap from
their "sitemap" link in the page footer, this top-down categorization is
pretty clear.

Navigating through the categories, all the way down to the articles, it
looks like everything of interest, i.e. the articles themselves, is
under the URL prefix

    http://findarticles.com/p/articles/

such as:

-   Site map  
    <http://findarticles.com/p/articles/?sm=sitemap>
-   Autos category  
    <http://findarticles.com/p/articles/tn_auto>
-   "American Rider" publication  
    <http://findarticles.com/p/articles/mi_hb4743>
-   "All that glitters is ...(Objects of Desire)" article  
    <http://findarticles.com/p/articles/mi_hb4743/is_200705/ai_n19268670>

So, if our crawl seed(s) is(are) good, then it should be pretty easy to
grab all the articles at least.

Now that begs the question of what exactly we are trying to archive
here. I assume the articles are it. Looking at the pages, there are
external bits of content that are probably not worth archiving: inline
Google ads, banner ad, header and footer graphics. Heck, I'd personally
probably be happy with just the HTML+CSS and omitting all graphics and
JavaScript all together. It depends on the goals of the crawl.

For this crawl, let's plan on grabbing all the articles, which we will
try an accomplish by using the human-friendly sitemap as the seed:

    http://findarticles.com/p/articles/?sm=sitemap

The idea is that the sitemap will have links to the various top-level
categories: art, autos, health, etc.; which can be followed to crawl the
list of publications and eventually the articles.

# Running Heritrix, Part 3

Now that we've chosen the seed and the basic strategy for crawling,
let's go back to the tutorial and pick the appropriate job template.

## Job template: basic\_seed\_sites

It sounds like basic\_seed\_sites is the way to go. We want to stay on
findarticles.com and not follow links to other domains/sites. The
exception being that images referenced by a page will be pulled in.
Good.

## The Seed

I follow the tutorial's instructions for entering the seed

    http://findarticles.com/p/articles/?sm=sitemap

The Sheet

I diverge a little from the tutorial by editing properties of the global
sheet rather than creating a new sheet for over-rides. I don't know if
it makes much difference in this simple case.

In the global sheet, I add the required properties:

    operator-contact-url    http://crawler.archive.org
    operator-from           [email address removed due to spam]@lists.sourceforge.net

along with one to enable checkpointing every hour.

    checkpointer-period    1

## The SURT

Lastly, I set the SURT, based on my understanding of the example  
in the tutorial.

    http://findarticles.com

## Copy the job

As simple as described in the tutorial.

### Suggestion: Job description field

It would be nice to have a comment/description field in addition to the
name. I'd probably use a fairly short name, but then be inclined to
write a longer description of the crawl for future reference.

I might even crawl the same site multiple times with different settings.
Having a long description field would be useful for telling them apart
and remembering what was different about each crawl. They all might be
named "findarticles", but in one I might use a different seed than the
other.

## Launch the job

Once copied, just click launch to launch it!

### Suggestion: Automatic job console refresh

Putting an HTTP refresh header on the job console screen would be nice.
That way it would refresh itself every few seconds (configurable in a
property?) so you don't have to keep hitting F5.

# Findarticles and robots.txt

As soon as I launched the findarticles job, almost immediately the job
completes. What? Hmmm, maybe I made a type-o somewhere, like entering
the wrong seed. So, I go back and double-check everything. Looks all
good. Let's try again.

I copy the basic\_seed\_sites job profile again and start the new job.
Same problem. Hmm.

I look at the logs and reports in the Heritrix web UI and the only
suspicious thing I can find is that in the URL log, it stops after
getting the robots.txt file. Wait a minute, I thought findarticles's
robots.txt file allowed for our crawler.

To double-check, I load up in my browser

    http://findarticles.com/robots.txt

Hmm, it seems ok, it only prohibits the crawling of the /print URL
(makes sense) and an MSN crawler of some sort:

    # Findarticles: robots.txt
    #
    # This file is used to allow crawlers to index our site.
    # It is NOT used for any other purpose, such as filtering
    # advertiser impressions or clicks.
    #
    # See http://listings.looksmart.com/help/faq.jhtml?showFaq=fraud for information
    # on the methods used to ensure the accuracy of advertiser click tracking and reporting.

    Sitemap: http://findarticles.com/sitemapindex.xml

    User-agent: *
    Disallow: /print

    User-agent: msnbot
    Disallow: /p/linker

But wait a minute, that robots.txt seems awfully short. And it's rather
odd that they would only prohibit an MSN crawler and no others. I mean,
if a site prohibits at least one crawler, they usually prohibit more
than just one. On a lark, I refresh the page. Lo and behold, suddenly
the robots.txt is much longer, and includes Disallow directives for
(among others) Mozilla 4 and 5

    ...
    User-agent: mozilla/4
    Disallow:/
    User-agent: Mozilla/4.0 (compatible; BullsEye; Windows 95)
    Disallow:/
    User-agent: Mozilla/4.0 (compatible; MSIE 4.0; Windows 95)
    Disallow:/
    User-agent: Mozilla/4.0 (compatible; MSIE 4.0; Windows 98)
    Disallow:/
    User-agent: Mozilla/4.0 (compatible; MSIE 4.0; Windows NT)
    Disallow:/
    User-agent: Mozilla/4.0 (compatible; MSIE 4.0; Windows XP)
    Disallow:/
    User-agent: Mozilla/4.0 (compatible; MSIE 4.0; Windows 2000)
    Disallow:/
    User-agent: Mozilla/4.0 (compatible; MSIE 4.0; Windows ME)
    Disallow:/
    User-agent: mozilla/5
    ...

If memory serves, that last one will prohibit my Heritrix job as
Heritrix's default user-agent is of the form

    Mozilla/5.0 (compatible; heritrix/@VERSION@ +@OPERATOR_CONTACT_URL@)

Doh.

Just to make sure I'm not heading down a rabbit hole, I refresh my
browser a couple times with the robots.txt URL and sure enough,
sometimes it serves the whole file and other times it stops after the
MSN line.

## What to do with robots?

The Internet Archive's policy is to follow the robots.txt exclusion
rules by default. The exceptions are typically if someone is crawling
their own site (and they don't want to change their own robots.txt for
their own crawl) or if explicit permission is given by the webmaster. In
those situations, Heritrix can be easily configured to ingore the
robots.txt all together.

So one option would be to ignore the robots.txt file (going against
Archive politeness policy), but I'd rather not.

A better option is to change the default user agent reported by Heritrix
to avoid being caught in the blanket Disallow rule for anything matching
mozilla 5. After chatting with Gordon about the robots.txt file, he
suggested using a custom user-agent, his reasoning being:

1.  The findarticles site doesn't exclude all robots from the whole
    site, which they could have easily done. They only excluded specific
    robots, likely ones that have burdened their server at some point in
    the past.
2.  If we ignore their policy and continue to use our standard
    user-agent, their server might be coded to detect a banned robot and
    could feed ours bad data or an endless loop of links, be banned by
    IP address, or incur the wrath of their webmaster in various ways.
3.  Therefore, use a different user-agent all together, one that doesn't
    match the generic Mozilla 5.0\* pattern and is clearly indicative of
    our organization, such as Archive-Heritrix (@VERSION@
    +@OPERATOR\_CONTACT\_URL@)

That sounded very reasonable to me, so I changed the user-agent
accordingly.

## Diagnosing robots.txt prohibition

In looking at the logs and reports, the only thing that suggested that
my crawl was terminated due to the robots.txt was the fact that it was
the last URL in the URL log. The line in the log for that URL did have
an error message, but it was pretty obtuse.

### Suggestion: Help robots exclusions

For newbies, it would help a lot to have a fairly obvious message show
up in the console and logs that a crawl was terminated do to a
robots.txt policy.

Now, I can imagine arguments to the contrary, probably because there are
many scenarios where only part of a crawl is prohibits by the
robots.txt, or a crawl manages to traverse a lot of pages, then hit some
URLs that are prohibited. In those cases we wouldn't want to falsely
warn the user that the robots.txt policy caused the crawl to stop.
However, if there are some simple tests that will catch the most obvious
cases where the robots.txt policy stops a crawl after only a few URIs,
then that might help newbies a lot.

# Running Heritrix, Part 4

So, after changing the user agent in the global sheet it's time to
launch the job. Let's go!

Things look much better this time around. The job quickly fills up the
queue and it looks like the crawl will take a long time. I monitor it a
bit by refreshing the job console page. I notice that the URI/sec is
pretty low, around 0.5 or so.

I asked Gordon about the seemingly slow crawl speed and he informed me
that two factors often result in slower than expected crawls.

-   The min-delay-ms and max-delay-ms properties. By default, Heritrix
    uses these to be polite and not slam the site being crawled.

<!-- -->

-   Single domain crawls only have one retrieval going at a time. By
    default, only one URL from a domain is crawled at a time, again for
    politeness reasons.

Makes sense.

## Hurry up and wait

Now that my job is off and running, there's not much to do other than
refresh the job console every now and again to see how many URIs are
archived and how many are queued.

The logs and reports are kind of interesting, but with such a relatively
small and simple crawl, they don't tell me a whole lot other than, "it's
working". Also, I can take a gander at the .arc files and see the
archived data, such as the HTML page sources, DNS queries, etc.

Since it's nearly midnight as I write this, and the job seems to be off
and running, and the estimated time to complete (as reported in the job
console) is measured in days, I think I'll go to bed.

# Running Heritrix, Part 5: The next day

Good morning. Well, it's some 10 hours later and my Heritrix crawl of
findarticles.com is still plugging away. The job console shows progress
and I don't see anything obviously alarming in the logs nor reports.

The hourly checkpointing seems to be working as well. In checkpoints
directory I can see them

    heritrix-2.0.0-RC1/jobs/active-findarticles-ignore-robots-20080110084430/checkpoints/0001
    heritrix-2.0.0-RC1/jobs/active-findarticles-ignore-robots-20080110084430/checkpoints/0002
    heritrix-2.0.0-RC1/jobs/active-findarticles-ignore-robots-20080110084430/checkpoints/0003
    heritrix-2.0.0-RC1/jobs/active-findarticles-ignore-robots-20080110084430/checkpoints/0004
    ...

and so forth, up to 10, and it's been a litle over 10 hours since I
started the job.

Not much else to do other than wait.

### Complaint: Error after reauth

If the HTTP session expires, then refreshing the job console, then
re-authenticating leads to a error page.

See <http://webteam.archive.org/jira/browse/HER-1399>

# Shutdown

After lettting Heritrix run for a while, I decided to shut her down.
Since this is a simple test crawl to get my feet wet, there's no sense
in letting the crawl run for the days and days it would take to crawl
the entire findarticles site.

I stopped the job by clicking the Terminate link on the job console.
After which, I killed the Heritrix server Java process.

### Suggestion: Confirm job termination

It would be nice to have some sort of confirmation when terminating a
job, since an otherwise errant mouse click can terminate the job.

# Post-mortem

After concluding the crawl and chatting with some of my colleagues, here
are some parting thoughts. Keep in mind these are from the perspective
of a Heritrix 2.0 first-time user.

## Audience

It seems that the audience – or least potential audience – for Heritrix
ranges from the experienced crawl engineers of the Archive's web team,
to crawl first-timers who might not have much of a development
background at all.

In the ideal world, we'd be able to have Heritrix suppose the full range
of users, from the highly-skilled expert, to the curious first-time
crawler. But, since our resources are limited, where do we want to focus
our efforts? Since our crawl engineers are doing the paid-for contract
crawls, their needs are definitely important. But, if our mission is to
also serve the greater community of archivists and librarians, then we
need to be able to support the less experienced as well.

Another division of our potential audience is between those that have
used Heritrix 1.x and those that are starting with Heritrix 2.0. It
seems that a lot of the most prominent documentation on the wiki is
aimed at Heritrix 1.x users migrating to 2.0. As someone starting with
2.0, I was inclined to ingore most of it.

## Interactive vs. Automatic

Another interesting tension I've noticed in Heritrix is supporting both
interactive and automatic operation. For a lot of newbies, the
interactive mode, typically using the web UI, is probably the favored.
However, I can easily imagine that more sophisticated users, such as our
crawl engineers, find using the programmatic or automated interfaces to
Heritrix, such as JMX, more useful.

Consequently, we have another resource allocation question: do we spend
time+effort on making the interactive interface(s) better, or do we
extend the capabilities exposed through the programmatic interfaces like
JMX? Similarly, we have to be careful that when we introduce new
features, we consider both sets of interfaces. E.g. don't add a feature
which will pause a crawl awaiting user input if the JMX interface is
being used.

## Checkpointing by default

IMO, enabling checkpointing by default would be nice for newbies. I got
bit by this when I started my test crawl, then my machine froze (due to
a buggy video driver) and when I rebooted I realized I didn't have
checkpointing enabled. Doh!

## Disk space

As my test crawl ran, I monitored the .arc files just by looking in the
directory for the job on the disk. Since I wasn't going to run the job
until completion, I didn't worry too much about disk space since I had
tens of gigs free. But, I did start to wonder how disk consumption is
managed in a large, production crawl done by our crawl engineers.

Gordon informed me that our crawl engineers employ a set of scripts that
monitor the .arc files as they are written and when one is completed,
the script copies it from the job's arcs directory off to a space in our
data center. This way, the crawl machines don't run out of disk space
during the crawl.

I was thinking that Heritrix users could make use of similar scripts.
Or, a new feature in Heritrix to monitor the amount of disk space and if
it falls below a configured threshold, automatically pause the job and
send a warning message. Heritrix could continue to monitor the disk and
if the free space increases above the threshold, the job automatically
continues.

## Web UI Ease of use

Overall, I think the web UI is pretty good. I did see the web UI for
Heritrix 1.x once, when I first started learning abou the Archive's web
team. IMO, compared to the Heritrix 1.x web UI, Heritrix 2.0 is a major
improvement.

I personally find the relatively plain design of the Heritrix 2.0 web UI
to be aesthetically pleasing. It doesn't have lots of unnecessary
graphic design and it looks clean. Also the basic navigation is rather
straightforward; the links go where you expect based on the name and
context.

But, a review/critique wouldn't be complete without some user interface
complaints ;D

### Sheet editing

Not surprisingly, sheet editing is one of the most complicated actions
in setting up a crawl. If it wasn't for the tutorial and the fact that
the UI does highlight properties needing correction, I would have been
totally lost on the sheet editing page.

There is a logic to the layout. You can see how properties are grouped
together in sensible ways. After further study, it becomes clear how the
processors are chained together, following the logic of page processing
for the crawl: DNS, then HTTP, then HTML extraction, etc.

My major complaint would be that this page smacks too much of the
underlying data-driven structure. For example, the processors sub-tree
is labeled map of Processor. The usability of the page is driven more by
the way the underlying data structure is defined, with maps and lists
than based on the user's needs.

### Sheet/property Inheritance

It seems that sheets follow a common inheritance model, where you create
a new sheet, with a global sheet as its parent. Properties defined in
the child sheet over-ride those in the parent sheet.

If that's the case, the sheet viewing and editing screens could give a
better view of the properties that are inherited and/or over-ridden.

Also, the global sheets seem to inherit properties from some sort of
built-in list (?) I mean, if you view the properties in the
broad\_but\_shallow global sheet, you won't see http-user-agent
property, but if you edit the sheet, you'll see that property and it's
value. Where does it come from?

### Initial validation problems

When you first edit the sheet (sheets/do\_show\_sheets.jsp), it warns
you that there are validation problems. That's a little unnerving as I
haven't done anything yet other than click the edit link from on the
crawl engine screen.

It does make sense for that warnin to appear on that screen, but only
after you've edited the sheet. Or, if you haven't edited it yet, but
there are properties that need editing (which is the case) then a
different warning message might be more helpful.

### Submitting vs. Committing vs. Saving

Although I can guess at some reasons why edits to the sheet must be
committed in addition to being submitted, it still is potentially
confusing and error-prone.

I don't have any specific suggestions on how to improve the usability at
this time, other than we should spend more time and effort to improve
it.

Also, on the sheet editing screen, at the top you might see a warning
that you've edited some property values but have not committed them. Or
is it that you haven't saved them? The warning message mixes the terms,
seemingly interchangeably. So now we have three concepts: "submit
changes", "commit changes" and "save changes". Are all three distinct,
or is saving the same as committing?

### Creating a job with invalid sheet is allowed

I was able to create a ready-to-run job from a profile that had
validation problems. In fact, if you view the sheet of one of the
predefined profiles, such as broad\_but\_shallow, you'll see the warning
about validation problems. But, you can then go back to the crawl engine
screen and copy the profile into a ready-to-run job; even though it
supposedly had validation problems.

Now, you do have to fix the validation errors before you can launch it.
If you try and launch a job with an invalid sheet, you are notified and
the job is not launched until the sheet is corrected.

Is it better to force the sheet validation when the job is
created/copied? Or is it better to wait until it is launched, like we do
now?

### Launching a job with no seeds is allowed

Ok, so you can't launch a job with an invalid sheet, but you can launch
a job with no seeds.

Shouldn't that be caught and and the user informed? Or are there
situations where running a seedless job is useful?

### Completed job in console loses log & reports links

One thing I found annoying was that once I terminated the job, in the
console screen (do\_show\_job\_console.jsp), the links for reports and
logs were removed. I had to go back to the main craw engine
(crawler\_area/do\_show\_crawler.jsp?) screen to to get the links to the
reports and logs.

It would be nice if the links to the reports and logs remained on the
job console screen after the job is completed.

### Link back to top-level page not obvious

On the job console, reports and logs, you have links at the top of each
page that will take you back to the job console, or "up" to the crawl
engine where you can see all the jobs and the global sheets. But how
does one return to the "very top-level" screen: the main index page?

It may not be obvious but the only link back to the main index page is
the black-and-white Heritrix logo in the upper-right corner of the page.
Although having a linked logo like this isn't unorthodox at all, it
being the only link back to the index page is unusual.

### Job console of completed job

From the crawler eninge screen (crawler\_area/do\_show\_crawler.jsp),
the list of completed jobs are not linked to the job console. When the
job is active, the links to the job console is there, but once the job
is completed, we no longer link it from that screen.

Now you can get to it. The completed job's sheets, seeds, etc. are all
linked. Just click on the Sheets link and on the
sheets/do\_show\_sheets.jsp page, you'll find a link to the job's
console.

The navigation inconsistency is a bit confusing.

### SURT add/remove distinction

It's not clear that SURT addition and removal screens are different. I
clicked on the remove link to remove a SURT and it looked just like the
add screen. I examined the URLs of the two screens and they only differ
in one parameter: add=Y/N

The text on the SURT add/remove page didn't distinguish the two
operations very well. It was easy to be confused as to which operation I
was performing.

### Confusing descriptive text on SURT add/remove screen

On the SURT addition and removal screens, the following text appears:

    One entry per line. SURT prefixes entered will be used
    directly. If the option below is checked, other URIs will be
    converted to SURT form then truncated to the implied prefix,
    and lain hosts/domains will be changed to the
    implied HTTP URI then converted as above. (If unchecked, all
    strings are accepted literally.)

I have no idea what the use of "lain" (as emphasized in the quote)  
means in this context.

# Documentation

Although it's a common theme in software to bemoan the lack of
documentation, I'll try to be more constructive than just complaining
about it.

As I mentioned above, I thought the tutorial was essential for the
beginner. I'd like to see more documentation along those lines. I'm a
big fan of tutorials and how-to documents, ones that teach you the
software as you use it. If we decide which subset of our audience we
want to focus on, providing them with a collection of how-to's aimed at
their typical use case would be a great benefit.

And even though tutorials are useful, those "here are the concepts"
documents are also useful. I think the main set of concepts to be
explained (at least to a beginner) are sheet inheritance, and how
profiles, jobs, sheets and SURTs all relate to each other.
