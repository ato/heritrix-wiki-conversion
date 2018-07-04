# Reloadable

Web pages with information that may change after its initial load should
be safe and easy to reload – either via the browser's reload button or
some in-page control.

In particular, pages resulting from POSTs should whenever possible
redirect to a stable, reload-in-place version of the action's results
(for which a reload neither prompts about rePOSTing nor duplicates the
original action).
