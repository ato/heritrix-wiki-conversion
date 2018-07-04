# Style Guide

This wiki section serves as the coding and interaction/UI-process style
guide for the Heritrix project and related open source web archiving
projects.

Guidance may occasionally be contradictory while topics are being
discussed; conflicting alternatives should each be well-described (with
supporting reasoning and precedent) to assist progress towards a
consensus/canonical expression.

## Other Authorities

Worthwhile references:

-   Sun's [Code Conventions for the Java Programming
    Language](http://java.sun.com/docs/codeconv/html/CodeConvTOC.doc.html) 
-   Geosoft's [Java Programming Style
    Guidelines](http://geosoft.no/development/javastyle.html) 

In the absence of guidance to the contrary below, recommendations in the
above sources may always be followed. 

## Code Style

(Some pulled from [Heritrix 1.X Developer
Manual](http://crawler.archive.org/articles/developer_manual/conventions.html)
.)

-   Use spaces, not tabs. Tabs should not appear in project source code.
-   Indent 4 spaces per level.
-   Place the opening bracket for a code block on the same line as the
    declaration/test expecting a block.
-   Use brackets even when a branch/block is only a single line of code
    (to provide an additional visual cue, and for robustness if other
    lines are added later).
-   Prefer longs over ints anywhere a large count of artifacts or
    large-sized file/range is possible. 
-   Prefer 'protected' over 'private' unless a consideration of
    potential subclass use suggests direct access will be dangerous.
-   (Deviation from Sun recommendations) It is permissable to declare
    local variables as close to first use as practical (as opposed to at
    the start of the enclosing block).
-   (Deviation from some recommendations) Early- and multiple- returns
    from methods are encouraged to minimize indention-levels, and handle
    simple or error cases quickly.
-   All classes and public methods should have Javadoc comments. See
    Sun's [style guide for
    Javadoc](http://java.sun.com/j2se/javadoc/writingdoccomments/#styleguide)
    for tips on good Javadoc comments.
-   Avoid broad catches (of all Exception or all Throwable) where
    possible. (Testing code and other all-or-nothing situations
    excepted.)
-   [Preserve toString()](Preserve%20toString())

## Interaction Style

-   [Usable in Lynx](Usable%20in%20Lynx)
-   [Reloadable](Reloadable)
-   Use exclamation points and ALL-CAPS sparingly. (Most warnings,
    errors, or other failure reports don't need such emphasis.)

## Development Style

-   [Issue best practices](Issue%20best%20practices)
-   [Commit best practices](Commit%20best%20practices)
