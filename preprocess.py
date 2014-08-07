import re
import sys
import nltk
import twitter_text
import mysql.connector
from twitter_text import TwitterText
from nltk.stem.wordnet import WordNetLemmatizer

stopwords = nltk.corpus.stopwords.words('english') + ['-']	#

def connectsql():
	
	connection = mysql.connector.connect(user = 'root',
										 password = '',
										 host = '127.0.0.1',
										 database = 'twitter')

	return connection

def pre_process(text):
	
	extractor = TwitterText(text).extractor

	for ele in extractor.extract_urls_with_indices():

		text = re.sub(ele['url'], '', text)

	text += ' '

	text = re.sub('RT', ' ', text)

	text = re.sub('&amp;', ' ', text)

	text = re.sub('@.*?[: ]', ' ', text)

	text = re.sub('[][#|.,!/?*_+"]', ' ', text)

	return text

def del_stopwords(terms):
	
	for term in terms:

		if term in stopwords:

			terms.remove(term)

	return terms

def lemmatize(terms):

	lmtzr = WordNetLemmatizer()
	
	for i in range(len(terms)):

		terms[i] = lmtzr.lemmatize(terms[i])

	return terms

connection = connectsql()

cursor = connection.cursor()

sql = "SELECT tweet_id, tweet_text FROM tweets"

cursor.execute(sql)

results = cursor.fetchall()

for(id, text) in results:

	# print text

	text = pre_process(text)

	# print text

	terms = [term for term in text.split()]

	# print terms

	# bigrams = nltk.bigrams(text.split())

	# print bigrams

	terms = del_stopwords(terms)

	# print terms

	terms = lemmatize(terms)

	keywords  = tfidf.gen_keywords(' '.join(terms), './corpus', 5)

	print keywords

	sql = "UPDATE tweets SET tweet_pre_process_result = \"%s\" WHERE tweet_id = %d" % (' '.join(keywords), id)

	cursor.execute(sql)





	

