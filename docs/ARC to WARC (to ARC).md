# ARC to WARC (to ARC)

There is some interest in converting material originally stored as ARC
files into the WARC format.

-   [basic level](#ARCtoWARC(toARC)-basiclevel)
    -   [advanced: preserving ability to reconstruct exact
        ARC](#ARCtoWARC(toARC)-advanced:preservingabilitytoreconstructexactARC)
    -   [why only reconstruct uncompressed
        ARC?](#ARCtoWARC(toARC)-whyonlyreconstructuncompressedARC?)
-   [current work](#ARCtoWARC(toARC)-currentwork)
    -   [ARC to WARC](#ARCtoWARC(toARC)-ARCtoWARC)
    -   [WARC to ARC](#ARCtoWARC(toARC)-WARCtoARC)

# basic level

At one level, this is very simple: every ARC record (other than the
starting arcinfo record) can be converted to a WARC 'response' or
'resource' record in a straightforward way.

## advanced: preserving ability to reconstruct exact ARC

However, to have total confidence that the WARC format retains all ARC
info, it would be desirable to have a round-trip process that can be
proven to restore the original ARC, if desired. This implies storing the
original ARC name, arcinfo record, and additional information to assist
reconstruction and verify completeness of the reconstructed ARC.

So, an idea for an enhanced ARC-to-WARC translation convention, that
would assist in later WARC-to-ARC reconstitution, would be:

-   store the first ARC record as a resource record, with the
    WARC-Target-URI retaining the unofficial ad-hoc 'filedesc:' URL.
-   store all subsequent ARC records as 'response' (for HTTP) or
    'resource' (for DNS) records as appropriate
-   add to each such ARC-derived WARC record three extra named-fields:
    -   arc-header-line: verbatim original ARC header line
    -   arc-file: for the original ARC, its filename,
        uncompressed-length, and uncompressed-full-file-hash (algo TBD)
    -   arc-range: byte-range of original uncompressed ARC filled by
        this record
-   adopt some extra arbitrary range/diff-patch mechanism so that even
    flawed ARCs can be reconstructed. (At times, buggy ARCs have been
    written; at times, the newlines-between-records convention has
    changes; sometimes ARCs become internally corrupted, but with valid
    records before and after the problem regions)

Reconstructing an exact uncompressed original ARC is thus a matter of:

1.  finding all the WARC records which describe every range (including
    flaws) composing up to the full original uncompressed length;
2.  reproducing each of their arc-header-lines and blocks in order
3.  confirming the result has the right length and full-file hash

To be determined: whether ranges are inclusive or exclusive of
between-record newlines, and whether any small gaps (1-N bytes) can be
filled with newlines.

## why only reconstruct uncompressed ARC?

By my understanding, it's not guaranteed that two gzip libraries, even
if fed the same '1-9' compression level, will return the exact same
compressed stream for the same input. Instead, it is only required that
they will give a comrpessed stream that when uncompressed yields the
original input.

So even if you perfectly reconstruct the uncompressed-ARC, verifying its
strong hash matches the original value, if you then apply
record-by-record compression, you may not exactly match the original
record-by-record gzipped ARC. (The gzip header extensions usually added
to each record – 'LX' – could also complicate things if not reproduced
exactly.)

So it seems reproducing the **uncompressed** ARC is an attainable goal,
just by being sure to save all relevant record metadata, while
reproducing the compressed ARCs would require holding gzip routines in
perfect alignment ove

# current work

## ARC to WARC

A prototype Arc2Warc class has existed in one form or another dating
back to early WARC drafts. However, until recently (March 2010) it
incorrectly wrote ARC HTTP response records as WARC 'resource' records
rather than 'response' records. See
[HER-1748](https://webarchive.jira.com/browse/HER-1748) for details.

## WARC to ARC

here's an example of the WARC named-fields, as written by trunk code
2010/03/11, which might help support ARC reconstruction:

    ARC-Header-Line: http://www.archive.org/ 207.241.229.39 20100304201318 text/html 30593
    ARC-File: /home/steve/workspace/heritrix1/jobs/msg6422-20100304201129898/arcs/IAH-20100304201314-00000-takomaki-8080.arc.gz
    ARC-Gzip-Offset: 1305
    ARC-Length: 30593

TBD
