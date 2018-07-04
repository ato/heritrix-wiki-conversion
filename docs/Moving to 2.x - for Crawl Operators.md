# Moving to 2.x - for Crawl Operators

-   The Web UI is now a separate program from the core crawl-engine.
    They may now run in separate JVMs or even different machines,
    communicating via JMX. In the common case where you want one engine
    and one web UI, this can be acheived in a single JVM with
    command-line options.
-   The 'modules', 'submodules', and 'settings' job configuration pages
    are now rolled into the idea of a configuration 'sheet'. Alternate
    implementation modules are specified by going to 'details' from the
    sheet editor.
-   'Overrides' are achieved by creating additional sheets changing some
    settings/implementations, then associating those override sheets
    with certain SURT prefixes. For URIs of the given prefix, the
    alternate settings are used.
