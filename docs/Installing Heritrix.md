# Installing Heritrix

# Heritrix 2.0.0 Tutorial

## Installing Heritrix

To install heritrix, simply unpack the tar.gz or zip file you downloaded
from the maven2 repository.

``` bash
$ tar -xzf heritrix-2.0.0-20071024.165839-74-heritrix.tar.gz
```

  

You'll end up with a `heritrix-2.0.0-SNAPSHOT` directory. It contains
the following subdirectories:

-   bin - contains shell scripts/batch files for lauching Heritrix.
-   lib - contains the third-party .jar files the Heritrix application
    requires to run.
-   conf - contains various configuration files (such as the
    configuration for Java logging, and pristine versions of the bundled
    profiles)
-   jobs - contains bundled crawl profiles (collections of settings),
    and is the default location where operator-created jobs are stored

The scripts in the `bin` subdirectory require that you set a
`HERITRIX_HOME` environment variable:

``` bash
$ cd heritrix-2.0.0-SNAPSHOT
$ export HERITRIX_HOME=`pwd`
```

  

You should probably edit your shell's startup file (eg, `.profile`) to
include the definition of `HERITRIX_HOME`.

Once `HERITRIX_HOME` is set, you are ready to run Heritrix in its
simplest form. See [Running Heritrix](Running%20Heritrix) for more
information.

[2.0 Tutorial](2.0%20Tutorial) \| [Running Heritrix](Running%20Heritrix)
