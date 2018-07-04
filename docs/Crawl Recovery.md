# Crawl Recovery

During normal operation, the Heritrix Frontier keeps a journal. The
journal is kept in the logs directory. It is named
`frontier.recovery.gz`. If a crash occurs during a crawl, the
`frontier.recover.gz` journal can be used to recreate the approximate
status of the crawler at the time of the crash. In some cases, recovery
may take an extended period of time, but it is usually much quicker than
repeating the crashed crawl.

  

If using this process, you are starting an all-new crawl, with your same
(or modified) configuration, but this new crawl will take an extended
detour at the beginning where it uses the prior crawl's
frontier-recover.gz output(s) to simulate the frontier status
(discovered-URIs, enqueued-URIs) of the previous crawl. You would move
aside all ARC/WARCs, logs, and checkpoints from the earlier crawl,
retaining the logs and ARC/WARCs as a record of the crawl so far.

  

Any ARC/WARC files that exist with the `.open` suffix were not properly
closed by the previous run, and may include corrupt/truncated data in
their last partial record. You may rename files with a `.warc.gz.open`
suffix to `.warc.gz`, but consider validating such ARC/WARCs (by
zcat'ing the file to /dev/null to check gzip validity, or other ARC/WARC
tools for record completeness) before removing the ".open" suffix.

  

## full recover

  

To run the recovery process, relaunch the crashed crawler and copy the
`frontier.recover.gz` file into the [Action
Directory](Action%20Directory). Then re-start the crawl. Heritrix will
automatically load the recovery file and begin placing its URIs into the
Frontier for crawling.

  

If using a `.recover.gz` file, a single complete file must be used.
(This is so that the action directory processing of one file at a time
can do the complete first pass of 'includes', then the complete full
pass of 'schedules', from one file. Supplying multiple `.recover.gz`
files in series will result in an includes/schedules,
includes/schedules, etc. cycle which will not produce the desired effect
on the frontier.)

  

While the file is being processed, any checkpoints (manual or
auto-periodic) will **not** be a valid snapshot of the crawler state.
(The frontier-recovery log process happens via a separate thread/path
outside the newer checkpointing system.) Only when the file processing
is completed (file moved to 'done') will the crawler be in an accurately
checkpointable state.

  

Once URIs start appearing in the queues (the recovery has entered the
'schedules' pass), the crawler may be unpaused to begin fetching URIs
while the rest of the 'schedules' recovery pass continues. However, the
above note about checkpoints still applies: only when the
frontier-recovery file-processing is finished may an accurate checkpoint
occur. Also, unpausing the crawl in this manner may result in some URIs
being rediscovered via new paths before the original discovery is
replayed via the recovery process. (Many crawls may not mind this slight
deviation from the recovered' crawls state, but if your scoping is very
path- or hop- dependent it could make a difference in what is
scope-included.)

  

may produce Warnings

Note: feeding the entire frontier back to the crawler is likely to
produce many *"Problem line"* warnings in the job log. Some operators
find it useful to allow the entire recovery file to be ingested by the
crawler before attempting to resume (unpause), to help isolate this
chatter, and to minimize generating duplicate crawldata during recovery.

  

## split recover

  

An alternate way to run the recovery process is illustrated below. By
eliminating irrelevant lines early (outside the recovery process), it
may allow the recovery process to complete more quickly than the
standard process. It also allows the process to proceed from many files,
rather than a single file, so may give a better running indication of
progress, and chances to checkpoint the recover.

  

To run the alternate recovery process:

  

1.  move aside prior logs and ARCs/WARCs as above
2.  relaunch the crashed crawler
3.  Split any source `frontier.recover.gz` files using commands like the
    following:

  

``` bash
zcat frontier.recover.gz | grep '^Fs' | gzip > frontier.include.gz
zcat frontier.recover.gz | grep '^F+' | gzip > frontier.schedule.gz
```

  

1.  Build and launch the previously failed job (with the same or
    adjusted configuration). The job will now be paused.
2.  Move the `frontier.include.gz` file(s) into the action directory.
    The `action` directory is located at the same level in the file
    structure hierarchy as the `bin` directory. (If you have many, you
    may move them all in at once, or in small batches to better monitor
    their progress. At any point when all previously-presented files are
    processed – that is, moved to the 'done' directory – it is possible
    to make a valid checkpoint.)
3.  You may watch the progress of this 'includes' phase by viewing the
    web UI or `progress-statistics.log` and seeing the `discovered`
    count rise.
4.  When all `.includes` are finished loading, you can repeat the
    process with all the `.schedule` logs.
5.  When you notice a large number (many thousands) of URIs in the
    `queued` count, you may unpause the crawl to let new crawling
    proceed in parallel to the enqueueing of older URIs.

  

You **may** drop all `.include` and `.schedule` files into the action
directory before launch, if you are confident that the lexicographic
ordering of their names will do the right thing (present all
{{.include}}s first, and the {{.schedule}}s in the same order as the
original crawl). But, that leave little opportunity to adjust/checkpoint
the process: the action directory will discover them all and process
them all in one tight loop.

  

Note:  To be sure of success and current crawl status against any sort
of possible IO/format errors, in large recoveries of millions of
records, you may want to wait for each step to complete before moving a
file, or unpausing the job.  Instead of looking at progress-statistics,
simply wait for the file to move from action to action/done.  Then add
the second file.  Wait again.  Finally unpause the crawler. 

  

A recovery of 100M URIs may take days, so please be patient.
