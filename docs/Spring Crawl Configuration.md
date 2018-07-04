# Spring Crawl Configuration

Heritrix3 now makes use of the 'Spring Container' (and its XML-based
configuration format) to assemble a runnable crawl, choosing from among
alternate compatible implementations and settings values.

Developers will find it helpful to review the relevant chapter of
Spring's reference documentation to learn all the options provided by
the container and configuration format:

[Spring Framework, Chapter 3: The IoC
Container](http://static.springframework.org/spring/docs/2.5.x/reference/beans.html)

Some key insights to understanding this model are:

1.  Applications are large groupings of collaborating components, and
    often components have alternate, swappable implementations. (In our
    case, one runnable crawl job, with chosen settings and options, is
    one application.)
2.  The configuration file(s) declare all participating components, and,
    where necessary, initial assignment values.
3.  The 'container' uses the configuration file(s), plus other hints
    derived from the components themselves (like compatible types and
    settings-names), to assemble all components with their initial state
    and direct references to their collaborators. If a component is
    needed (as implied by other components), but insufficiently
    declared, errors are thrown.
