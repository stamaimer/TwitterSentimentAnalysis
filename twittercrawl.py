import os
import re
import hmac
import json
import time
import base64
import urllib
import hashlib
import pymongo
import binascii
import requests

url = "https://stream.twitter.com/1.1/statuses/sample.json"

payloads = {"stall_warnings" : "true", "language" : "en"}

CONSUMER_SECRET = "oFAlNZr6JGHwCdYGrYNfS3plUSdxg8UlEP2RtiKg59uSYahWRk"
TOKEN_SECRET    = "rVX3YRtx2Qa5rO9PPqtWP1Fu3HHTK70EuSmBtJXmW7KjE"

secrets = {"consumer_secret" : CONSUMER_SECRET, "token_secret" : TOKEN_SECRET}

signkey = '&'.join(secrets.values())

OAUTH_SIGNATURE_METHOD = "HMAC-SHA1"
OAUTH_CONSUMER_KEY     = "6s35FXsv4jD2ar0ZlDYjnt7jZ"
OAUTH_VERSION          = "1.0"
OAUTH_TOKEN 	       = "1112070588-5bNvcWYSIowvzRbRnSp4jetaCbpLk0xNVFg8egv"

def urlencode(str):

	return urllib.quote(str, '')

def timestamp():

	return str(int(time.time()))

def gen_nonce():

	return re.sub('[\W_]', '', base64.b64encode(os.urandom(32)))

oauth_timestamp = timestamp()
oauth_nonce 	= gen_nonce()

parameters = {
                "oauth_signature_method" : OAUTH_SIGNATURE_METHOD, 
		"oauth_consumer_key"     : OAUTH_CONSUMER_KEY, 
		"oauth_timestamp" 	 : oauth_timestamp, 
		"oauth_version" 	 : OAUTH_VERSION, 
		"oauth_token" 		 : OAUTH_TOKEN, 
		"oauth_nonce"		 : oauth_nonce
	     }

parameters.update(payloads)

parastr = ""

for key in sorted(parameters):

	parastr = parastr + urlencode(key) + "=" + urlencode(parameters[key]) + "&"

parastr = parastr[:-1]

basestr = "GET&" + urlencode(url) + "&" + urlencode(parastr)

digest = hmac.new(signkey, basestr, hashlib.sha1).digest()

oauth_signature = binascii.b2a_base64(digest)[:-1]

authorization = "OAuth "\
		+ "oauth_signature_method=\"" + urlencode(parameters["oauth_signature_method"]) + "\", "\
		+ "oauth_consumer_key=\""     + urlencode(parameters["oauth_consumer_key"]) 	+ "\", "\
		+ "oauth_timestamp=\"" 	      + urlencode(parameters["oauth_timestamp"]) 	+ "\", "\
		+ "oauth_signature=\"" 	      + urlencode(oauth_signature) 			+ "\", "\
		+ "oauth_version=\"" 	      + urlencode(parameters["oauth_version"]) 		+ "\", "\
		+ "oauth_nonce=\"" 	      + urlencode(parameters["oauth_nonce"]) 		+ "\", "\
		+ "oauth_token=\"" 	      + urlencode(parameters["oauth_token"]) 		+ "\""

headers = {"authorization" : authorization}

response = requests.get(url, params = payloads, headers = headers, stream = True)

print response.status_code

mongo_client = pymongo.MongoClient('127.0.0.1', 27017)

twitter = mongo_client.twitter

tweets = twitter.tweets

users  = twitter.users

for line in response.iter_lines():

	if line:

		print line

		tweet = json.loads(line)

		user = tweet["user"]

		print "tweet_id : ", tweets.insert(tweet)

		print "user_id : ", users.insert(user)



