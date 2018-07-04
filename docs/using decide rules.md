# using decide rules

# How can I use `DecideRules` to include/exclude specific material from my crawl?

See also [Configuring Crawl Scope Using
DecideRules](Configuring%20Crawl%20Scope%20Using%20DecideRules).

From the [H1 User
Manual](http://crawler.archive.org/articles/user_manual/config.html#decidingscope):

> To define a Scope, the operator configures an ordered series of
> DecideRules. A URI under consideration begins with no assumed status.
> Each rule is applied in turn to the candidate URI. If the rule decides
> ACCEPT or REJECT, the URI's status is set accordingly. After all rules
> have been applied, if the URI's status is ACCEPT it is "in scope" and
> scheduled for crawling; if its status is REJECT it is discarded.
>
> There are no branches, but much of what nested conditionals can
> achieve is possible, in a form that should be be easier to follow than
> arbitrary expressions.

In other words, each `DecideRule` is applied in turn (i.e. each URI is
stamped with ACCEPT, REJECT or PASS); the last one to express a non-PASS
preference wins. So if you chain your `DecideRules` together, you should
be able to create the desired effect.

If you find "chaining together" `DecideRules` to get the effect you want
is too awkward, you may consider writing your own `DecideRules` based on
those already provided in the Heritrix source code. See [message
\#6250](http://tech.groups.yahoo.com/group/archive-crawler/message/6250?var=0&l=1)
from the `archive-crawler` list for an example.

More info about, and options for, using `DecideRules`:

**On 1/5/10 4:06 PM
([\#6529](http://tech.groups.yahoo.com/group/archive-crawler/message/6259)),
Gordon Mohr wrote:**

> A bit of background:
>
> We used to have a system of composable 'Filter' URI-test classes,
> with  
> AND/OR/NOT options.
>
> However, to implement common needs, the nesting got to be pretty
> deep  
> and complicated. Inside the setup, it wasn't very easy to understand  
> whether 'true' or 'false' meant 'ok to get' or 'not ok to get' or
> 'no  
> opinion'.
>
> We observed that it was very common to need rules where, if a test  
> passes, a URI is definitively "in" or "out" – while if the test does  
> not pass, no opinion is expressed either way. (Doing a series of
> these  
> in nested boolean expressions can get quite confusing.)
>
> So, we transitioned to scoping (and other per-URI go/no-go actions) as
> a  
> flat series of 'DecideRules', where the last to express an opinion
> wins.  
> That makes a lot of common needs a matter of ordering the rules
> (rather  
> than nesting) – first rule-in everything of general interest, then  
> rule-out those known to have problems.
>
> Which brings us to now.
>
> The series-of-DecideRules approach has worked well for our usual
> needs.  
> I thought we might eventually implement OR and AND rules, and they
> would  
> be relatively easy to add, but our internal crawls haven't had a  
> pressing need for that yet.
>
> That said, you have a number of options to implement what you need:
>
> -   create generic AND/OR/etc rules in Java, then compose your tests  
>     with them
> -   create a custom DecideRule class in Java which does exactly the  
>     test(s) you need, applying a decision if appropriate
> -   use the BeanShellDecideRule (Heritrix 1.x) or ScriptedDecideRule  
>     (H3) to write your custom test in a scripting language
>
> (If you do wind up implementing generic AND/etc composing-rules,
> we'd  
> welcome the code-contribution to the core project, even as I would  
> suggest people avoid that complexity in their scope rules whenever  
> possible.)
>
> Hope this helps,
>
> -   Gordon @ IA

See the
[DecideRules](http://crawler.archive.org/apidocs/org/archive/crawler/deciderules/package-summary.html)
package description in our JavaDocs for more details.
