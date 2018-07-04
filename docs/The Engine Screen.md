# The Engine Screen

# The Heritrix Tutorial

## Using the User Interface

### The Engine Screen

When you click on an Engine ID on [The Home
Screen](The%20Home%20Screen), you will be taken to a page that displays
the profiles and jobs for that engine. A *profile* is a predefined
configuration for a web crawl. A *job* is either an active ongoing web
crawl, a "ready" job that can be run at any time but is not taking up
any engine resources yet, or a previously completed web crawl:

![](attachments/3755/90996899.png)

(Screenshots may vary from current UI.)

Since we just started Heritrix, we have no Active, Ready or Completed
jobs. Luckily Heritrix ships with two profiles. These profiles represent
two very common types of web crawls.

The first, `basic_seed_sites`, crawls only the sites that you entered as
seeds. For instance, if you enter "http://crawler.archive.org" as your
only seed, then "http://crawler.archive.org/a/b/c/d.html" would be
crawled, but  not"http://books.archive.org/index.html". There are some
exceptions to this rule. For instance, an image linked to from a seed
will be crawled, regardless of where that image resides. We set it up
this way because, typically, this is how operators expect the crawl to
behave.

The second profile, `broad_but_shallow`, differs in that it will crawl
any site, but only if that site is only one or two links away from a
seed.

For this tutorial, we will be using the `basic_seed_sites` profile to
crawl some of our favorite websites.

There are a number of links for each profile:

-   Sheets - displays the *configuration sheets* for the profile.
-   Seeds - displays the *seed list* for the profile.
-   Copy - creates a copy of the job or profile. You will have the
    option of creating a profile (template) or a ready-to-run job.
-   Delete - deletes the job or profile

Don't worry about configuration sheets just yet; we'll be getting to
those later. For now, we have to set up the profile's *seed list*. This
is the base list of URLs that we want to crawl. Click on the "Seeds"
link under `basic_seeds_profile`.

## Attachments:

![](images/icons/bullet_blue.gif){width="8" height="8"}
[engine.png](attachments/3755/90997201.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[engine\_alpha2.png](attachments/3755/90996899.png) (image/png)  
