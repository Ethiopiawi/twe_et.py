import requests


url = "https://mobile.twitter.com/i/api/1.1/statuses/update.json"

he = {"authority": "mobile.twitter.com",
"method": "POST",
"authorization": "FILL THE AUTHORAIZATION BEARER HERE",
"path": "/i/api/1.1/statuses/update.json",
"scheme": "https",
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-US,en;q=0.9",
"cache-control": "no-cache",
# "content-length": "146",
"content-type": "application/x-www-form-urlencoded",
"cookie": """HERE GOES YOUR COOKIE""",
"origin": "https://mobile.twitter.com",
"pragma": "no-cache",
"referer": "https://mobile.twitter.com/compose/tweet",
"x-csrf-token": "THE CSRF TOKEN",
"x-twitter-active-user": "yes",
"x-twitter-auth-type": "OAuth2Session",
"x-twitter-client-language": "en",
# "sec-fetch-dest": "document",
# "sec-fetch-mode": "navigate",
# "sec-fetch-site": "same-origin",
# "sec-fetch-user": "?1",
# "upgrade-insecure-requests": "1",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.320"}

tweet = """Your Tweet text goes here"""

par = {'include_profile_interstitial_type': '1',
'include_blocking': '1',
'include_blocked_by': '1',
'include_followed_by': '1',
'include_want_retweets': '1',
'include_mute_edge': '1',
'include_can_dm': '1',
'include_can_media_tag': '1',
'skip_status': '1',
'cards_platform': 'Web-12',
'include_cards': '1',
'include_ext_alt_text': 'true',
'include_quote_count': 'true',
'include_reply_count': '1',
'tweet_mode': 'extended',
'simple_quoted_tweet': 'true',
'trim_user': 'false',
'include_ext_media_color': 'true',
'include_ext_media_availability': 'true',
'auto_populate_reply_metadata': 'true',
'batch_mode': 'off',
#'in_reply_to_status_id': 'status id for reply', ---- If you are replying to some body
'status': "This is where the tweet goes."}




def tweet()
	par['status'] = tweet #This sets the text to be tweeted to the one stated in the tweet variable
	rsp = requests.post(url = url, headers=he, params=par)
	print(rsp)


if __name__ == "__main__":
	tweet()
