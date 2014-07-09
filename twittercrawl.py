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

def to_html_escaped(str):

	if str == None:

		return str

	else:

		tmp = re.sub("\"", "\\\"", str)

		return re.sub("\\", "\\\\", tmp)


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

for line in response.iter_lines():

	if line:

		tweet = json.loads(line)

		t_sql = ("INSERT INTO tweets "\
				 "(tweet_id, tweet_text, tweet_source, tweet_created_time, tweet_retweet_count, tweet_favorite_count) "\
				 "VALUES (%d, \"%s\", \"%s\", \"%s\", %d, %d)" % (tweet["id"],\
																  to_html_escaped(tweet["text"]),\
																  to_html_escaped(tweet["source"]),\
																  to_html_escaped(tweet["created_at"]),\
																  tweet["retweet_count"],\
																  tweet["favorite_count"]))

		print t_sql

		user = tweet["user"]

		u_sql = ("INSERT INTO users "\
				 "(user_id, user_url, user_desc, user_name, user_screen_name, user_lang, user_location, user_time_zone, user_created_time, user_favorites_count, user_statuses_count, user_listed_count, user_friends_count, user_followers_count) "\
				 "VALUES (%d, \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", %d, %d, %d, %d, %d)" % (user["id"],\
																													  to_html_escaped(user["url"]),\
																													  to_html_escaped(user["description"]),\
																													  to_html_escaped(user["name"]),\
																													  to_html_escaped(user["screen_name"]),\
																													  to_html_escaped(user["lang"]),\
																													  to_html_escaped(user["location"]),\
																													  to_html_escaped(user["time_zone"]),\
																													  to_html_escaped(user["created_at"]),\
																													  user["favourites_count"],\
																													  user["statuses_count"],\
																													  user["listed_count"],\
																													  user["friends_count"],\
																													  user["followers_count"]))
		print u_sql

		cursor.execute("set names utf8mb4")

		cursor.execute(t_sql)
		cursor.execute(u_sql)

		connection.commit()

cursor.close()
connection.close()

