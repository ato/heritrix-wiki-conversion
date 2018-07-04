# Editing a Running Job

The configuration of a job can be edited while it is running.  This is
done through the [Browse
Beans](https://webarchive.jira.com/wiki/display/Heritrix/Browse+Beans) or
the ﻿[Scripting
Console](https://webarchive.jira.com/wiki/spaces/~hstern/pages/15008001/Scripting+a+Crawl)
link on the job page.  The Bean Browser allows you to edit runtime
properties of beans.

You can also use the scripting console to programmatically edit a
running job.

If changing a non-atomic value, it is a good practice to pause the crawl
prior to making the change, as some modifications to composite
configuration entities may not occur in a thread-safe manner.  An
example of a non-atomic change is adding a new Sheet.

As of Heritrix 3.1, handling of queue-budgeting and rotation/retirement
operations has been refactored to ensure mid-crawl changes (via new
overlay ﻿﻿Sheets or direct editing with the ﻿Bean Browser tool or
scripting-console) take effect immediately.  The DispositionProcessor
has a sheet-overlayable setting to apply this marking. More generally,
settings changes via new Sheets and Sheet-associations during a crawl
(as inserted via scripting) now take effect on all URIs being dequeued
for processing, rather than just newly-discovered URIs.  Therefore,
changes via bean-browse/scripting/new-sheet-overlays take effect
immediately.
