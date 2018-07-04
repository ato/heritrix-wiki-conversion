# Associating SURTs with the Sheet

# Heritrix 2.0 Tutorial

## Using the Web User Interface

### Associating SURTs with the Sheet

You should be looking at the Sheets screen for the `basic_seed_sites`
profile. Click on the "Add" next to "SURT Prefix Associations" under the
"Slowly" sheet. You will be taken to a form where you can enter SURT
prefixes to associate with the sheet:

![](attachments/3784/90997142.png)

Enter "archive.org" and click "Submit". Note you could have entered many
domains, URLs or SURTs in this form, and all of them would then be
associated with the sheet.

Clicking Submit takes you back to the sheet page. You can click "List"
next to "SURT prefix associations" to see your new association. Note
that the simple domain you entered - "archive.org" - was converted into
its SURT form, which is "http://(org,archive,". A full description of
SURTs is beyond the scope of this tutorial, but to make a long story
short, SURTs make it easy to apply settings to domains or subdomains, or
even to particular paths. Basically SURT form inverts the order of the
dot-separated tokens in the domain. So "http://www.archive.org" becomes
"http://(org,archive,www,".

When determining what configuration sheets to apply when crawling a
particular URI, the crawl engine first converts that URI to SURT form.
Then any association that's a prefix of that URI will have its sheet
applied to the configuration.

For instance, one of our seed URLs was `http://crawler.archive.org`. The
SURT form of that seed is `http://(org,archive,crawler,`. Since the
seed's SURT begins with `http://(org,archive,`, the seed will have the
Slowly sheet applied to its crawl configuration.

Confused? Then use the web UI to test the configuration for our seeds.
At the bottom of the sheets page, you'll see a section labeled "Test
Settings".

By entering a URL into the "Test Settings" box, then clicking the
"Settings" button, you will see the full configuration that will be
applied when crawling that URL. If you click the "Sheets" button
instead, you will see the SURT prefixes that matched the URL, as well as
the sheets associated with those prefixes.

Go ahead and enter our three seeds into the Test Settings box, and click
on both "Settings" and "Sheets" for each. You'll note that
`http://www.ilovepauljack.com` didn't have any associations that
matched, so it just uses the global sheet. Our other two seeds
(`http://crawler.archive.org` and `http://webteam.archive.org`) match
the `http://(org,archive,` SURT prefix, and so the Slowly sheet is
applied to those URLs.

This may not seem terribly useful now, but on a large crawl, you could
have dozens of sheets and hundreds of thousands of associations. You
could apply different settings for massive blog sites like myspace and
blogspot, different settings for newspaper sites, and so on.

Now that we've customized our crawl configuration a bit, we're ready to
launch the job!

## Attachments:

![](images/icons/bullet_blue.gif){width="8" height="8"}
[associate.png](attachments/3784/90997142.png) (image/png)  
