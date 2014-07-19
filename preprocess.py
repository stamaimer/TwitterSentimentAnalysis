import re
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

sql = "SELECT tweet_id, tweet_text FROM tweets"

cursor.execute(sql)

for(id, text) in cursor:

	print text

	extractor = TwitterText(text).extractor

	for ele in extractor.extract_urls_with_indices():

		text = re.sub(ele['url'], '', text)

	text += ' '

	text = re.sub('RT', ' ', text)

	text = re.sub('&amp;', ' ', text)

	text = re.sub('@.*?[: ]', ' ', text)

	text = re.sub('[][#|.,!/?"]', ' ', text)

	print text