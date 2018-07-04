# Running the pjack\_settings Heritrix

# Running From Distribution Tarball

Go to our maven repository, download the latest tarball. You'll find it
in this directory:

<http://builds.archive.org:8080/maven2/org/archive/crawler/heritrix/2.0.0-SNAPSHOT/>

You're looking for something that ends with "-dist.tar.gz" – the build
box includes a timestamp  
in the filename, so it'll be different every build.

untar the tarball. Then:

    cd heritrix-2.0.0-snapshot
    ls
    # Output of ls should look familiar to you
    export HERITRIX_HOME=`pwd`

    # bin/heritrix will start the crawler, but first we need to enable remote JMX
    vi conf/jmxremote.password

    # # Type the following into jmxremote.password:
    # controlRole=X
    # monitorRole=X
    #
    # # Where "X" is the password you want to use

    # IMPORTANT! JVM refuses to run if jmxremote.password is visible
    # to anyone but user
    chmod 0600 conf/jmxremote.password

    bin/heritrix

At this point, you have a CrawlJobManager running, but no crawl jobs.
You can see what operations are available in the CrawlJobManager with:

    java -jar cmdline-jmxclient-0.10.5.jar \
       controlRole:happy \
       localhost:8849    \
       org.archive.crawler:name=CrawlJobManager,type=CrawlJobManager

The quickest way to start a job is to:

    vi profiles/default/seeds.txt

...and create your seeds list. Then:

    java -jar cmdline-jmxclient-0.10.5.jar \
       controlRole:happy \
       localhost:8849    \
       org.archive.crawler:name=CrawlJobManager,type=CrawlJobManager \
       launchProfile=default,the_job

You now have a job called "the\_job". It's not running yet. What has
happened is, the profile directory was copied into the jobs directory,
and a new MBean was registered in JMX. To find the MBean:

    java -jar cmdline-jmxclient-0.10.5.jar \
       controlRole:happy \
       localhost:8849    \
       | grep CrawlController

You have to do this because the ObjectName of the CrawlController
includes its identityHashCode, ensuring that two CrawlControllers can
live in the same JVM and be distinguishable. You'll probably want to
assign the output of the above to an environment variable, let's say
$CC.

OK. We have a CrawlController. It controls the crawl. The following
lists your available options:

    java -jar cmdline-jmxclient-0.10.5.jar \
       controlRole:happy \
       localhost:8849    \
       $CC

And this will (finally, finally) start the crawl:

    java -jar cmdline-jmxclient-0.10.5.jar \
       controlRole:happy \
       localhost:8849    \
       $CC requestCrawlStart

Similarly, this will stop the crawl:

    java -jar cmdline-jmxclient-0.10.5.jar \
       controlRole:happy \
       localhost:8849    \
       $CC requestCrawlStop

And the following operation on CrawlJobManager should gracefully
terminate the JVM. It doesn't, due to a bug, but it should:

    java -jar cmdline-jmxclient-0.10.5.jar \
       controlRole:happy \
       localhost:8849    \
       org.archive.crawler:name=CrawlJobManager,type=CrawlJobManager \
       close

## Or Do It The Easy Way

So the latest tarball includes a "jmxclient" script in the bin directory
that simplifies things greatly. It attaches to your Heritrix running at
localhost:8849, using the username of "controlRole" and the password it
parsed from conf/jmxremote.password. It then looks up the full object
name based on a partial object type. So, to make a long story short, to
start a crawl:

    cd $HERITRIX_HOME/bin
    ./heritrix
    ./jmxclient CrawlJobManager launchProfile=default,the_job
    ./jmxclient CrawlController requestCrawlStart

# Running Within Eclipse 

First pick a directory where you would like to store Heritrix jobs and
profiles. I'm going to use $CRAWLS in this example as the heritrix
runtime directory. I'm going to use $PROJECT\_HOME for the heritrix
project directory.

mkdir $CRAWLS/profiles 

cp -R $PROJECT\_HOME/testdata/selftest/SimpleSelfTest/profile/\*
$CRAWLS/profiles/default

That's the basic setup. You'll want to edit
$CRAWLS/profiles/default/sheets/default.single to edit the global
configuration. And you'll want to edit the seeds list at
$CRAWLS/profiles/default/seeds.txt.

Then run org.archive.crawler.Heritrix from Eclipse, setting args\[0\] to
$CRAWLS.

Use jconsole to launch crawls. Find the CrawlJobManager MBean, then
invoke the launchProfile operation. Specify "default" as the profile
name, specify whatever name you want for the job.

Once launchProfile finishes, two new MBeans will exist: A
CrawlController, and a SheetManager. You can use the SheetManager bean
to make configuration changes. You can use the CrawlController bean to
start/pause/checkpoint the job.  
