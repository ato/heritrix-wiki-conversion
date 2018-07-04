# JVM Options

Miscellaneous notes on JVM options of interest to Heritrix operators.
Eventually any wisdom here will find its way into the launch-script
defaults; but new/untested/optional things may be discussed here.

Recommended:

-XX:+UseParallelOldGC

May be useful to speed full GC compactions on multi-core machines.See
<http://java.sun.com/javase/technologies/hotspot/gc/gc_tuning_6.html#par_gc>

-XX:+DoEscapeAnalysis

Available in 6u14, may improve performance; see
<http://java.sun.com/javase/6/webnotes/6u14.html>

-XX:+UseCompressedOops

Available in 6u14, may improve memory use/GC if using 64-bit JVM on
heaps &lt;32GB in size; see
<http://java.sun.com/javase/6/webnotes/6u14.html>

Maybe:

-XX:-UseGCOverheadLimit

Disables a OOME that is created not when memory is truly depleted, but
when an excessive amount of time is spent in GC. We've seen this OOME at
times when a requested memory-intensive report may have completed if not
for this OOME (albeit in an extreme length of time).
