import os
import re
import time
import json
import hmac
import urllib
import base64
import hashlib
import binascii
import requests
import mysql.connector

def connectsql():
	
	connection = mysql.connector.connect(user = "root",
										 password = "",
										 host = "127.0.0.1",
										 database = "twitter")

	return connection

def urlencode(str):
	return urllib.quote(str, '')

def timestamp():
	return str(int(time.time()))

def gen_nonce():
	return re.sub('[\W_]', '', 	base64.b64encode(os.urandom(32)))

#url = "https://stream.twitter.com/1.1/statuses/filter.json"
url = "https://stream.twitter.com/1.1/statuses/sample.json"
#url = "https://stream.twitter.com/1.1/statuses/firehose.json"

#keyword  = "Confucius Institute"

secrets = {\
		   "consumer_secret":"oFAlNZr6JGHwCdYGrYNfS3plUSdxg8UlEP2RtiKg59uSYahWRk",\
		   "token_secret":"rVX3YRtx2Qa5rO9PPqtWP1Fu3HHTK70EuSmBtJXmW7KjE"\
		  }

signkey = '&'.join(secrets.values())

oauth_timestamp = timestamp()
oauth_nonce 	= gen_nonce()

params = {\
		  "oauth_signature_method":"HMAC-SHA1",\
		  "oauth_consumer_key":"6s35FXsv4jD2ar0ZlDYjnt7jZ",\
		  "oauth_timestamp":oauth_timestamp,\
		  "oauth_version":"1.0",\
		  "oauth_token":"1112070588-5bNvcWYSIowvzRbRnSp4jetaCbpLk0xNVFg8egv",\
		  "oauth_nonce":oauth_nonce\
		 }

#payloads = {"track":keyword}
#payloads = {"delimited":"length"}
payloads = {"language":"en"}

paramstr = ""

params.update(payloads)

for key in sorted(params):
	paramstr = paramstr + urlencode(key) + "=" + urlencode(params[key]) + "&"

paramstr = paramstr[:-1]

#basestr = "POST&" + urlencode(url) + "&" + urlencode(paramstr)
basestr = "GET&" + urlencode(url) + "&" + urlencode(paramstr)

digest = hmac.new(signkey, basestr, hashlib.sha1).digest()

oauth_signature = binascii.b2a_base64(digest)[:-1]

authorization = "OAuth "\
				+ "oauth_consumer_key=\"" + urlencode(params["oauth_consumer_key"]) + "\", "\
				+ "oauth_nonce=\"" + urlencode(params["oauth_nonce"]) + "\", "\
				+ "oauth_signature=\"" + urlencode(oauth_signature) + "\", "\
				+ "oauth_signature_method=\"" + urlencode(params["oauth_signature_method"]) + "\", "\
				+ "oauth_timestamp=\"" + urlencode(params["oauth_timestamp"]) + "\", "\
				+ "oauth_token=\"" + urlencode(params["oauth_token"]) + "\", "\
				+ "oauth_version=\"" + urlencode(params["oauth_version"]) + "\""

headers = {"authorization":authorization}

#response = requests.post(url, data = payloads, headers = headers, stream = True)
response = requests.get(url, params = payloads, headers = headers, stream = True)
#response = requests.get(url, headers=headers, stream=True)
print response.url
print response.status_code

connection = connectsql()

cursor = connection.cursor()

t_sql = ("INSERT INTO tweets VALUES (%d, %s, %s, %s, %d, %d)")
u_sql = ("INSERT INTO users VALUES (%d, %s, %s, %s, %s, %s, %s, %s, %s, %d, %d, %d, %d, %d)")

for line in response.iter_lines():

	if line:

		tweet = json.loads(line)

		t_fields = (tweet["id"],\
					tweet["text"],\
					tweet["source"],\
					tweet["created_at"],\
					tweet["retweet_count"],\
					tweet["favorite_count"])

		user = tweet["user"]

		u_fields = (user["id"],\
					user["url"],\
					user["description"],\
					user["name"],\
					user["screen_name"],\
					user["lang"],\
					user["location"],\
					user["time_zone"],\
					user["created_at"],\
					user["favourites_count"],\
					user["statuses_count"],\
					user["listed_count"],\
					user["friends_count"],\
					user["followers_count"])

		cursor.execute(t_sql, t_fields)
		cursor.execute(u_sql, u_fields)

		connection.commit()

cursor.close()
connection.close()

