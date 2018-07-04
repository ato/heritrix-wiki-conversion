# HOWTO Launch Heritrix

# Introduction

**`HERITRIX_HOME`** is used throughout this document to refer to the
root of the installation.

The startup scripts use the environment variable `HERITRIX_HOME`. You
can set it manually, but normally the startup scripts are able to figure
it out themselves.

## Quick Start

Here is the simplest way to start heritrix:

``` bash
$HERITRIX_HOME/bin/heritrix --webui-admin PASSWORD
```

This starts the heritrix crawl engine and web UI in the background,
logging to **`$HERITRIX_HOME/heritrix_out.log`**, listening on
<http://localhost:8080/> with the specified password. Remote JMX support
may also be initialized (see the section **Remote JMX Configuration**
below for more information).

[There are more examples at the bottom](#HOWTOLaunchHeritrix-examples).

## Foreground vs. Background

There are two Heritrix launcher scripts:

-   `$HERITRIX_HOME/bin/heritrix`
-   `$HERITRIX_HOME/bin/foreground_heritrix`

Typically you will use **`$HERITRIX_HOME/bin/heritrix`**, which forks
heritrix into the background and logs to an external file,
`$HERITRIX_HOME/heritrix_out.log` by default.

Useful for debugging, **`$HERITRIX_HOME/bin/foreground_heritrix`** does
not fork and logs to stdout.

# Command Line Options

    $ ./heritrix --help
    usage: Heritrix
     -a,--webui-admin <arg>          Specifies the authorization password
                                     which must be supplied to access the webui. Required if launching the
                                     webui.
     -b,--webui-bind-hosts <arg>     A comma-separated list of hostnames for
                                     the webui to bind to.
     -h,--help <arg>                 Usage information.
     -j,--jobs-dir <arg>             The jobs directory.  Defaults to ./jobs
     -k,--keystore <arg>             Path to keystore with private key and
                                     certificate for webui running behind https.
     -l,--logging-properties <arg>   The full path to the logging properties
                                     file (eg, conf/logging.properties).  If present, this file will be used to
                                     configure Java logging.  Defaults to ./conf/logging.properties
     -n,--no-web-ui                  Do not run the admin web user interface;
                                     only run the crawl engine.  If set, the crawl engine will need to be
                                     controlled via JMX or a remote web UI.
     -p,--webui-port <arg>           The port the webui should listen on.
                                     Defaults to 8443 with SSL enabled or 8080 otherwise.
     -r,--run-job <arg>              Specify a ready job or a profile name to
                                     launch at launch.  If you specify a profile name, the profile will first
                                     be copied to a new ready job, and that ready job will be launched.
     -u,--no-engine                  Do not run the crawl engine; only run the
                                     admin web UI.
     -w,--webui-war-path <arg>       The path to the Heritrix webui WAR.
     -x,--no-ssl                     Use plain http and not https for the
                                     webui.

### Web UI and/or Crawl Engine

The web-based user interface and the crawl engine are distinct pieces of
heritrix. Typically they run together, but that is not required.

###### `--no-engine`

Use this option to run only the web UI. Once heritrix is launched, you
can hook up crawl engines through the web UI.

###### `--no-web-ui`

Use this option to run only the crawl engine. The engine can then be
controlled through remote JMX or through a separate web UI. See below
for more info on JMX.

### Web UI Configuratioin

###### `--webui-admin <arg>`

Sets the admin password. This option is required, there is no default.

###### `--webui-bind-hosts <arg>`

This option takes a comma-separated list of hosts/ip addresses to listen
on (though typically one is enough). Specify **`/`** or **`0.0.0.0`** to
listen on all interfaces.

The default is to listen only on localhost.

For security, when this option is specified, the web UI will be served
over https (SSL encrypted), unless --no-ssl is specified.

###### `--webui-port <arg>`

If SSL (https) is enabled, the default port is 8443, otherwise it is
8080. Use this option to specify a different port.

###### `--webui-war-path <arg>`

By default heritrix will look for the WAR in `$HERITRIX_HOME/lib`. Use
this option to specify a different location. The path can point to
either a WAR file or an exploded webapp directory.

###### `--no-ssl`

Use this option to force the web UI to be served over plain, insecure
http. **Use of this option is discouraged.**

###### `--keystore <arg>`

By default, when SSL is enabled, heritrix will generate a private key
and certificate at startup.

For a variety of reasons, particularly if you are running heritrix as a
public-facing service, you may want to use your own certificate. To do
this, you can create a keystore using the java keytool. There is some
rudimentary information on using keytool here:
<http://docs.codehaus.org/display/JETTY/How+to+configure+SSL>. **Note:
the password on the keystore and on the key must be "heritrix"**.

Unless there is a compelling rationale, use of a keystore is
discouraged. It is more secure to let heritrix generate a key/cert on
the fly, since there is no secret file that can be compromised.

### Other Options

###### `--jobs-dir <arg>`

The default jobs directory is **`$HERITRIX_HOME/jobs`**. Use this option
to specify a different path.

###### `--logging-properties <arg>`

By default, heritrix will look for logging configuration in
**`$HERITRIX_HOME/conf/logging.properties`**. Use this option to specify
a different path. There is some information on customizing this file in
the one that comes with heritrix.

###### `--run-job <arg>`

Start the specified ready job immediately. The argument is the name of
the job, which is the name of the subdirectory, not including the prefix
"`ready-`". [See an example](#HOWTOLaunchHeritrix-examples)

# Environment Variables

### General

###### `HERITRIX_HOME`

**`HERITRIX_HOME`** sets the root of the installation. Search this
document for "HERITRIX\_HOME" and look at each instance to discover what
this variable affects concretely.

Heritrix (the startup script) writes the process id in
`$HERITRIX_HOME/heritrix.pid`. It does not make further use of this
file, does not complain if it is overwritten, and does not delete even
after shutting down.

###### `HERITRIX_OUT`

The default log location is `$HERITRIX_HOME/heritrix_out.log`. Use
**`HERITRIX_OUT`** to specify a different location.

###### `JAVA_HOME`

If the **`java`** command is on the system path, the startup script will
set **`JAVA_HOME`** based on that. Use this environment variable to
specify a different location, or if `java` is not on the path.

### Remote JMX Configuration

The crawl engine can be remotely controlled via JMX.

When **`--no-webui`** is specified, remote JMX must be enabled and
configured properly, otherwise the crawl engine would be inaccessible.

A password file is required for remote JMX, and it will start
automatically if the password file exists. See
**`$HERITRIX_HOME/conf/jmxremote.password.template`** for more
information.

###### `JMX_PORT`

The default JMX port is 8849. Use this environment variable to specify a
different port.

###### `JMX_OFF`

Set this variable to a non-empty string, e.g. **`JMX_OFF=off`**, to
disable remote JMX.

# Examples

    $ heritrix --webui-admin heritrix-password
    WARNING: $HERITRIX_HOME/conf/jmxremote.password not found.
    WARNING: Disabling remote JMX.
    Fri Nov 21 00:05:46 PST 2008 Starting heritrix...
    No JNDI context.
    Engine registered at org.archive.crawler:instance=14434757,jmxport=-1,name=Engine,type=org.archive.crawler.framework.Engine,host=noah-levitts-computer.local
    Web UI listening on localhost:8080.

-   logs to $HERITRIX\_HOME/heritrix\_out.log
-   web UI on <http://localhost:8080/>
-   password "heritrix-password"
-   JMX on port 8849 if $HERITRIX\_HOME/conf/jmxremote.password exists

    $ HERITRIX_HOME=/var/heritrix HERITRIX_OUT=/var/log/heritrix.log JMX_PORT=9949 JAVA_HOME=/usr/lib/jvm/jdk1.6.0_06 heritrix -a heritrix-password --webui-bind-hosts 0.0.0.0 -j /var/heritrix-jobs
    Fri Nov 21 00:33:47 PST 2008 Starting heritrix..
    No JNDI context.
    Engine registered at org.archive.crawler:instance=30931963,jmxport=9949,name=Engine,type=org.archive.crawler.framework.Engine,host=cheese
    Web UI listening on 0.0.0.0:8443.

-   web UI on <https://THIS_HOST:8443/> and <https://localhost:8443/>
-   the rest is pretty self-explanatory at this point

    $ ./heritrix -a admin --run-job broad_but_shallow-20081121085437
    Fri Nov 21 00:55:18 PST 2008 Starting heritrix.....
    No JNDI context.
    Engine registered at org.archive.crawler:instance=7832149,jmxport=8849,name=Engine,type=org.archive.crawler.framework.Engine,host=noah-levitts-computer.local
    Web UI listening on localhost:8080.

-   This runs the job in
    `$HERITRIX_HOME/jobs/ready-broad_but_shallow-20081121085437`, which
    would normally be initialized through the web UI, but could be
    mimicked outside heritrix.

# Shutting Down

Heritrix can be shut down cleanly by killing the process with the
default signal SIGTERM. It can also be shut down throught the web UI.
