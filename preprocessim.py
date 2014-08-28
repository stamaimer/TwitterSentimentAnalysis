# -*- coding: utf-8 -*-

"""
this code implements a basic twitter-aware preprocesser
"""

import re
import nltk
import tfidf
import codecs
import HTMLParser
import mysql.connector

stopwords = nltk.corpus.stopwords.words('english')

punctuation = ['.', '?', '!', ',', ':', '...', ';', '-', '–', '(', ')', '[', ']', '{', '}', '"']

connection = mysql.connector.connect(user = 'root', password = '', host = 'localhost', database = 'twitter')

cursor = connection.cursor()

sql = "SELECT tweet_text FROM tweets LIMIT 0, 2500"

cursor.execute(sql)

records = cursor.fetchall()

parser = HTMLParser.HTMLParser()

file = codecs.open('results', 'w', 'utf-8')

def preprocess(text):

	text = re.sub('http?s?:?/?/?.*?( |$)', ' ', text)	#deal with url
	text = re.sub('ht?….*$', ' ', text)					#deal with truncated url
	text = parser.unescape(text)						#deal with character entity
	text = re.sub('RT @.*?[:| ]', ' ', text)
	text = re.sub('RT ', ' ', text)
	text = re.sub('@.*?[ |:]', 'USERNAME ', text)
	text = re.sub('[][!"#$%*,./;<=>?@\^_`{|}~-]', '', text)

	return text

for record in records:
	
	# print record[0]
	file.write(record[0])
	file.write('\r\n')
	print preprocess(record[0])
	file.write(preprocess(record[0]))
	file.write('\r\n')



