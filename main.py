#Import libs
import acoustid,sys,requests,json,tweepy
#Variables that contains the user credentials to access Twitter API
access_token = "6661012-wKLHzit2xUDbMGlF0i7LzQXPcpDDmKA1Zp3mjl0Qfx"
access_token_secret = "Cj5qqv5ysn8Siec8BZ0D3SNKolz8Yr3IoCSAPKtkj0AGj"
consumer_key = "pvVMheQrbLpVf5S0ZFB2kDFfh"
consumer_secret = "6HwpjVBGCGO0TrQ4GrsMc4FbbVnS7wmLcKwGQbZp9aAPvH0Zzp"
#retrive txid from api
def findtxid(txid):
    url = 'http://libraryd.alexandria.media/alexandria/v1/search'
    payload = {
      "protocol":"publisher",
      "search-on":"txid",
      "search-for":txid
    }

    # GET
    r = requests.get(url)

    # GET with params in URL
    r = requests.get(url, params=payload)

    # POST with form-encoded data
    r = requests.post(url, data=payload)

    # POST with JSON
    r = requests.post(url, data=json.dumps(payload))

    # Response, status etc
    return([json.loads(r.text),r.status_code])
#function that verifies song against tweet and txid
def verify_song(tweetid,txid,song):
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        tweet = api.get_status(sys.argv[1])
        if txid in tweet.text:
            if findtxid(txid)[0]["response"][0]["publisher-data"]["alexandria-publisher"]["name"].lower() in tweet.text.lower():
                if 0==sum(1 for x in acoustid.match("Hcspu7zG",song)):
                    print '{"authdata":[{"foundtxid":"True"},{"foundname":"False"},{"verified":"'+str(tweet.user.verified)+'"},{"songmatch":"NotFound"}]}'
                else:
                    for score, recording_id, title, artist in acoustid.match("Hcspu7zG",song):
                        if artist.decode("utf-8").lower() in tweet.text.lower():
                            print '{"authdata":[{"foundtxid":"True"},{"foundname":"True"},{"verified":"'+str(tweet.user.verified)+'"},{"songmatch":"True"}]}'
                            break
                        else:
                            print '{"authdata":[{"foundtxid":"True"},{"foundname":"True"},{"verified":"'+str(tweet.user.verified)+'"},{"songmatch:"False"}]}'
                            break
            else:
                print '{"authdata":[{"foundtxid":"True"},{"foundname":"False"},{"verified":"'+str(tweet.user.verified)+'"},{"songfound":"False"}]}'
        else:
            print '{"authdata":[{"foundtxid":"False"},{"foundname":"False"},{"verified":"'+str(tweet.user.verified)+'"},{"songfound":"False"}]}'

    except Exception,e1:
        print e1


#function that checks txid in tweet
def verify_tweet(tweetid,txid):
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        tweet = api.get_status(sys.argv[1])
        if txid in tweet.text:
            if findtxid(txid)[0]["response"][0]["publisher-data"]["alexandria-publisher"]["name"].lower() in tweet.text.lower():
                print '{"authdata":[{"foundtxid":"True"},{"foundname":"True"},{"verified":"'+str(tweet.user.verified)+'"}]}'
                return 0
            else:
                print '{"authdata":[{"foundtxid":"True"},{"foundname":"False"},{"verified":"'+str(tweet.user.verified)+'"}]}'
                return 0
        print '{"authdata":[{"foundtxid":"False"},{"foundname":"False"},{"verified":"'+str(tweet.user.verified)+'"}]}'
    except Exception,e0:
        print e0

#handle arguments
if __name__ == "__main__":
    if len(sys.argv) == 3:
        verify_tweet(sys.argv[1],sys.argv[2])
    if len(sys.argv) == 4:
        verify_song(sys.argv[1],sys.argv[2],sys.argv[3])
    if len(sys.argv) == 1 or len(sys.argv)>4:
        print >>sys.stderr, "Usage: %s <tweet id> <txid> <audio file(optional)>" % sys.argv[0]
