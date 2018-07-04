# YouTube

## Heritrix 1:

To capture YouTube videos add the scope rules:

    +http://(com,youtube,c,
    +http://(com,youtube-nocookie,c,
    +http://(com,ytimg,
    +http://(be,youtu,
    +http://(com,youtube,www,)/crossdomain.xml

and include the following in order.xml.

At the end of the extractors section:

``` xml
      <newObject name="ExtractorImpliedURI-YoutubeEmbedded" class="org.archive.crawler.extractor.ExtractorImpliedURI">
        <boolean name="enabled">true</boolean>
        <newObject name="ExtractorImpliedURI-YoutubeEmbedded#decide-rules" class="org.archive.crawler.deciderules.DecideRuleSequence">
          <map name="rules">
          </map>
        </newObject>
        <string name="trigger-regexp">^(http://(?:www.)?youtube.com)/v/([a-zA-Z0-9_-]+).*$</string>
        <string name="build-pattern">$1/watch?v=$2</string>
        <boolean name="remove-trigger-uris">false</boolean>
      </newObject>
      <newObject name="ExtractorImpliedURI-YoutubeWatchPage" class="org.archive.crawler.extractor.ExtractorImpliedURI">
        <boolean name="enabled">false</boolean>
        <newObject name="ExtractorImpliedURI-YoutubeWatchPage#decide-rules" class="org.archive.crawler.deciderules.DecideRuleSequence">
          <map name="rules">
          </map>
        </newObject>
        <string name="trigger-regexp"/>
        <string name="build-pattern"/>
        <boolean name="remove-trigger-uris">false</boolean>
      </newObject>
```

In settings/com/youtube/settings.xml:

``` xml
  <object name="ExtractorImpliedURI-YoutubeWatchPage">
    <boolean name="enabled">true</boolean>
    <string name="trigger-regexp">^(http://[^/]*\.c\.youtube.com)/[^?]+\?(.*)$</string>
    <string name="build-pattern">$1/videoplayback?$2</string>
  </object>
```

In settings/com/youtube/c/settings.xml:

``` xml
  <object name="robots-honoring-policy">
    <string name="type">ignore</string>
  </object>
```

If you have questions regarding anything you see documented here, please
don't hesitate to contact the list at archive-crawler at yahoogroups dot
com.
