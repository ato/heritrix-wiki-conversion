# Logging

To enable text console logging of authentication interactions, set the
`FetchHTTP` and `PreconditionEnforcer` log levels to fine

    org.archive.crawler.fetcher.FetchHTTP.level = FINE
    org.archive.crawler.prefetch.PreconditionEnforcer.level = FINE

This is done by editing the `logging.properties` file under the conf
directory.
