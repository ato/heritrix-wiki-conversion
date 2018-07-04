# Running Heritrix 3.0 and 3.1

Heritrix can be run with many command line options.  Enter the following
command to output the options.

``` bash
$HERITRIX_HOME/bin/heritrix --help
```

The following table lists the command line options.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Command Line Options <br />
</p></th>
<th><p>Description<br />
</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><code>-a</code> <code>--web-admin &lt;arg&gt;</code></p></td>
<td><p>Specifies the authorization username and password that must be supplied to access the Web UI.  This parameter is required if launching the Web UI.  The parameter format is <code>&lt;adminname&gt;:&lt;adminpassword&gt;</code>.  For example, <code>admin:admin</code>.  As of Heritrix 3.1, if the parameter supplied to the -a command line option is a string beginning with &quot;@&quot;, the rest of the string is interpreted as a local file name containing the operator login and password. This adds an additional layer of protection to the admin username and password.</p></td>
</tr>
<tr class="even">
<td><p><code>-b</code> <code>--web-bind-hosts &lt;arg&gt;</code></p></td>
<td><p>Specifies a comma-separated list of hostnames/IP-addresses to bind to the Web UI. If none are specified, the Web UI will only be available via localhost/127.0.0.1. You may use '/' as a shorthand for 'all addresses'.</p></td>
</tr>
<tr class="odd">
<td><p><code>-h</code>,<code>--help &lt;arg&gt;</code><br />
</p></td>
<td><p>Display usage information.</p></td>
</tr>
<tr class="even">
<td><p><code>-j</code>,<code>--jobs-dir</code></p></td>
<td><p>Display the jobs directory.  The default is <code>./jobs</code>.</p></td>
</tr>
<tr class="odd">
<td><p><code>-l</code>,<code>--logging-properties</code></p></td>
<td><p>Display the full path to the logging properties file (e.g., <code>conf/logging.properties</code>).  If present, this file will be used to configure Java logging.  The default is <code>./conf/logging.properties</code>.</p></td>
</tr>
<tr class="even">
<td><p><code>-p</code>,<code>--web-port &lt;arg&gt;</code></p></td>
<td><p>Specify the port the Web UI will listen on.</p></td>
</tr>
<tr class="odd">
<td><p><code>-r</code>,<code>--run-job &lt;arg&gt;</code></p></td>
<td><p>Specifies a ready job or profile name to launch when Heritrix starts.  If a profile name is specified, the profile will first be copied to a new ready job, and that ready job will be launched.  As of Heritrix 3.1, this option has been eliminated.</p></td>
</tr>
<tr class="even">
<td><p><code>-s</code>,<code>--ssl-params &lt;arg&gt;</code></p></td>
<td><p>Specifies a keystore path, keystore password, and key password for HTTPS use.  Separate the values with commas and do not include whitespace.</p></td>
</tr>
</tbody>
</table>

To launch Heritrix with the Web UI enabled, enter the following command.
 The username and password for the Web UI are set to "admin" and
"admin", respectively.

``` bash
$HERITRIX_HOME/bin/heritrix -a admin:admin
```

By default, the Web UI listening address is only bound to the
'localhost' address.  Therefore, the Web UI can only be accessed on the
same machine from which it was launched. The '-b' option may be used to
listen on different/additional addresses.  See [Security
Considerations](Security%20Considerations) before changing this default.
