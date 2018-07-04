# Heritrix3 Useful Scripts

Heritrix 3 H3 useful scripts to run in the scripting console.

-   [get a list of seeds from the seeds file on
    disk](#Heritrix3UsefulScripts-getalistofseedsfromtheseedsfileondisk)
-   [print out available variables from the scripting
    context](#Heritrix3UsefulScripts-printoutavailablevariablesfromthescriptingcontext)
-   [printProps(obj) and using
    appCtx.getData()](#Heritrix3UsefulScripts-printProps(obj)andusingappCtx.getData())
-   [changing a regex decide
    rule](#Heritrix3UsefulScripts-changingaregexdeciderule)
-   [adding an exclusion
    surt](#Heritrix3UsefulScripts-addinganexclusionsurt)
-   [take a gander at the decide
    rules](#Heritrix3UsefulScripts-takeaganderatthedeciderules)
-   [check your metadata](#Heritrix3UsefulScripts-checkyourmetadata)
-   [add a sheet forcing many queues into 'retired'
    state](#Heritrix3UsefulScripts-addasheetforcingmanyqueuesinto'retired'state)
-   [create a sheet for forcing queue assignment, and associate two
    surts with
    it](#Heritrix3UsefulScripts-createasheetforforcingqueueassignment,andassociatetwosurtswithit)
-   [add a decide rule sheet
    association](#Heritrix3UsefulScripts-addadeciderulesheetassociation)
-   [apply sheet (ignoreRobots) to a list of URIs as strings, taken from
    the seeds.txt
    file](#Heritrix3UsefulScripts-applysheet(ignoreRobots)toalistofURIsasstrings,takenfromtheseeds.txtfile)
-   [reconsiderRetiredQueues](#Heritrix3UsefulScripts-reconsiderRetiredQueues)
-   [run arbitrary command on the machine (BE CAREFUL WITH THIS,
    OBVIOUSLY)](#Heritrix3UsefulScripts-runarbitrarycommandonthemachine(BECAREFULWITHTHIS,OBVIOUSLY))
-   [list pending urls](#Heritrix3UsefulScripts-listpendingurls)
-   [GC Garbage Collector Collection
    Info](#Heritrix3UsefulScripts-GCGarbageCollectorCollectionInfo)
-   [Retrieving history for
    URI](#Heritrix3UsefulScripts-RetrievinghistoryforURI)
-   [dump surts](#Heritrix3UsefulScripts-dumpsurts)
-   [Add cookie to running
    crawl](#Heritrix3UsefulScripts-Addcookietorunningcrawl)
-   [Delete urls matching regex from
    frontier](#Heritrix3UsefulScripts-Deleteurlsmatchingregexfromfrontier)
-   [Force a site to crawl through a
    proxy](#Heritrix3UsefulScripts-Forceasitetocrawlthroughaproxy)
-   [Force wake all snoozed
    queues](#Heritrix3UsefulScripts-Forcewakeallsnoozedqueues)
-   [Add a DecideRule to scope rejecting the second speculative
    hop](#Heritrix3UsefulScripts-AddaDecideRuletoscoperejectingthesecondspeculativehop)
-   [Retire Queues Matching
    Regex](#Heritrix3UsefulScripts-RetireQueuesMatchingRegex)
-   [Determine which multi-machine crawler is responsible for given
    URI](#Heritrix3UsefulScripts-Determinewhichmulti-machinecrawlerisresponsibleforgivenURI)

### get a list of seeds from the seeds file on disk

``` bash
//groovy
//this is not the original list of seeds. it's just the contents of the seeds file, filtered.
appCtx.getBean("seeds").textSource.file.readLines().findAll{l -> l =~ /^http/}.unique().each{seedStr ->
 rawOut.println(seedStr)
}
```

### print out available variables from the scripting context

``` bash
//groovy
this.binding.getVariables().each{ rawOut.println("${it.key}=\n ${it.value}\n") }
```

### printProps(obj) and using appCtx.getData()

The bash `ls` command is to the working directory what this method is to
a java object. It uses [getProperties provided by
groovy](http://groovy.codehaus.org/groovy-jdk/java/lang/Object.html#getProperties%28%29).

Putting printProps in appCtx.getData() means you don't have to include
the whole printProps definition later, which helps keep scripts short
and managable. appCtx.getData() is a java.util.Map. There is more
information [from Groovy](http://groovy.codehaus.org/JN1035-Maps)
(detailed) and [from
IBM](http://www.ibm.com/developerworks/java/tutorials/j-groovy/section9.html)
(concise) about that.

``` bash
//Groovy
appCtxData = appCtx.getData()
appCtxData.printProps = { rawOut, obj ->
  rawOut.println "#properties"
  // getProperties is a groovy introspective shortcut. it returns a map
  obj.properties.each{ prop ->
    // prop is a Map.Entry
    rawOut.println "\n"+ prop
    try{ // some things don't like you to get their class. ignore those.
      rawOut.println "TYPE: "+ prop.value.class.name
    }catch(Exception e){}
  }
  rawOut.println "\n\n#methods"
  try {
  obj.class.methods.each{ method ->
    rawOut.println "\n${method.name} ${method.parameterTypes}: ${method.returnType}"
  } }catch(Exception e){}
}

// above this line need not be included in later script console sessions
def printProps(x) { appCtx.getData().printProps(rawOut, x) }

// example: see what can be accessed on the frontier
printProps(job.crawlController.frontier)
```

### changing a regex decide rule

It's a wise idea to pause the crawl while modifying collections it
depends on.

``` bash
//Groovy
pat = ~/your-regex-here/
dec = org.archive.modules.deciderules.DecideResult.REJECT
regexRuleObj = appCtx.getBean("scope").rules.find{ it.class == org.archive.modules.deciderules.MatchesListRegexDecideRule }
regexRuleObj.decision = dec
rawOut.println("decision: "+ regexRuleObj.decision)
regexRuleObj.regexList.add(pat)
rawOut.println("regexList: "+ regexRuleObj.regexList)
```

### adding an exclusion surt

``` bash
//Groovy
rule = appCtx.getBean("scope").rules.find{ rule ->
  rule.class == org.archive.modules.deciderules.surt.SurtPrefixedDecideRule &&
  rule.decision == org.archive.modules.deciderules.DecideResult.REJECT
}

theSurt = "http://(org,northcountrygazette," // ncg is cranky. avoid.
rawOut.print( "result of adding theSurt: ")
rawOut.println( rule.surtPrefixes.considerAsAddDirective(theSurt) )
rawOut.println()

//dump the list of surts excluded to check results
rule.surtPrefixes.each{ rawOut.println(it) }
```

**Adding an exclusion surt for a list of URIs**

``` groovy
rule = appCtx.getBean("scope").rules.find{ rule ->
  rule.class == org.archive.modules.deciderules.surt.SurtPrefixedDecideRule &&
  rule.decision == org.archive.modules.deciderules.DecideResult.REJECT
}

def stringList = [ "www.example.com", "example.net", "foo.org" ]


stringList.each() { rawOut.println( rule.surtPrefixes.considerAsAddDirective("${it}")) }
rule.surtPrefixes.each{ rawOut.println(it) }
```

### take a gander at the decide rules

``` bash
//Groovy
def printProps(obj){
  // getProperties is a groovy introspective shortcut. it returns a map
  obj.properties.each{ prop ->
    // prop is a Map.Entry
    rawOut.println "\n"+ prop
    try{ // some things don't like you to get their class. ignore those.
      rawOut.println "TYPE: "+ prop.value.class.name
    }catch(Exception e){}
  }
}
 
// loop through the rules
counter = 0
appCtx.getBean("scope").rules.each { rule ->
  rawOut.println("\n###############${counter++}\n")
  printProps( rule )
}
```

### check your metadata

``` bash
appCtx.getBean("metadata").keyedProperties.each{ k, v ->
  rawOut.println( k)
  rawOut.println(" $v\n")
}
```

### add a sheet forcing many queues into 'retired' state

``` bash
// force-retire all .org queues
mgr = appCtx.getBean("sheetOverlaysManager")
mgr.putSheetOverlay("forceRetire","disposition.forceRetire",true)
mgr.addSurtAssociation("http://(org,","forceRetire")
```

### create a sheet for forcing queue assignment, and associate two surts with it

``` bash
mgr = appCtx.getBean("sheetOverlaysManager");
newSheetName = "urbanOrgAndTaxpolicycenterOrgSingleQueue"
mgr.putSheetOverlay(newSheetName, "queueAssignmentPolicy.forceQueueAssignment", "urbanorg_and_taxpolicycenterorg");
mgr.addSurtAssociation("http://(org,urban,", newSheetName);
mgr.addSurtAssociation("http://(org,taxpolicycenter,", newSheetName);

//check your results
mgr.sheetNamesBySurt.each{ rawOut.println(it) }
rawOut.println(mgr.sheetNamesBySurt.size())
```

### add a decide rule sheet association

force queue assignment based on the hop path

``` bash
mgr = appCtx.getBean("sheetOverlaysManager");
newSheetName = "speculativeSingleQueue"
dr = new org.archive.crawler.spring.DecideRuledSheetAssociation()
hpreg = new org.archive.modules.deciderules.HopsPathMatchesRegexDecideRule()
hpreg.setRegex(~/.*X$/)
dr.setRules(hpreg)
dr.setTargetSheetNames([newSheetName])
dr.setBeanName("forceSpeculativeQueueAssociation")
mgr.putSheetOverlay(newSheetName, "queueAssignmentPolicy.forceQueueAssignment", "speculative-queue");
mgr.addRuleAssociation(dr)
```

similar xml:

``` bash
 <bean class='org.archive.crawler.spring.DecideRuledSheetAssociation'>
  <property name='rules'>
    <bean class="org.archive.modules.deciderules.HopsPathMatchesRegexDecideRule">
     <property name="regex" value=".*X$" />
    </bean>
  </property>
  <property name='targetSheetNames'>
   <list>
    <value>speculativeSingleQueue</value>
   </list>
  </property>
 </bean>
 <bean id='speculativeSingleQueue' class='org.archive.spring.Sheet'>
  <property name='map'>
   <map>
    <entry key='queueAssignmentPolicy.forceQueueAssignment' value='speculative-queue' />
   </map>
  </property>
 </bean>
```

### apply sheet (ignoreRobots) to a list of URIs as strings, taken from the seeds.txt file

``` bash
//Groovy
sheetName = "ignoreRobots"
mgr = appCtx.getBean("sheetOverlaysManager")
 
//test that you got the name right
if ( ! mgr.sheetsByName.containsKey( sheetName ) ) {
 rawOut.println( "sheet $sheetName does not exist. your choices are:" )
 mgr.sheetsByName.keySet().each{ rawOut.println(it) }
 return;
}
 
//look for lines in the seeds.txt file starting with http
appCtx.getBean("seeds").textSource.file.readLines().findAll{ l ->
 l =~ /^http/
}.collect{ uriStr ->
 //turn the domain into a surt and remove www
 org.archive.util.SurtPrefixSet.prefixFromPlainForceHttp("http://"+ new org.apache.commons.httpclient.URI(uriStr).host).replaceAll( /www,$/, "" )
}.unique().each{ seedSurt ->
 rawOut.println("associating $seedSurt")
 try{
  //ignore robots on the domain
  mgr.addSurtAssociation( seedSurt, sheetName)
 } catch (Exception e) {
  println("caught $e on $seedSurt")
 }
}
//review the change
mgr.sheetNamesBySurt.each{ k, v -> rawOut.println("$k\n $v\n") }
```

### reconsiderRetiredQueues

if frontier related settings have changed (for instance, budget), this
can bring queues out of retirement

``` bash
appCtx.getBean("frontier").reconsiderRetiredQueues()
```

### run arbitrary command on the machine (BE CAREFUL WITH THIS, OBVIOUSLY)

``` bash
command = "ls";
proc = Runtime.getRuntime().exec(command);

stdout = new BufferedReader(new InputStreamReader(proc.getInputStream()));
while ((line = stdout.readLine()) != null) {
    rawOut.println("stdout: " + line);
}

stderr = new BufferedReader(new InputStreamReader(proc.getErrorStream()));
while ((line = stderr.readLine()) != null) {
    rawOut.println("stderr: " + line);
}
```

There are [groovier ways to do
it](http://groovy.codehaus.org/Executing+External+Processes+From+Groovy),
starting with the basic

    rawOut.println( "ls".execute().text )

### list pending urls

``` bash
// groovy
// see org.archive.crawler.frontier.BdbMultipleWorkQueues.forAllPendingDo()

import com.sleepycat.je.DatabaseEntry;
import com.sleepycat.je.OperationStatus;

MAX_URLS_TO_LIST = 1000

pendingUris = job.crawlController.frontier.pendingUris

rawOut.println "(this seems to be more of a ceiling) pendingUris.pendingUrisDB.count()=" + pendingUris.pendingUrisDB.count()
rawOut.println()

cursor = pendingUris.pendingUrisDB.openCursor(null, null);
key = new DatabaseEntry();
value = new DatabaseEntry();
count = 0;

while (cursor.getNext(key, value, null) == OperationStatus.SUCCESS && count < MAX_URLS_TO_LIST) {
    if (value.getData().length == 0) {
        continue;
    }
    curi = pendingUris.crawlUriBinding.entryToObject(value);
    rawOut.println curi
    count++
}
cursor.close(); 

rawOut.println()
rawOut.println count + " pending urls listed"
```

### GC Garbage Collector Collection Info

``` bash
// beanshell
for (gcMxBean: java.lang.management.ManagementFactory.getGarbageCollectorMXBeans()) {
    rawOut.println(gcMxBean.getName() + " pools=" + java.util.Arrays.toString(gcMxBean.getMemoryPoolNames()) + " count=" + gcMxBean.getCollectionCount() + " time=" + gcMxBean.getCollectionTime());
}
```

### Retrieving history for URI

``` bash
//Groovy
uri="http://example.com/"
loadProcessor = appCtx.getBean("persistLoadProcessor") //this name depends on config
key = loadProcessor.persistKeyFor(uri)
history = loadProcessor.store.get(key)
history.get(org.archive.modules.recrawl.RecrawlAttributeConstants.A_FETCH_HISTORY).each{historyStr ->
    rawOut.println(historyStr)
}
```

### dump surts

``` bash
// beanshell

// permit access to protected variable surtPrefixes
setAccessibility(true);

// assumes SurtPrefixedDecideRule is second rule in scope; adjust number for nth rule
rawOut.print(appCtx.getBean("scope").rules.get(1).surtPrefixes);
```

### Add cookie to running crawl

``` bash
//Groovy
cookies = appCtx.getBean("cookieStorage").getCookiesMap();
epochSeconds = Long.parseLong("2094586238") //Expiration in 2036
expirationDate = (epochSeconds >= 0 ? new Date(epochSeconds * 1000) : null);
 
//Domain (compare with actual cookie, may be partial domain), Name, Value, Path, Expiration, isSecure (cookie only over https)
cookie = new org.apache.commons.httpclient.Cookie("www.trivediforcongress.com", "splash","1","/",expirationDate,false); 
//Indicates whether the cookie had a path specified in a path attribute of the Set-Cookie header
cookie.setDomainAttributeSpecified(true);

rawOut.println(cookie.getSortKey());
rawOut.println(cookie);
cookies.put(cookie.getSortKey(), cookie);
```

### Delete urls matching regex from frontier

``` bash
// groovy
count = job.crawlController.frontier.deleteURIs(".*", "^http://de.wikipedia.org/.*")
rawOut.println count + " uris deleted from frontier"
```

### Force a site to crawl through a proxy

``` bash
//groovy
mgr = appCtx.getBean("sheetOverlaysManager");
newSheetName = "proxyFetch"
mgr.putSheetOverlay(newSheetName, "fetchHttp.httpProxyHost", "my.proxy.host"); //hostname or ip
mgr.putSheetOverlay(newSheetName, "fetchHttp.httpProxyPort", "8443"); //port

mgr.addSurtAssociation("http://(com,timgriffinforcongress,", newSheetName);

//check your results
mgr.sheetNamesBySurt.each{ rawOut.println(it) }
rawOut.println(mgr.sheetNamesBySurt.size())
```

### Force wake all snoozed queues

``` groovy
//Groovy
 
countBefore = job.crawlController.frontier.getSnoozedCount()


job.crawlController.frontier.forceWakeQueues()
countAfter = job.crawlController.frontier.getSnoozedCount()

rawOut.println("Snoozed queues.")
rawOut.println(" - Before: " + countBefore)
rawOut.println(" - After: " + countAfter)
```

### Add a DecideRule to scope rejecting the second speculative hop

Pause the crawl before doing this.

``` groovy
//Groovy

scope = appCtx.getBean("scope")
hpm = new org.archive.modules.deciderules.HopsPathMatchesRegexDecideRule()
hpm.regex = ~/.*X.*X.*/
hpm.decision = org.archive.modules.deciderules.DecideResult.REJECT
rawOut.println scope.rules.add(hpm)
scope.rules.each{rawOut.println it}
```

### Retire Queues Matching Regex

Set a sheet overlay by Regex and set a small budget for matching domains

``` groovy
//Groovy

dr = new org.archive.crawler.spring.DecideRuledSheetAssociation()
matchreg = new org.archive.modules.deciderules.MatchesRegexDecideRule()
matchreg.setRegex(~/^https?:\/\/([^\/])*((discount)|(cheap))[^\/]*.*$/)
dr.setRules(matchreg)
dr.setBeanName("cheap-discount-domain-small-budget")
dr.setTargetSheetNames(["smallBudget"])

//smallBudget bean exists by default
```

### Determine which multi-machine crawler is responsible for given URI

Interpret the output as an index into the divert map.

``` groovy
//Groovy
import org.archive.modules.CrawlURI
import org.archive.net.UURIFactory
uris=['http://foo.com','http://bar.org']
mapper = appCtx.getBean("hashCrawlMapper")
uris.each{ uri -> rawOut.println(uri + ":" + mapper.map(new CrawlURI(UURIFactory.getInstance(uri)))) }
```
