# Future Directions Brainstorming

Some future ideas for future crawler changes.

## Processor Chains

The current grouping by role (prefetch, fetch, extract, etc.) is a bit
constraining, especially when a processor could be used multiple places
or multiple processors need to work together.

Could processor chain be replaced with hooks & callbacks? There could be
a series of established callback points: start earlyPrereqs, latPreReqs,
earlyFetch, lateFetch, earlyAnalysis, middleAnalysis, lateAnalysis,
earlyFinish, lateFinish end. One module could  
hook itself in at multiple places – then we wouldn't have to use many
small Processors for simple functionality. Modules would by default hook
themselves in at reasonable places, but that could be overridden by
expert operators.

Alternatively, the processor chain could be merged into one chain, but
perhaps have advisory orderings – either integers suggestive of relative
position, or a series of recommended preconditions/postconditions, like
"shouldn't go after any Fetch processors".

## Prescheduling Chain / Scope vs. AlreadyIncluded

Can the testing done by scope and alreadyIncluded be merged into the
same process? We currently scope first then test for alreadyIncluded, on
the theory scoping is cheaper (never requires IO), but soem crawls might
benefit from the reverse, or certain efficient alreadyIncluded
mechanisms could make rejecting a commonly-encountered URI cheaper than
scoping it.

Is there a place for a 'prescheduling' chain that all discovered URIs
get fed through?
