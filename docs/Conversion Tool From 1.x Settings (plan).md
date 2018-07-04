# Conversion Tool From 1.x Settings (plan)

-   [Crawl Order](#ConversionToolFrom1.xSettings(plan)-CrawlOrder)
-   [Settings](#ConversionToolFrom1.xSettings(plan)-Settings)
-   [Crawl Scope](#ConversionToolFrom1.xSettings(plan)-CrawlScope)
-   [Directories](#ConversionToolFrom1.xSettings(plan)-Directories)
-   [Overrides to H3
    Overlays](#ConversionToolFrom1.xSettings(plan)-OverridestoH3Overlays)
-   [Completed Jobs](#ConversionToolFrom1.xSettings(plan)-CompletedJobs)
-   [Testing & Graceful
    Failure](#ConversionToolFrom1.xSettings(plan)-Testing&GracefulFailure)
-   [Goals &
    Non-Goals](#ConversionToolFrom1.xSettings(plan)-Goals&Non-Goals)

Note: the target is now to offer a tool which takes configurations that
work in 1.14.3, and converts them to 3.0.

# Crawl Order

This should be mostly straightforward. The settings that went through
the most changes to H3 happen to be the ones that were the best
structured in the 1.14 order.xml, the CrawlOrder settings and the
CrawlController settings. By coming up with a H3 template for 1.14
migrations, it should be trivial to move CrawlOrder and CrawlController
settings via a simple mapping.

(A large table mapping 1.14 order.xml portions to edit that must be made
to a starting H3 template may be enough to handle almost all simple
orders.)

# Settings

The names of module settings have changed, but usually in simple
easy-to-understand ways. (For example, from dashed-words to camelCase.)
Many new settings were added, but these are almost universally
"autowire" settings to pull in other singleton beans. If the migration
template includes adequate default beans, then the new settings
shouldn't be problematic.

The package names of the module classes changed a lot, but in almost
algorithmic ways. I think we should use external properties files to
define mappings from 1.x names to 3.x names, and allow end users to
specify additional mappings in case we miss something.

# Crawl Scope

One area of concern is the class CrawlScope and its subclasses, which no
longer exists in 3.x. It was replaced by a generic DecideRuleSequence,
which can't really have primary status. We can create standard sets of
decide-rules that approximate the behavior of the legacy CrawlScope
subclasses.

# Directories

Heritrix 3 is closer to the 1.x approach, with several layers of
relativeness, than Heritrix 2. A simply copying-over of default paths to
the new analogous settings may be sufficient.

# Overrides to H3 Overlays

Migration of overrides from 1.14 to H3 poses some challenges. In 1.14,
each host/domain+setting combination had its own file. In H3, we'd want
to aggregate similar setting values into sheets, and then place the
host/domains into associations for that sheet. This is straightforward
assuming we can just keep it all in memory, but we'll have to come up
with some sane algorithm for naming the sheets that are created, as 1.14
overrides didn't really have names.

H3's options for overriding lists, maps and modules should be a superset
of what was possible in 1.14, but we should double-check that.

# Completed Jobs

There may be concern about how the migration tool should handle
completed jobs. Should those migrate? Should seeds, reports etc be
migrated? Should we copy state directories and arc files from the 1.x
directory to the H3 directory? Initially, the tool should only bring
over configuration information -- so that an identical (to the greatest
extent possible) crawl can be repeated in H3. Only if pressing needs for
converting other portions of completed jobs arise should the tool be
expanded.

# Testing & Graceful Failure

We can test the tool on all of our own crawl configurations, but there
are likely to be corner cases we won't encounter in such tests. It's
unclear how conversion errors should be handled. We could just include
faulty settings in the output sheet files; the web UI would then
complain loudly about those configurations and hopefully make human
intervention easier. We could also loudly log all portions of the
order.xml/settings.xml that don't yield to a formulaic conversion. (Even
some that do, might require a log warning that behavior is not
identical.)

# Goals & Non-Goals

It is a goal for any crawl based on our 1.14.x bundled defaults,
including only superficial changes (changes to Strings/primitive values
or addition/removal of commonly-used optional components), to convert
without problems.

It is a goal for all configurations used in active IA crawls --
including contract crawls, nat'l domain crawls, and Archive-It crawls --
to convert without problems or with only trivial problems that are easy
to manually remedy.

It is not a goal for components unused in IA crawls to convert without
problems. (We don't have the knowledge to evaluate the conversion.)
Ideally, the lookup-based mechanism for mapping old settings to new
settings will be flexible enough so that if the original authors or
heavy users of these tools help, it can cover these components as well.
However, at least until fixes are contributed, a helpful error
explaining those portions of the 1.14 config untranslated is sufficient.

![](plugins/servlet/confluence/placeholder/unknown-macro){.wysiwyg-unknown-macro}
