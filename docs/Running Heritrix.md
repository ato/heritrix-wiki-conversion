# Running Heritrix

# Heritrix 2.0.0 Tutorial

## Running Heritrix

After you have downloaded and unpacked the heritrix tar.gz or zip file,
and after you've set the `HERITRIX_HOME` environment variable, you are
ready to run Heritrix in its simplest configuration. To do so, simply
enter the following into your shell:

``` bash
$ $HERITRIX_HOME/bin/heritrix -a admin
```

The `-a` argument is very important, as it specifies that you want
Heritrix to run with the web UI enabled. You can use this web UI to
start and stop crawls. The argument following the `-a` option specifies
the password you want to use to access the web UI. In this tutorial
we're using the password "admin", but you probably want to come up with
something more secure.

The above command should produce output similar to the following:

``` bash
$ bin/heritrix -a admin
WARNING: No $HERITRIX_HOME/conf/jmxremote.password found.
WARNING: Disabling remote JMX.
Tue Jul 17 14:00:25 PDT 2007 Starting heritrix
No JNDI context.
Engine registered at org.archive.crawler:instance=14306161,jmxport=8849,name=Engine,type=org.archive.crawler.framework.Engine,host=localhost
Web UI listening on localhost:8080.
```

You needn't worry about the dire WARNINGS. Unless you've properly
configured jmxremote.password and/or jndi.properties, you will see the
warnings regarding JMX and JNDI not being configured. You don't need JMX
or JNDI to use the crawler if you started it with `-a`, so don't panic.

The last line of output - the one that starts with "Engine registered
at..." - is the Java MBean ObjectName of the central component of the
Heritrix crawler. This component is called the Engine, and it is used to
start and start crawl jobs. You can use this output to control the
Engine via JMX, if you properly configure jmxremote.password first. This
can be useful if you'd like to automate the starting and stopping of
crawls without using the web user interface.

In this tutorial, though, we'll only be using the web user interface to
control crawl jobs. For security reasons, the web server only listens on
`localhost`. You can change this behavior with the `-b` option (which
takes a comma-separated list of IP addresses, or '/' for all). By
default, it will try to listen on port 8080; you can override that with
the `-p` option.

So, you can access the web user interface by browsing to
<http://localhost:8080/>. You'll have to enter the password you
specified using the -a option. In this case, we set the password to
"admin".

[2.0 Tutorial](2.0%20Tutorial) \| [Using the Web User
Interface](Using%20the%20Web%20User%20Interface)
