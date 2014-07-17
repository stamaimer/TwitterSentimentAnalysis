import nltk
import twitter_text
import mysql.connector
from twitter_text import TwitterText

def connectsql():
	
	connection = mysql.connector.connect(user = 'root',
										 password = '',
										 host = '127.0.0.1',
										 database = 'twitter')

	return connection

connection = connectsql()

cursor = connection.cursor()

sql = "SELECT tweet_id, tweet_text FROM tweets WHERE tweet_id = 486789001287045120"

cursor.execute(sql)

for(id, text) in cursor:

	extractor = TwitterText(text).extractor

	for ele in extractor.extract_urls_with_indices():

		

	


