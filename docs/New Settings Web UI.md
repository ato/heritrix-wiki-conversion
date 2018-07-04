# New Settings Web UI

(from some brainstorming of Paul, Michael Magin, Vinay, and Gordon on
April 27th)

The redone UI for operating on the new settings will likely have an area
for composing 'sheets' and one for assigning URIs/SURT-prefixes to
sheets.

(Gordon wondered: can there be more than one 'global defaults' sheet,
either as a bundle or an empty-prefix override?)

Some problems with current settings web UI include:

-   overrides sometimes don't work as expected, either having no effect
    or (at one point, bug probably fixed) changing global settings
-   it's unclear what can be effectively changed mid-crawl, and whether
    it is necessary to pause to do so. Can we better document/enforce
    these? Can we make all changes 'safe' either via some way of holding
    settings constant for a thread until a moment to safely atomically
    change is possible?

Though the SURT-prefixed-mapped-overrides are a superset of the current
functionality, the convenience of still being able to enter a plain
hostname should be retained.

View/edit frontier looks useful but isn't useful/efficient at scale –
can that be fixed?

Is there a way to interactively test what settings would apply to a URI
in the UI? (Same goes for scopes.)

Frontier report is oft-used but not optimal form for common tasks. A
sort by queue size (or other salient characteristics) would help. It is
often hard to view long URIs (exactly those of most interest for
trap-evaluation). Can color/size be used to highlight important data
needing attention? The seeds report – errors at top, clickable URIs – is
a good model.

The cross-links from reports to regex-filtered views of logs have
sometimes been broken in the past.

Can the crawl.log get syntax-highlighting or be clickable?

Bugs/defects/annoyances/unexpected-behaviors in old and new UIs should
be quickly and liberally reported to bug-tracking. (Err on the side of
over-reporting.)
