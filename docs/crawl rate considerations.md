# crawl rate considerations

# Why isn't Heritrix crawling as fast as I expected?

We are often asked why Heritrix is crawling slower than expected, and
the answer can usually be divided into the following considerations:

-   If your crawl is going more slowly than expected, and your machine
    seems to have extra capacity or idle threads, see [unexpectedly slow
    crawling on idle
    crawler](unexpectedly%20slow%20crawling%20on%20idle%20crawler)
-   If your crawl is busy with all threads active and the machine busy,
    but you'd like it to go even faster, see [making a busy crawl go
    faster](making%20a%20busy%20crawl%20go%20faster)

Politeness or resource optimization?

The important factor to consider is whether you are crawling a **small
number of sites** or a **large number** (having many independent
queues). In the case of the former, your politeness policy and/or
coordination with site maintainers is your primary concern, for the
latter, resource optimizations (like using more RAM or a different disk
layout) may be of benefit.
