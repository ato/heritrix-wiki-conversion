# crawling JavaScript

# Can Heritrix collect websites which make heavy use of Javascript?

Heritrix will collect referenced script files (as in &lt;SCRIPT&gt;
elements). However, discovery of URIs inside javascript code is limited.

Heritrix does not currently include a browser-equivalent Javascript
interpreter and page (DOM) model. It does scan script code for strings
that appear likely to be absolute or relative URIs, and will treat these
the same as other discovered outlinks. In many cases, this finds
valuable content, while in others, it causes requests to invalid URIs at
sites. (Usually this results in harmless 'not found' responses, but it
can inconvenience sites, and so this 'speculative' crawling of possible
URIs can be turned off.) This simple scanning will not find URIs that
are dynamically composed from parts in scripts.

Heritrix may better simulate browsers to discover more links in the
future. Two previous student 'Google Summer of Code' projects suggest
possible approaches. The [Browser
Monkeys](https://webarchive.jira.com/wiki/spaces/SOC06/pages/1400/Leverage+browsers+for+link-extraction)
project remote-controls a Firefox instance to observe its pattern of
followup requests, and thus gains the benefits of Firefox's own
Javascript/DOM implementation. The [Javascript Cloaking
Detection](Web%20Spam%20Detection%20for%20Heritrix) project embedded the
open-source Rhino Javascript engine and Lobobrowser mock-browser into
Heritrix to discover links created by predictable Javascript actions.
Neither of these techniques are yet integrated into an official Heritrix
release or scheduled for a specific future release.

Even with better Javascript link-discovery, highly dynamic sites which
involve repeated user-specific browser-to-server interaction (such as
after a user login, and with 'AJAX' background operations refreshing
only part of a page) will not be meaningfully harvestable with current
automated techniques.
