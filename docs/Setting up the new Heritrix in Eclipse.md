# Setting up the new Heritrix in Eclipse

**To set up the new Heritrix build in Eclipse:**

1.  Check out as project from SVN
2.  Install Maven 2 if not already installed
3.  Run "mvn install" task on root POM. As a side effect, this should
    also build all subprojects, and will download all the necessary
    libraries to your 'local' maven repository. There are two ways to do
    this:
    1.  CD to the relevant directory. Run "mvn install"; OR...
    2.  Using the M2Eclipse plugin, by right-clicking the master POM and
        choosing 'Run as...' &gt; 'maven install
4.  Set the M2\_REPO variable in Eclipse project 'Build Path' settings
    to point to the local Maven repository on your machine. (This is
    often in your home directory, in '.m2/repository'.

That should get you to the point where Eclipse can build the project.

(It should not be necessary to individually 'mvn install' each
subproject -- but if there are problems, try that, for each subproject,
in order -- commons modules engine webui -- then the main project.)

(After setting the M2\_REPO variable, all the project's existing library
paths -- which are defined in terms of M2\_REPO, should start to work.
However, it may be necessary to force a clean rebuild of the project.
You may wish to quit/restart Eclipse, use the 'Project'&gt;'Clean..'
Eclipse menu, or disable and reenable 'Build automatically' if there are
issues at this point.)

**To run Heritrix plus Web UI via Eclipse:**

Create 'Run' Profile for org.archive.crawler.Heritrix

1.  Set the following VM arguments:  
       -Dheritrix.development
2.  Set the following program arguments:  
       -ldist/src/main/conf/heritrix.properties  
       -j\[suitable folder for jobs created when testing Heritrix, make
    sure it exists and contains bundled profiles\]  
       -a\[chosen admin password\]

In this case, the engine and ui share the same JVM instance and the UI
automatically discovers the engine.

**To launch only the crawl engine (no web UI):**

An engine without a Web UI can only be controlled via JMX, so will need
additional starting configuration.

1.  Create a JMX password file.  
       Use heritrix/src/main/conf/jmxremote.password.template to
    create  
       the JMX password file where indicated by the VM parameter set
    earlier.  
       Make sure that this file is only readable by the system user that
    you will be running the crawler as!  
    ([This
    tip](http://blogs.sun.com/jmxetc/entry/the_hidden_command_that_would)
    may help set permissions right on Windows.)
2.  Add the following VM arguments:  
       -Dcom.sun.management.jmxremote.port=8849  
       -Dcom.sun.management.jmxremote.ssl=false  
       -Dcom.sun.management.jmxremote.password.file=\[suitable
    directory\]/jmxremote.password
3.  Use the following program command-line argument to refrain from
    launching the web UI  
       -n

**If you then wanted to launch a separate Web UI to control that
engine**

Run like the combined example above, but add the '-u' command-line
argument to request running a UI only.

This also uses a simple Jetty engine to launch the WebUI. Could also use
other JSP servlet engines, but that requires that the project be
deployed on them. (Needed: instructions/examples for this.)

Using this configuration the Heritrix crawl engine and the web UI run in
separate JVM instances (or even different machines if desired) and you
will have to manually add the crawl engine to the UI, using its JMX
hostname and port.

**Finally:**

Once both the crawler and the Web UI have been launched, navigate your
browser to  
<http://localhost:8080/heritrix/> (or appropriate host/path/port if
you've changed any settings or not running on localhost)

Then click Add and supply the hostname for the crawler (most likely
localhost will do) and the password you set  
for controlRole in the JMX password file.

That should do it!
