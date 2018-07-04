# Configuring a Crawl

# Heritrix 2.0 Tutorial

## Configuring a Crawl

If you ran Heritrix using the steps in [Running
Heritrix](Running%20Heritrix), then you should have an admin web user
interface available at <http://localhost:8080/heritrix>. When you enter
that address in your browser, you should see something like this:

![](attachments/3730/90996753.png)

One difference between Heritrix 1.x and Heritrix 2.0 is that the new web
user interface can be used to control more than one crawl engine. The
home page of the user interface displays each engine it knows about. If
you have configured a JNDI server, then the user interface will query
that JNDI server to find engines. Otherwise you can manually tell the
user interface about crawl engines by clicking the "Add a remote crawl
engine..." link.

For each known crawl engine, the home page displays the Engine ID. The
Engine ID usually consists of the JMX host and port of the engine,
followed by the Java unique identifier of the engine (this is the number
returned by System.identityHashCode). However, there is a special Engine
ID used to represent an engine that's running inside the same Java
virtual machine as the user interface. That Engine ID uses -1 as the
port number, to distinguish it from actual remote engines.

Since we started Heritrix with `-r`, there is a crawl engine in the same
JVM as the user interface. The user interface has automatically
displayed this engine for you. (The hostname of my machine is `badwolf`,
so your Engine ID will probably be different.)

## Attachments:

![](images/icons/bullet_blue.gif){width="8" height="8"}
[home.png](attachments/3730/90996753.png) (image/png)  
