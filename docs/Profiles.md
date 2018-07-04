# Profiles

A profile is a template for a crawl job.  It contains all the
configurations of a crawl job, but it is not considered "crawlable." 
Heritrix will not allow you to directly crawl a profile.  Only jobs
based on profiles can be crawled.

A common example of a profile configuration is to leave the
`metadata.operatorContactUrl` property undefined to force the operator
to input a valid value.

Profiles can be used as templates by leaving their configuration
settings in an invalid state.  In this way, an operator is forced to
choose his or her settings when creating a job from a profile.  This can
be  advantageous when an administrator must configure many different
crawl jobs to accommodate his or her crawling policy.

Whether a crawl job is a profile or a launchable job is determined by a
file name of primary config file. If it starts with "profile-," it is a
profile. Be careful when changing the name of a primary config file when
manually copying the profile to create a launch-able crawl job.

As of Heritrix 3.1 the "profile-" naming convention has been eliminated.
 There are no restrictions on a profile name.
