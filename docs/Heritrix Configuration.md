# Heritrix Configuration

1.  Set the `JAVA_HOME` environment variable. The value should point to
    the JRE 1.6 Java installation.  For example, this variable might be
    set to `/usr/local/java/jre`
    ``` bash
    export JAVA_HOME=/usr/local/java/jre
    ```

2.  Set the `HERITRIX_HOME` environment variable. The value should be
    set to the main Heritrix directory, which is below the `bin`
    directory.
    ``` bash
    export HERITRIX_HOME=/PATH/TO/HERITRIX
    ```

    For example, an installation of Heritrix with a `bin` directory
    located at `/home/user/heritrix3.1/bin` would be configured as
    follows.
    ``` bash
    export HERITRIX_HOME=/home/user/heritrix3.1
    ```

3.  Set execute permission on the Heritirix startup file.
    ``` bash
    chmod u+x $HERITRIX_HOME/bin/heritrix
    ```

4.  To change the amount of memory allocated to Heritrix (the Java heap
    size), set the `JAVA_OPTS` environmental variable.  The following
    example allocates 1GB of memory to Heritrix.
    ``` bash
    export JAVA_OPTS=-Xmx1024M
    ```
