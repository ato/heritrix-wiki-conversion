# Security Considerations

Heritrix is a large and active network application that presents
security implications, both on the local machine, where it runs, and
remotely, on machines it contacts.

#### Understanding the Risks

It is important to recognize that the Web UI allows remote control of
the crawler in ways that could potentially disrupt a crawl, change the
crawler's behavior, read or write locally-accessible files, and perform
or trigger other actions in the Java VM or local machine by the
execution of arbitrary operator-supplied scripts.

Unauthorized access to the Web UI could end or corrupt a crawl. It could
also change the crawler's behavior to be a nuisance to other network
hosts. Files accessible to the crawler process could potentially be
deleted, corrupted, or replaced, which could cause extensive problems on
the crawling machine.

Another potential risk is that worst-case or maliciously-crafted
content, in conjunction with crawler issues, could disrupt the crawl or
other files and operations on the local system. For example, in the
past, without malicious intent, some rich-media content has caused
runaway memory use in third-party libraries used by the crawler. This
resulted in memory-exhaustion that stopped and corrupted the crawl in
progress. Similarly, atypical input patterns have caused runaway CPU use
by crawler link-extraction regular expressions, causing severely slow
crawls. Crawl operators should monitor their crawls closely and use the
project discussion list and issue database to stay current on crawler
issues.

#### Network Access Control

Launched without any specified bind-address ('-b' flag), the crawler's
Web UI only binds to the localhost/loopback address (127.0.0.1), and
therefore is only network-accessible from the same machine on which it
was launched.

If practical, this default setting should be maintained. A technique
such as SSH tunneling could be used by authorized users of the crawling
machine to enable Web access from their local machine to the crawling
machine. For example, consider Heritrix running on a machine
'crawler.example.com', with its Web UI only listening/bound on its
localhost address. Assuming a user named 'crawloperator' has SSH access
to 'crawler.example.com', she can issue the following SSH command from
her local machine:

``` bash
ssh -L localhost:9999:localhost:8443 crawloperator@crawler.example.com -N
```

This tells SSH to open a tunnel which forwards conections to
"localhost:9999" (on the local machine) to the remote machines' own idea
of "localhost:8443". As a result, the crawler's Web UI will be available
via "https://localhost:9999/" for as long as the tunnel exists (until
the ssh command is killed or connection otherwise broken). No one else
on the network may directly connect to port 8443 on
'crawler.example.com' (since it is only listening on the local loopback
address), and no one elsewhere on the net may directly connect to the
operator's port 9999 (since it also is only listening on the local
loopback address).

If you need Heritrix's listening port bound to a public address, the
'-b' command-line flag may be used.  This flag takes, as an argument,
the hostname/address to use.  The '/' character can be used to indicate
all addresses.

If you use this option, you should take special care to choose an even
more unique/unguessable/brute-force-search-resistant set of login
credentials. You may still want to consider using other network/firewall
policies to block access from unauthorized origins.

#### Login Authentication Access Control

The administrative login and password only offer rudimentary protection
against unauthorized access. For best security, you should be sure to:

1.  Use a strong, unique username and password combination to secure the
    Web UI. Heritrix uses HTTPS to encrypt communication between the
    client and the Web UI. Keep in mind that setting the username and
    password on the command-line may result in their values being
    visible to other users of the crawling machine – for example, via
    the output of a tool like 'ps' that shows the command-lines used to
    launch processes. Additionally, note that these values are echoed in
    plain text in the `heritrix_out.log` for operator reference.  As of
    Heritrix 3.1, the administrative username and password are no longer
    echoed to `heritrix_out.log`.  Also, as of Heritrix 3.1, if the
    parameter supplied to the -a command line option is a string
    beginning with "@", the rest of the string is interpreted as a local
    file name containing the operator login and password.  Thus, the
    credentials are not visible to other machines that use the process
    listing (ps) command.
2.  Launch the Heritrix-hosting Java VM with a user-account that has the
    minimum privileges necessary for operating the crawler. This will
    limit the damage in the event that the Web UI is accessed
    maliciously.
