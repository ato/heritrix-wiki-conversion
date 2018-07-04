# New Features in Heritrix 3.0 and 3.1

New features in Heritrix 3.0:

1.  Ability to run multiple crawl jobs simultaneously.  The only limit
    on the number of crawl jobs that can run concurrently is the memory
    allocated to Heritrix.
2.  Single XML configuration file based on the
    [Spring](Glossary_5735753.html#Glossary-Spring) framework.  This
    file replaces order.xml and other Heritrix 1.x configuration files.
3.  Ability to browse and modify the
    configured [Spring](Glossary_5735753.html#Glossary-Spring) beans
    through an easy-to-use browser based utility.  See [Bean
    Browser](Browse%20Beans) .
4.  Enhanced extensibility through the
    [Spring](Glossary_5735753.html#Glossary-Spring) framework.  For
    example, domain overrides can be set at a very fine-grained level. 
    See [Sheets](Sheets).
5.  More secure user control console.  HTTPS is used to access and
    manipulate the user control console.
6.  Increased scalability.  Previously, crawls with large seed values
    (tens or hundreds of millions) might attempt to utilize more memory
    than allocated to Heritrix.  This would cause the crawl to crash. 
    Heritrix 3.0 eliminates these problems, allowing stable processing
    of large scale scrawls.
7.  Increased flexibility when modifying a running crawl.  Running
    crawls can be modified by using the [Bean Browser](Browse%20Beans)
    or by using the [Action Directory](Action%20Directory).
8.  Introduction of parallel queues.  When crawling specific sites that
    can handle large amounts of traffic, the parallel queues option can
    be used to open many concurrent crawling connections to a single
    site.
9.  A Scripting Console that accepts script input in various formats
    such as AppleScript and ECMAScript.  Scripting can be used to
    programmaticly access and manipulate the core components of
    Heritrix.

New features in Heritrix 3.1 can be found
﻿﻿[here](Release%20Notes%20-%20Heritrix%203.2.0).
