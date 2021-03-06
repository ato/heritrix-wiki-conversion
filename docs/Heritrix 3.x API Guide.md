# Heritrix 3.x API Guide

-   1 [Introduction](#Heritrix3.xAPIGuide-Introduction)
-   2 [Conventions and
    Assumptions](#Heritrix3.xAPIGuide-ConventionsandAssumptions)
-   3 [REST](#Heritrix3.xAPIGuide-REST)
-   4 [Heritrix Restlet API](#Heritrix3.xAPIGuide-HeritrixRestletAPI)
    -   4.1 [Requirements for API
        Invocation](#Heritrix3.xAPIGuide-RequirementsforAPIInvocation)
    -   4.2 [API Format](#Heritrix3.xAPIGuide-APIFormat)
-   5 [API](#Heritrix3.xAPIGuide-API)
    -   5.1 [Create New Job](#Heritrix3.xAPIGuide-CreateNewJob)
    -   5.2 [Add Job Directory](#Heritrix3.xAPIGuide-AddJobDirectory)
    -   5.3 [Build Job
        Configuration](#Heritrix3.xAPIGuide-BuildJobConfiguration)
    -   5.4 [Launch Job](#Heritrix3.xAPIGuide-LaunchJob)
    -   5.5 [Rescan Job
        Directory](#Heritrix3.xAPIGuide-RescanJobDirectory)
    -   5.6 [Pause Job](#Heritrix3.xAPIGuide-PauseJob)
    -   5.7 [Unpause Job](#Heritrix3.xAPIGuide-UnpauseJob)
    -   5.8 [Terminate Job](#Heritrix3.xAPIGuide-TerminateJob)
    -   5.9 [Teardown Job](#Heritrix3.xAPIGuide-TeardownJob)
    -   5.10 [Copy Job](#Heritrix3.xAPIGuide-CopyJob)
    -   5.11 [Checkpoint Job](#Heritrix3.xAPIGuide-CheckpointJob)
    -   5.12 [Execute Shell Script in
        Job](#Heritrix3.xAPIGuide-ExecuteShellScriptinJob)
    -   5.13 [Submitting a CXML Job Configuration
        File](#Heritrix3.xAPIGuide-SubmittingaCXMLJobConfigurationFile)

In case of SSL error

If you get an error like this from curl:  
`error:14077438:SSL routines:SSL23_GET_SERVER_HELLO:tlsv1 alert internal error`  
try adding the argument **`-sslv3`** to your curl commands.  
See <http://tech.groups.yahoo.com/group/archive-crawler/message/7456>

# Introduction

This manual describes the REST application programming interface (API)
of the Heritrix Web crawler.  Heritrix is the Internet Archive's open
source, extensible, Web-scale, archival-quality Web crawler. For more
information about Heritrix, visit <http://crawler.archive.org/>.

This document is intended for application developers and administrators
interested in controlling the Heritrix Web crawler through its REST API.

# Conventions and Assumptions

The following conventions are used in this document.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Convention<br />
</p></th>
<th><p>Description<br />
</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>(identifier)</p></td>
<td><p>A identifier surrounded by parenthesis indicates a user-defined value. For example, (heritrixhostname) indicates a user-defined hostname that is running Heritrix.</p></td>
</tr>
<tr class="even">
<td><p>[identifier1,identifier2,...]</p></td>
<td><p>Multiple identifiers surrounded by brackets indicate a predefined set of values. For example, [on,off] indicates a set of values comprised of the literals, &quot;on&quot; and &quot;off&quot;.</p></td>
</tr>
</tbody>
</table>

The following curl parameters are used when invoking the API.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>curl Parameter<br />
</p></th>
<th><p>Description<br />
</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>-v</p></td>
<td><p>Verbose. Output a detailed account of the curl command to standard out.</p></td>
</tr>
<tr class="even">
<td><p>-d</p></td>
<td><p>Data. These are the name/value pairs that are send in the body of a POST.</p></td>
</tr>
<tr class="odd">
<td><p>-k</p></td>
<td><p>Insecure. Allows connections to SSL sites without certificates.</p></td>
</tr>
<tr class="even">
<td><p>-u<br />
</p></td>
<td><p>User. Allows the submission of a username and password to authenticate the HTTP request.</p></td>
</tr>
<tr class="odd">
<td><p>--anyauth</p></td>
<td><p>Any authentication type. Allows authentication of the request based on any type of authentication method.</p></td>
</tr>
<tr class="even">
<td><p>--location</p></td>
<td><p>Follows HTTP redirects. This option is used so that API calls that return data (such as HTML) will not halt upon receipt of a redirect code (such as an HTTP 303).</p></td>
</tr>
<tr class="odd">
<td><p>-H<br />
</p></td>
<td><p>Set the value of an HTTP header. For example, &quot;Accept: application/xml&quot;.</p></td>
</tr>
</tbody>
</table>

It is assumed that the reader has a working knowledge of the HTTP
protocol and Heritrix functionality.  Also, the examples assume that
Heritrix is run with an administrative username and password of "admin."

# REST

Representational State Transfer (REST) is a software architecture for
distributed hypermedia systems such as the World Wide Web (WWW). REST is
built on the concept of representations of resources. Resources can be
any coherent and meaningful concept that may be addressed. A URI is an
example of a resource. The representation of the resource is typically a
document that captures the current or intended state of the resource. An
example of a representation of a resource is an HTML page.

Heritrix uses REST to expose its functionality. The REST implementation
used by Heritrix is Restlet. Restlet implements the concepts defined by
REST, including resources and representations. It also provides a REST
container that processes RESTful requests. The container is the Noelios
Restlet Engine. For detailed information on Restlet,
visit <http://www.restlet.org/>.

# Heritrix Restlet API

Heritrix exposes its REST functionality through HTTPS. The HTTPS
protocol is used to send requests to retrieve or modify configuration
settings and manage crawl jobs.

### Requirements for API Invocation

Any client that supports HTTPS can be used to invoke the Heritrix API.
The most common clients are command line tools such as curl and wget.
These command line tools are typically found in Unix environments but
can also be run on a Windows environment by
installing [Cygwin](http://www.cygwin.com/).  Cygwin is a free Linux
emulation environment for Windows.

### API Format

The format used to describe each API is as follows.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Name<br />
</p></th>
<th><p>Description<br />
</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>API Name<br />
</p></td>
<td><p>The name assigned to the API. The name is a single word or short phrase that encapsulates the purpose of the API call.</p></td>
</tr>
<tr class="even">
<td><p>URI</p></td>
<td><p>The URI to call when invoking the API.</p></td>
</tr>
<tr class="odd">
<td><p>Description</p></td>
<td><p>The description of the API. The description provides a detailed overview of what the API accomplishes and when the API should be called.</p></td>
</tr>
<tr class="even">
<td><p>HTTP Method</p></td>
<td><p>The HTTP method to use when invoking the API.</p></td>
</tr>
<tr class="odd">
<td><p>HTTP Data</p></td>
<td><p>The name/value pairs that are submitted with the HTTP request.</p></td>
</tr>
<tr class="even">
<td><p>HTML Example</p></td>
<td><p>An example call to the API. The curl command line utility is the HTTPS client used in the examples. The call returns HTML output.<br />
</p></td>
</tr>
<tr class="odd">
<td><p>XML Example<br />
</p></td>
<td><p>An example call to the API that returns XML output.  The curl command line utility is the HTTPS client used in the examples.</p></td>
</tr>
</tbody>
</table>

# API

### Create New Job

###### URI

https://(heritrixhost):8443/engine

###### Description

This API creates a new crawl job configuration. It uses the default
configuration provided by the profile-defaults profile.

###### HTTP Method

POST

###### HTTP Data

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Name<br />
</p></th>
<th><p>Value<br />
</p></th>
<th><p>Description<br />
</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>createpath<br />
</p></td>
<td><p>(jobname)<br />
</p></td>
<td><p>The name of the job.<br />
</p></td>
</tr>
<tr class="even">
<td><p>action<br />
</p></td>
<td><p>create<br />
</p></td>
<td><p>The action to invoke.<br />
</p></td>
</tr>
</tbody>
</table>

###### HTML Example

``` bash
curl -v -d "createpath=myjob&action=create" -k -u admin:admin --anyauth --location https://localhost:8443/engine
```

###### XML Example

``` bash
curl -v -d "createpath=myjob&action=create" -k -u admin:admin --anyauth --location -H "Accept: application/xml" https://localhost:8443/engine
```

### Add Job Directory

###### URI

https://(heritrixhost):8443/engine

###### Description

This API adds a new job directory to the Heritrix configuration. The
directory must contain a cxml configuration file.

###### HTTP Method

POST

###### HTTP Data

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Name<br />
</p></th>
<th><p>Value<br />
</p></th>
<th><p>Description<br />
</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>addpath<br />
</p></td>
<td><p>(job directory to add)<br />
</p></td>
<td><p>The job directory to add.<br />
</p></td>
</tr>
<tr class="even">
<td><p>action<br />
</p></td>
<td><p>add<br />
</p></td>
<td><p>The action to invoke<br />
</p></td>
</tr>
</tbody>
</table>

###### HTML Example

``` bash
curl -v -d "action=add&addpath=/Users/hstern/job" -k -u admin:admin --anyauth --location https://localhost:8443/engine
```

###### XML Example

``` bash
curl -v -d "action=add&addpath=/Users/hstern/job" -k -u admin:admin --anyauth --location -H "Accept: application/xml" https://localhost:8443/engine
```

### Build Job Configuration

###### URI

https://(heritrixhost):8443/engine/job/(jobname)

###### Description

This API builds the job configuration for the chosen job. It reads an
XML descriptor file and uses Spring to build the Java objects that are
necessary for running the crawl. Before a crawl can be run it must be
built.

###### HTTP Method

POST

###### HTTP Data

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Name<br />
</p></th>
<th><p>Value<br />
</p></th>
<th><p>Description<br />
</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>action<br />
</p></td>
<td><p>build<br />
</p></td>
<td><p>The action to invoke.<br />
</p></td>
</tr>
</tbody>
</table>

###### HTML Example

``` bash
curl -v -d "action=build" -k -u admin:admin --anyauth --location https://localhost:8443/engine/job/myjob
```

###### XML Example

``` bash
curl -v -d "action=build" -k -u admin:admin --anyauth --location -H "Accept: application/xml" https://localhost:8443/engine/job/myjob
```

### Launch Job

###### URI

https://(heritrixhost):8443/engine/job/(jobname)

###### Description

This API launches a crawl job. The job can be launched in the "paused"
state or the "unpaused" state. If launched in the "unpaused" state the
job will immediately begin crawling.

###### HTTP Method

POST

###### HTTP Data

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Name<br />
</p></th>
<th><p>Value<br />
</p></th>
<th><p>Description<br />
</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>action<br />
</p></td>
<td><p>launch<br />
</p></td>
<td><p>The action to invoke.<br />
</p></td>
</tr>
</tbody>
</table>

###### HTML Example

``` bash
curl -v -d "action=launch" -k -u admin:admin --anyauth --location https://localhost:8443/engine/job/myjob
```

###### XML Example

``` bash
curl -v -d "action=launch" -k -u admin:admin --anyauth --location -H "Accept: application/xml" https://localhost:8443/engine/job/myjob
```

### Rescan Job Directory

###### URI

https://(heritrixhost):8443/engine

###### Description

This API rescans the main job directory and returns an HTML page
containing all the job names. It also returns information about the
jobs, such as the location of the job configuration file and the number
of job launches.

###### HTTP Method

POST

HTTP Data

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Name<br />
</p></th>
<th><p>Value<br />
</p></th>
<th><p>Description<br />
</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>action<br />
</p></td>
<td><p>rescan<br />
</p></td>
<td><p>The action to invoke.<br />
</p></td>
</tr>
</tbody>
</table>

###### HTML Example

``` bash
curl -v -d "action=rescan" -k -u admin:admin --anyauth --location https://localhost:8443/engine
```

###### XML Example

``` bash
curl -v -d "action=rescan" -k -u admin:admin --anyauth --location -H "Accept: application/xml" https://localhost:8443/engine
```

### Pause Job

###### URI

https://(heritrixhost):8443/engine/job/(jobname)

###### Description

This API pauses an unpaused job. No crawling will occur while a job is
paused.

###### HTTP Method

POST

###### HTTP Data

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Name<br />
</p></th>
<th><p>Value<br />
</p></th>
<th><p>Description<br />
</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>action<br />
</p></td>
<td><p>pause<br />
</p></td>
<td><p>The action to invoke.<br />
</p></td>
</tr>
</tbody>
</table>

###### HTML Example

``` bash
curl -v -d "action=pause" -k -u admin:admin --anyauth --location https://localhost:8443/engine/job/myjob
```

###### XML Example

``` bash
curl -v -d "action=pause" -k -u admin:admin --anyauth --location -H "Accept: application/xml" https://localhost:8443/engine/job/myjob
```

### Unpause Job

###### URI

https://(heritrixhost):8443/engine/job/(jobname)

###### Description

This API unpauses a paused job. Crawling will resume (or begin, in the
case of a job launched in the paused state) if possible.

###### HTTP Method

POST

###### HTTP Data

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Name <br />
</p></th>
<th><p>Value <br />
</p></th>
<th><p>Description <br />
</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>action <br />
</p></td>
<td><p>unpause <br />
</p></td>
<td><p>The action to invoke. <br />
</p></td>
</tr>
</tbody>
</table>

###### HTML Example

``` bash
curl -v -d "action=unpause" -k -u admin:admin --anyauth --location https://localhost:8443/engine/job/myjob
```

###### XML Example

``` bash
curl -v -d "action=unpause" -k -u admin:admin --anyauth --location -H "Accept: application/xml" https://localhost:8443/engine/job/myjob
```

### Terminate Job

###### URI

https://(heritrixhost):8443/engine/job/(jobname)

###### Description

This API terminates a running job.

###### HTTP Method

POST

###### HTTP Data

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Name<br />
</p></th>
<th><p>Value<br />
</p></th>
<th><p>Description<br />
</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>action<br />
</p></td>
<td><p>terminate<br />
</p></td>
<td><p>The action to invoke.<br />
</p></td>
</tr>
</tbody>
</table>

###### HTML Example

``` bash
curl -v -d "action=terminate" -k -u admin:admin --anyauth --location https://localhost:8443/engine/job/myjob
```

###### XML Example

``` bash
curl -v -d "action=terminate" -k -u admin:admin --anyauth --location -H "Accept: application/xml" https://localhost:8443/engine/job/myjob
```

### Teardown Job

###### URI

https://(heritrixhost):8443/engine/job/(jobname)

###### Description

This API removes the Spring code that is used to run the job. Once a job
is torn down it must be rebuilt in order to run.

###### HTTP Method

POST

###### HTTP Data

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Name<br />
</p></th>
<th><p>Value<br />
</p></th>
<th><p>Description<br />
</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>action<br />
</p></td>
<td><p>teardown<br />
</p></td>
<td><p>The action to invoke.<br />
</p></td>
</tr>
</tbody>
</table>

###### HTML Example

``` bash
curl -v -d "action=teardown" -k -u admin:admin --anyauth --location https://localhost:8443/engine/job/myjob
```

###### XML Example

``` bash
curl -v -d "action=teardown" -k -u admin:admin --anyauth --location -H "Accept: application/xml" https://localhost:8443/engine/job/myjob
```

### Copy Job

###### URI

https://(heritrixhost):8443/engine/job/(jobname)

###### Description

This API copies an existing job configuration to a new job
configuration. If the "as profile" checkbox is selected, than the job
configuration is copied as a non-runnable profile configuration.

###### HTTP Method

POST

HTTP Data

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Name<br />
</p></th>
<th><p>Value<br />
</p></th>
<th><p>Description<br />
</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>copyTo<br />
</p></td>
<td><p>(new job or profile configuration name)</p></td>
<td><p>The name of the new job or profile configuration.</p></td>
</tr>
<tr class="even">
<td><p>asProfile</p></td>
<td><p>[on]<br />
</p></td>
<td><p>Whether to copy the job as a runnable configuration or as a non-runnable profile. &quot;On&quot; means the job will be copied as a profile. If the &quot;asProfile&quot; parameter is ommitted, the job will be copied as a runnable configuration.</p></td>
</tr>
</tbody>
</table>

###### HTML Example

``` bash
curl -v -d "copyTo=mycopy&asProfile=on" -k -u admin:admin --anyauth --location https://localhost:8443/engine/job/myjob
```

###### XML Example

``` bash
curl -v -d "copyTo=mycopy&asProfile=on" -k -u admin:admin --anyauth --location -H "Accept: application/xml" https://localhost:8443/engine/job/myjob
```

### Checkpoint Job

###### URI

https://(heritrixhost):8443/engine/job/(jobname)

###### Description

This API checkpoints the chosen job. Checkpointing writes the current
state of a crawl to the file system so that the crawl can be recovered
if it fails.

###### HTTP Method

POST

###### HTTP Data

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Name<br />
</p></th>
<th><p>Value<br />
</p></th>
<th><p>Description<br />
</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>action<br />
</p></td>
<td><p>checkpoint<br />
</p></td>
<td><p>The action to invoke.<br />
</p></td>
</tr>
</tbody>
</table>

###### HTML Example

``` bash
curl -v -d "action=checkpoint" -k -u admin:admin --anyauth --location https://localhost:8443/engine/job/myjob
```

###### XML Example

``` bash
curl -v -d "action=checkpoint" -k -u admin:admin --anyauth --location -H "Accept: application/xml" https://localhost:8443/engine/job/myjob
```

### Execute Shell Script in Job

###### URI

https://(heritrixhost):8443/engine/job/(jobname)/script

###### Description

This API executes a shell script. The script can be written as
Beanshell, ECMAScript, Groovy, or AppleScript.

###### HTTP Method

POST

###### HTTP Data

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Name<br />
</p></th>
<th><p>Value<br />
</p></th>
<th><p>Description<br />
</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>engine<br />
</p></td>
<td><p>[beanshell,js,groovy,AppleScriptEngine]<br />
</p></td>
<td><p>The script engine to use.</p></td>
</tr>
<tr class="even">
<td><p>script</p></td>
<td><p>(code to execute)</p></td>
<td><p>The script code to execute.</p></td>
</tr>
</tbody>
</table>

###### HTML Example

``` bash
curl -v -d "engine=beanshell&script=System.out.println%28%22test%22%29%3B" -k -u admin:admin --anyauth --location https://localhost:8443/engine/job/myjob/script
```

###### XML Example

``` bash
curl -v -d "engine=beanshell&script=System.out.println%28%22test%22%29%3B" -k -u admin:admin --anyauth --location -H "Accept: application/xml" https://localhost:8443/engine/job/myjob/script
```

### Submitting a CXML Job Configuration File

###### URI

https://(heritrixhost):8443/engine/job/(jobname)/jobdir/crawler-beans.cxml

###### Description

This API submits the contents of a CXML file for a chosen job. CXML
files are the configuration files used to control a crawl job. Each job
has a single CXML file.

###### HTTP Method

PUT

###### HTTP Data

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>(CXML file content)</p></td>
<td><p>The XML-based text of the CXML file.</p></td>
</tr>
</tbody>
</table>

###### Example

``` bash
curl -v -T my-crawler-beans.cxml -k -u admin:admin --anyauth --location https://localhost:8443/engine/job/myjob/jobdir/crawler-beans.cxml
```

###### API Response

On success, the Heritrix REST API will return a HTTP 200 with no body.
