import sys
import pymongo
import mysql.connector

mysql_connection = mysql.connector.connect(user = "root",
                                           password = "",
                                           host = "127.0.0.1",
                                           database = "twitter"
                                          )

mysql_cursor = mysql_connection.cursor()

sql = "SELECT tweet_text FROM tweets LIMIT 0, %s" % sys.argv[1]

print sql

mysql_cursor.execute(sql)

results = mysql_cursor.fetchall()

for tweet in results:

    if u'' in tweet:

        print tweet

#mongo_client = pymongo.MongoClient("127.0.0.1", 27017)

#twitter = mongo_client.twitter

#tweets = twitter.tweets

#for tweet in tweets.find():

#    if u'\u2764' in tweet["text"]:

#        print tweet["text"]
