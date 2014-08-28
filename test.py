import mysql.connector
import twitter_text
import utilities
import codecs
import nltk
import re

def pre_process(text):

	extractor = twitter_text.TwitterText(text).extractor

	for ele in extractor.extract_urls_with_indices():

		text = re.sub(ele['url'], '', text)

	text += ''

	text = re.sub('RT', ' ', text)
	text = re.sub('@.*?[: $]', ' ', text)

	return text

def connectsql():
	
	connection = mysql.connector.connect(user = "root", password = "", host = "localhost", database = "twitter")

	return connection

connection = connectsql()

cursor = connection.cursor()

sql = "SELECT tweet_text FROM tweets"

cursor.execute(sql)

records = cursor.fetchall()

file = codecs.open('preprocessed', 'w', 'utf-8')

#tokenizer = utilities.Tokenizer()

for record in records:
	
#	print record[0]
	
	file.write(record[0])

	file.write('\r\n')

	text = pre_process(record[0])
	
	file.write(text)

	file.write('\r\n')

#	print '\r\n'.join(tokenizer.tokenize(text))

#	print '====================================================='

#	print '\r\n'.join(nltk.tokenize.word_tokenize(text))

#	print '====================================================='

file.close()
	
