# Offline PageRank Analysis Notes

Heritrix 2.0.0 includes in its 'extras' directory utility classes and
scripts which can be used, together with other tools like Hadoop, to
perform an offline PageRank-calculation of a crawl's revealed link
graph.

These values can then influence future crawls, for example by assigning
URIs precalculated precedence values for a recrawl.

**Breakdown of steps involved in Offline PageRank analysis**

-   Extract source and target urls from ARC/DAT files. Save the
    target\_url &lt;space&gt; source\_url entries in a flat file
    (links.txt).
-   Canonicalize the target and source urls.
    ``` bash
    cat links.txt | $WAYBACK_HOME/bin/url-client -f 1 -f 2 > canonicalized_links.txt
    ```

      
      
-   Sort by target urls.
    ``` bash
    sort canonicalized_links.txt > sorted_canonicalized_links.txt
    ```

      
      
-   Assign unique integer identifiers to the target urls. By doing so,
    we are bringing into the computation, only those pages that have
    atleast one incoming link.

    ``` bash
    cat sorted_canonicalized_links.txt | assignUrlIndex.pl > input_links.txt
    ```

      
      

    > *assignUrlIndex.pl*: This script optimizes the input to
    > GenGraph.java by assigning a unique integer id to every target
    > URL. Input is a text file containing target\_url &lt;space&gt;
    > source\_url entries.  Output is target\_url\_id &lt;space&gt;
    > target\_url &lt;space&gt; source\_url. You definitely want to
    > preserve this output file as the next step's (GenGraph) output 
    > does not include full URLs.  You only need to preserve the first
    > two columns (target\_url\_id&lt;space&gt;target\_url).
    >
    > ``` bash
    > cat input_links.txt | cut -d" " -f1,2 | uniq > map.txt
    > ```
    >
    >   
    >   
    >   
    > map.txt will allow you to lookup the URL of a page with a given
    > integer id.  

      
      

-   Run the GenGraph hadoop job.  

    > *GenGraph.java*: This job reads in the output of assignUrlIndex.pl
    > (input\_links.txt: target\_url\_id &lt;space&gt; target\_url
    > &lt;space&gt; source\_url  records) and creates, using hadoop, an
    > 'outlink' webgraph file (pr0.txt) with the following entries:
    > (source\_url\_id &lt;tab&gt; initial\_pagerank\_score &lt;tab&gt;
    > O:target\_url\_id-1, target\_url\_id-2, ..., target\_url\_id-n).
    > The process also eliminates records where the source and target
    > urls are the same (self-loops). Dangling pages (pages with no
    > outgoing link) have (source\_url\_id &lt;tab&gt;
    > initial\_pagerank\_score &lt;tab&gt; O:dummy) entries.
    > source\_url\_id is a page with a total of 'n' outgoing links to
    > the target\_url\_id pages. initial\_pagerank\_score represents the
    > starting PageRank score of the source\_url and is set to 1.0. "O:"
    > is a tag that helps identify the comma separated list of
    > target\_url\_ids in the next hadoop process (PageRank). 'dummy' is
    > a dummy page that helps us handle dangling pages in the PageRank
    > algorithm. To this output file, add the following line: dummy
    > &lt;tab&gt; 1.0 &lt;tab&gt; O:dummy
    >
    > ``` bash
    > echo "dummy     1.0     O:dummy" >> pr0.txt
    > ```
    >
    >   
    >   
    >   

      
      
      

-   Run the PageRank hadoop job.  

    > *PageRank.java*: This job reads in the (source\_url\_id
    > &lt;tab&gt; initial\_pagerank\_score &lt;tab&gt;
    > O:target\_url\_id-1, target\_url\_id-2, ..., target\_url\_id-n)
    > records and generates (source\_url\_id &lt;tab&gt;
    > new\_pagerank\_score &lt;tab&gt; O:target\_url\_id-1,
    > target\_url\_id-2, ..., target\_url\_id-n) records. So, each run /
    > iteration of this job updates the pagerank score of the
    > source\_url\_id using the PageRank algorithm; the output of the
    > previous run is the input to the next run. You should run as many
    > iterations as it takes to reach convergence, where the output
    > scores and the input scores don't vary much (usually between 10
    > and 20 iterations). The random jump probability in the PageRank
    > algorithm is set to 0.15.

      
      

<!-- -->

-   Generate list of URLs with their assigned PageRank scores.  

    > Say, you ran the PageRank hadoop job for 10 iterations and the
    > output is saved in pr10.txt. Extract the source\_url\_id and the
    > pagerank scores from the file (first two columns). Then do a
    > 'join' of this file with the map.txt file to generate a list of
    > id&lt;tab&gt;pagerank\_score&lt;tab&gt;url entries. You will no
    > longer need the 'id' field, and hence, extract only the 2nd and
    > 3rd columns, giving you pagerank\_score&lt;tab&gt;url entries
    > (score\_uri.txt).
    >
    > ``` bash
    > cat pr10.txt | cut -f1,2 | sort -n > pr.txt
    > ```
    >
    >   
    >   
    >
    > ``` bash
    > join pr.txt map.txt | cut -f2,3 > score_uri.txt
    > ```
    >
    >   
    >   

      

More info on PageRank code:

Input:

A text file with lines of the following format:  
fromUrl initialPRscore O:toUrl1,toUrl2,...

where O: identifies a comma separated list of toUrls.

Output:

A text file with lines of the following format:  
fromUrl newPRscore O:toUrl1,toUrl2,...

The PageRank mapreduce job updates the PR score over one iteration. So,
repeat execution of the job with the output of the previous stage as the
input to the next stage for the desired number of iterations or till
convergence.

Working:

Map phase:  
----------

Read in the fromUrl, PRscore and the toUrls  
Compute outdegree (number of toUrls)  
Compute share of PR score to each toUrl (PRScoreShare =
PRScore/outdegree)  
For each toUrl in toUrl1, toUrl2,...,  
    EmitIntermediate(toUrl,PRScoreShare)  
EmitIntermediate(fromUrl,O:toUrl1,toUrl2...)

Reduce phase:  
------------

prvalue = 0  
   
For each v in values:  
  If v begins with O:  
    set toUrlString=value  
  else     
    prvalue+=v

prvalue\*=0.85  
prvalue+=0.15  
prvalueString = prValue + toUrlString (concatenation)  
Emit(key,prValueString)

-------------------------------------------------------------------------  
  

The Heritrix2 crawl-ordering functionality requires integer precedence
levels, where lower numbers are higher precedence. The PrecedenceLoader
utility class can take a file of URI -&gt; integer preset precedence
values. So, these scores require additional transformation before they
can be input to a future crawl.

Several ways of mapping scores to integer precedence levels are
possible; let us assume we want the to break the URIs into quintiles,
and map the top quintile to precedence '1', the next to '2', and so
forth.

TK
