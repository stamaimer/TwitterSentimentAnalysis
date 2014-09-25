# -*- coding: utf-8 -*-

"""
this code implements a basic twitter-aware preprocesser
"""

import re
import nltk
import tfidf
import codecs
import utilities
import HTMLParser
import mysql.connector

stopwords = nltk.corpus.stopwords.words('english') + ['mh17', 'says', 'url', 'username', u'\u2026', '\'', '&', 'via', 'must', 'may', 'it\'s', 'u', '-', 'another', 'please', 'say', 'many', '9', '6', '4', '3', '2', '1', '+', 'goes', 'i\'m', ':', '.', ',', '17', 'prayformh', '(', ')']

# emotion = [':-)', ':)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}', ':^)', ':っ)',\
# 		   ':-D', ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=-D', '=D', '=-3', '=3', 'B^D',\
# 		   ':-))',\
# 		   '>:[', ':-(', ':(', ':-c', ':c', ':-<', ':っC', ':<', ':-[', ':[', ':{',\	
# 		   ':-||', ':@', '>:(',\
# 		   ':\'-(', ':\'(',\
# 		   ':\'-)', ':\')',\
# 		   'QQ',\
# 		   'D:<', 'D:', 'D8', 'D;', 'D=', 'DX', 'v.v', 'D-\':',\
# 		   ]

punctuation = ['.', '?', '!', ',', ':', '...', ';', '-', '–', '(', ')', '[', ']', '{', '}', '"']

connection = mysql.connector.connect(user = 'root', password = '', host = 'localhost', database = 'twitter')

cursor = connection.cursor()

sql = "SELECT tweet_text FROM tweets"

cursor.execute(sql)

records = cursor.fetchall()

words = ""

parser = HTMLParser.HTMLParser()
tokenizer = utilities.Tokenizer()

file1 = codecs.open('results1', 'w', 'utf-8')

file2 = codecs.open('results2', 'w', 'utf-8')

def preprocess(text):

	text = re.sub(u'[\u2018\u2019]', '\'', text)
	text = re.sub(u'[\u201c\u201d]', '"', text)
	#text = re.sub('\(.*?\)', ' ', text)
	text = re.sub('(^|)?http?s?:?/?/?.*?( |$)', ' ', text)	#deal with url
	text = re.sub('ht?….*$', ' ', text)					#deal with truncated url
	text = re.sub('h…', ' ', text)
	text = parser.unescape(text)						#deal with character entity
	text = re.sub(u'(RT |\\\\|\u201c)"?@.*?[: ]', ' ', text)
	#text = re.sub('RT ', ' ', text)
	text = re.sub('\.?@.*?( |:|$)', 'USERNAME ', text)
	text = re.sub('[][!"#$*/;<=>?@\\\\^_`{|}~]', ' ', text)
	text = re.sub('( - )', ' ', text)
	text = re.sub('---', ' ', text)
	text = re.sub('\.\.\.', ' ', text)
	text = re.sub(u'\u2026', ' ', text)
	text = re.sub('(, |\.( |$))', ' ', text)

	return text

# for record in records:
	
# 	print record[0]
# 	file.write(record[0])
# 	file.write('\r\n')
# 	print preprocess(record[0])
# 	file.write(preprocess(record[0]))
# 	file.write('\r\n')

# for record in records:

# 	words = words + ' ' + preprocess(record[0])

# words = [word.lower() for word in nltk.tokenize.word_tokenize(words)]

# freqdist = nltk.FreqDist(words)

# for item in freqdist.items():

# 	if item[0] not in stopwords:
# 		print item[0]
# 		file1.write(item[0])
# 		file1.write('\t\t')
# 		file1.write(str(item[1]))
# 		file1.write('\r\n')

for record in records:

 	words = words + ' ' + preprocess(record[0])

freqdist = nltk.FreqDist(tokenizer.tokenize(words))

for item in freqdist.items():

 	if item[0] not in stopwords:

 		print item[0]
 		file2.write(item[0])
 		file2.write('\t\t')
		file2.write(str(item[1]))
 		file2.write('\r\n')

def output(tweet):

	text = preprocess(tweet)

	file1.write('******************************************************************')
	file1.write('\r\n')
	file1.write(tweet)
	file1.write('\r\n')
	file1.write('------------------------------------------------------------------')
	file1.write('\r\n')
	file1.write(text)
	file1.write('\r\n')
	file1.write('------------------------------------------------------------------')
	file1.write('\r\n')
	file1.write(' '.join([word.lower() for word in nltk.tokenize.word_tokenize(text)]))
	file1.write('\r\n')
	file1.write(' '.join([word.lower() for word in tokenizer.tokenize(text)]))
	file1.write('\r\n')
	file1.write('\r\n')

	print ('******************************************************************')
	print tweet
	print '------------------------------------------------------------------'
	print text
	print '------------------------------------------------------------------'
	print ' '.join([word.lower() for word in nltk.tokenize.word_tokenize(text)])
	print '------------------------------------------------------------------'
	print ' '.join([word.lower() for word in tokenizer.tokenize(text)])

for record in records:

	output(record[0])

# file1.close()
# file2.close()

	







