`python main.py $TweetID $TX-ID-OF-PUBLISHER-ANNOUNCEMENT [$path-to-file]`   

####Error Responses
`[{u'message': u'No status found with that ID.', u'code': 144}]`   
The above response means the tweet no longer exists. Treat as *not currently authorized*

####Response Format
`{"authdata":[{"foundtxid":"True"},{"foundname":"True"},{"verified":"True"},{"songmatch":"True"}]}`

####Field Definitions   
<list>
`foundtxid` = *provided TXID found in provided tweet*   
`foundname` = *publisher name at TXID found in provided tweet*   
`verified` = *twitter user's "verified" status*   
`songmatch` (only if path to file provided):    
`Not Found` = *Fingerprint from file provided not found in Musicbrainz db*  
`False` = *Fingerprint from file provided does not match artist name with provided Publisher name*  
`True` = *Fingerprint from file provided matches artist name with provided Publisher name*  

#####Examples:
Situation 1, Publisher name matches name found in public tweet, Musicbrainz artist name and fingerprint of song found in artists catalog in Musicbrainz, and Twitter profile *is* Verified 
<pre><code>
python main.py 657537600895496192 bf3c92f97728a4f0875cd837af0851cd340d855346928dc047157a07cf874214 Imogen-Heap/Tiny-Human.mp3

{"authdata":[{"foundtxid":"True"},{"foundname":"True"},{"verified":"True"},{"songmatch":"True"}]}
</code></pre>

Situation 2, Publisher name matches name found in public tweet, Musicbrainz artist name and fingerprint of song found in artists catalog in Musicbrainz, but Twitter profile is *not* Verified:   
<pre><code>
python main.py 654718134306213889 bf3c92f97728a4f0875cd837af0851cd340d855346928dc047157a07cf874214 Imogen-Heap/Tiny-Human.mp3

{"authdata":[{"foundtxid":"True"},{"foundname":"True"},{"verified":"False"},{"songmatch":"True"}]}
</code></pre>

Situation 3, Publisher name matches name found in public tweet, but twitter user not "Verified". Fingerprint of song file not found in Musicbrainz database:  
<pre><code>
python main.py 654370721641029632 93b62fc2a8f7cbb5a9e8e08395f88aa71187765d2239aae458d6b923b7a06506 /Users/devon/Desktop/bums/128/01\ DJ\ Day.mp3 
{"authdata":[{"foundtxid":"True"},{"foundname":"True"},{"verified":"False"},{"songmatch":"NotFound"}]}
</code></pre>



