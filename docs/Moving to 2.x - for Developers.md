# Moving to 2.x - for Developers

-   3rd-party libraries are no longer stored in SVN. To acquire for
    running from an SVN working copy, run a Maven build inside your
    project directory, and ensure your project build-path variables
    include a definition for M2-REPO pointing to your maven local
    repository. (Typically, something like ~/.m2/repository)

<!-- -->

-   AList and its associated classes have gone away; HashMaps are used
    instead.
