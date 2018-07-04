# Disposition Chain Processors

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Processor Name<br />
</p></th>
<th><p>Description<br />
</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>warcWriter<br />
</p></td>
<td><p>This processor writes the archival WARC files.<br />
</p></td>
</tr>
<tr class="even">
<td><p>candidates<br />
</p></td>
<td><p>This processor sends the outlinks of the fetched URI back to the Candidate Chain for processing.<br />
</p></td>
</tr>
<tr class="odd">
<td><p>disposition<br />
</p></td>
<td><p>This processor updates crawl statistics, data structures, and Frontier decisions.</p></td>
</tr>
</tbody>
</table>
