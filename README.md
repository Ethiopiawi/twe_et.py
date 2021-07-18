# twe_et.py
Tweet on Twitter without API keys.
import requests
import sys
import time
url = "https://mobile.twitter.com/i/api/graphql/hBV04XE9V0y6Lal1y3fnWQ/CreateTweet"

he = {"authority": "mobile.twitter.com",
"method": "POST",
"authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
"path": "/i/api/graphql/hBV04XE9V0y6Lal1y3fnWQ/CreateTweet",
"scheme": "https",
"accept": "*/*",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-US,en;q=0.9",
"cache-control": "no-cache",
# "content-length": "146",
"content-type": "application/json",
"cookie": """_ga=GA1.2.339678395.1575875973; personalization_id="v1_NyEIZSwcT37qF7Q+iQBTzw=="; guest_id=v1%3A162567935219284615; gt=1416738746792398856; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D; _gid=GA1.2.38886096.1626611598; dnt=1; ads_prefs="HBISAAA="; kdt=woE02LwLRwkfL41ewzb9uf5NNexutVguA2fSdjAD; remember_checked_on=1; _twitter_sess=BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCI%252BRnrl6AToMY3NyZl9p%250AZCIlYWEzZmZhNzNiNzA1NDM3ZGMxNTQ3M2RiMTg1ODJhMWM6B2lkIiVlZGZj%250AM2FiYTBhY2UxNzQzMWJlNmU5ZmY2ZTYyOGUxYToJdXNlcmwrCQKgVg%252FWiZkR--61310ed8c711d0ef4b74f9efb97efa353419d632; auth_token=a7d2bf21d9c13e4f5ac3274fa8cae92f419d0314; twid=u%3D1268196322554847234; ct0=80818e134ad0161d51d509e0bd15b283014607bac3a6e20dea5f2fc10b5b9feae330978132aa7179950bb5eb90be2f16c10f427a8aedd93b676e75792c538a73833765300dd15158c6e4feac5e1db4c6; csrf_id=0202237ff1816334e5a52f04208c2752""",
"origin": "https://mobile.twitter.com",
"pragma": "no-cache",
"referer": "https://mobile.twitter.com/compose/tweet",
"x-csrf-token": "80818e134ad0161d51d509e0bd15b283014607bac3a6e20dea5f2fc10b5b9feae330978132aa7179950bb5eb90be2f16c10f427a8aedd93b676e75792c538a73833765300dd15158c6e4feac5e1db4c6",
"x-twitter-active-user": "yes",
"x-twitter-auth-type": "OAuth2Session",
"x-twitter-client-language": "en",
# "sec-fetch-dest": "document",
# "sec-fetch-mode": "navigate",
# "sec-fetch-site": "same-origin",
# "sec-fetch-user": "?1",
# "upgrade-insecure-requests": "1",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.320"}

tweett = """#AbiyAhmedAli Salvaging Ethiopia from the Monsters Who Used Children As Soldiers. #TPLFisTerrorist"""





n=0
def tweet(n,tweett):
  tweetn = tweett + " | " + f"{n}"
  par = {"variables":{"tweet_text":tweetn,"media":{"media_entities":[],"possibly_sensitive":False},"withReactions":False,"withSuperFollowsTweetFields":False,"semantic_annotation_ids":[],"dark_request":False,"withTweetResult":True,"withBirdwatchPivots":False,"withSuperFollowsUserFields":False},"queryId":"hBV04XE9V0y6Lal1y3fnWQ"}
  print(par)
  for n in range(40,1500):
      tweetn = tweett + " | " + f"{n}"
      par = {"variables":{"tweet_text":tweetn,"media":{"media_entities":[],"possibly_sensitive":False},"withReactions":False,"withSuperFollowsTweetFields":False,"semantic_annotation_ids":[],"dark_request":False,"withTweetResult":True,"withBirdwatchPivots":False,"withSuperFollowsUserFields":False},"queryId":"hBV04XE9V0y6Lal1y3fnWQ"}
      print(par)
      rsp = requests.post(url = url, headers=he, json=par)
      print(rsp.content)
      time.sleep(3)

tweet(0,tweett)
