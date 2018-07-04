# Force speculative embed URIs into single queue.

Use of the following setting will send speculative embeds ('X' hoppath
found via extraction from javascript) into a single, separate queue.

This was needed due to the javascript extractor enqueuing a large number
of faulty/non-existent URIs.

``` bash
<!-- extracted uris go to their own queue -->
<bean class='org.archive.crawler.spring.DecideRuledSheetAssociation'>
  <property name='rules'>
    <bean>
     <property name="regex" value=".*X$" />
    </bean>
  </property>
  <property name='targetSheetNames'>
   <list>
    <value>speculativeSingleQueue</value>
    <value>speculativeSingleQueueBalance</value>
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
 <bean id='speculativeSingleQueueBalance' class='org.archive.spring.Sheet'>
   <property name='map'>
     <map>
       <entry key='frontier.balanceReplenishAmount' value='2000000000' />
     </map>
   </property>
</bean>
```
