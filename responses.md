####Field 1
True = Name in tweet matches publisher name

####Field 2
True = TXID in tweet matches provided txid

####Field 3 (if a file was provided)  
  Not Found = Fingerprint from file provided not found in Musicbrainz db  
  False = Fingerprint from file provided does not match artist name with provided Publisher name  
  True = Fingerprint from file provided matches artist name with provided Publisher name  

####Field 4 (if a file was provided)  
####Field 3 (if a file is not provided)
True = Twitter user is "Verified"

#####Examples:
Situation 1, Publisher name matches name found in public tweet, Musicbrainz artist name and fingerprint of song found in artists catalog in Musicbrainz, and Twitter profile *is* Verified 
<pre><code>
python main.py $INSERTTWEETFROMIMOGEN bf3c92f97728a4f0875cd837af0851cd340d855346928dc047157a07cf874214 Imogen-Heap/Tiny-Human.mp3

True,True,True,True
</code></pre>

Situation 2, Publisher name matches name found in public tweet, Musicbrainz artist name and fingerprint of song found in artists catalog in Musicbrainz, but Twitter profile is *not* Verified:   
<pre><code>
python main.py 654718134306213889 bf3c92f97728a4f0875cd837af0851cd340d855346928dc047157a07cf874214 Imogen-Heap/Tiny-Human.mp3

True,True,True,False
</code></pre>

Situation 3, Publisher name matches name found in public tweet, but twitter user not "Verified". Fingerprint of song file not found in Musicbrainz database:  
<pre><code>
python main.py 654370721641029632 93b62fc2a8f7cbb5a9e8e08395f88aa71187765d2239aae458d6b923b7a06506 /Users/devon/Desktop/bums/128/01\ DJ\ Day.mp3 
True,True,Notfound,False
</code></pre>



