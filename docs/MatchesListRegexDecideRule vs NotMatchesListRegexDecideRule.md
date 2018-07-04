# MatchesListRegexDecideRule vs NotMatchesListRegexDecideRule

class *NotMatchesListRegexDecideRule* and *MatchesListRegexDecideRule*
are used by *DecideRuleSequence* for finding candidates for crawling, I
found them a little confusing in the beginning , but this is what I have
figured out.

class *NotMatchesListRegexDecideRule* inherits 
*MatchesListRegexDecideRule*

and returns the opposite(in terms of regex evaluation):

*protected boolean evaluate(CrawlURI object) {*  
*       return ! super.evaluate(object);*  
*}*

Again, the opposite in terms of "**regex evaluation**" not
"**decision**(ACCEPT,REJECT,NONE)" the decision by default for both is
"ACCEPT", so  you have the set the decision manually.

so:

if you want to accept a positive pattern match: add

MatchesListRegexDecideRule with &lt;property name="decision"
value="ACCEPT"/&gt;

if you want to reject a positive positive pattern match: add

MatchesListRegexDecideRule with &lt;property name="decision"
value="REJECT"/&gt;

and:

if you want to accept a negative pattern match: add

NotMatchesListRegexDecideRule with &lt;property name="decision"
value="ACCEPT"/&gt;

if you want to reject a negative pattern match: add

NotMatchesListRegexDecideRule with &lt;property name="decision"
value="REJECT"/&gt;

To be honest I think the existing of NotMatchesListRegexDecideRule is a
bit disturbing, as you can use MatchesListRegexDecideRule for almost
every thing.
