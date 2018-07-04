# Unix Utility Scripts

Heritrix comes bundled with Unix utility scripts.

###### manifest\_bundle.pl

This script will bundle all resources referenced in the [crawl
manifest](crawl%20manifest) file.  A bundle is an uncompressed or
compressed tar ball.  The directory structure of the tar ball is:

-   Top level directory (crawl name)
-   Three default subdirectories
-   Any other arbitrary subdirectories
-   **Script Usage**

    ``` bash
    manifest_bundle.pl crawl_name manifest_file -f output_tar_file -z [ -flag directory]
    -f output tar file. If omitted output to stdout.
    -z compress tar file with gzip.
    -flag is any upper case letter. Default values C, L, and are R are set to
    configuration, logs and reports
    ```

<!-- -->

-   **manifest-bundle.pl example**

    ``` bash
    manifest_bundle.pl testcrawl crawl-manifest.txt -f /0/testcrawl/manifest-bundle.tar.gz -z -F filters
    ```

For the example above, the tar ball will contain the following directory
structure:  
\|- testcrawl

       \|- configurations

       \|- logs

       \|- reports

       \|- filters

###### hoppath.pl

This Perl script, found in `(HERETRIX_HOME)/bin` recreates the hop path
to the specified URI.  The hop path is the path of links (URIs) that
were followed to get to the specified URI.

**Script Usage**

``` bash
hoppath.pl crawl.log URI_PREFIX
crawl.log Full-path to Heritrix crawl.log instance.
URI_PREFIX URI we're querying about. Must begin 'http(s)://' or 'dns:'.
Wrap this parameter in quotes to avoid shell interpretation
of any '&' present in URI_PREFIX.
```

**hoppath.pl Example**

``` bash
hoppath.pl crawl.log 'http://www.house.gov/'
```

**hoppath.pl Result**

``` bash
2004-02-25-02-36-06 - http://www.house.gov/house/MemberWWW_by_State.html
2004-02-25-02-36-06 L http://wwws.house.gov/search97cgi/s97_cgi
2004-02-25-03-30-38 L http://www.house.gov/
```

The `L` in the example refers to the type of link followed.

###### RecoveryLogMapper

The `org.archive.crawler.util.RecoveryLogMapper` Java class is similar
to the `hoppath.pl` script.  It was contributed by Mike Schwartz.  The
`RecoveryLogMapper` parses a Heritrix recovery log file and builds maps
that allow a caller to look up any seed URI.  The `RecoveryLogMapper`
then returns a list of all URIs successfully crawled from the seed.  The
`RecoveryLogMapper` also can find the seed URI from which any crawled
URI was captured.
