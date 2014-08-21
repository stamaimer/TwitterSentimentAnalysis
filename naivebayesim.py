# -*- coding: utf-8 -*-

import mysql.connector
import nltk

def connectsql():
	
	connection = mysql.connector.connect(user = "root",
										 password = "",
										 host = "127.0.0.1",
										 database = "twitter")

	return connection

connection = connectsql()

cursor = connection.cursor()

sql = "SELECT tweet_pre_process_result, tweet_classification FROM tweets LIMIT 0, 2500"

cursor.execute(sql)

records = cursor.fetchall()

words = ""

stopwords = nltk.corpus.stopwords.words('english') + ['mh17', '…', 'http', 'n\'t', ':', 't…', 'and…', '”', '“', 'c…',\
													  'u', 'wa', 'htt…', '\'m', 'h…', 'p…', '—', '\'ll', 'http…', 'let’s',\
													  '➽', 'com', 'we', 'gt', 'le', '\'ve', 'fo…', 'treatmen…', '–', 'mt',\
													  'blowjob', 'don’t', 'families…', 'fb', 'fm', 'hd', 'her…', 'if', 'igor',\
													  '✈️', '\'deep', 'a…', 'had', 'internat\'l', 'm…', 'nex…', 'w', '✈', '✈️✈️',\
													  'al', 'in…', 'ipped', 'mp', 'qld', 'razak', 'today9', '»', '\'we', 'nz',\
													  'abt', 'from', 'his', 'it\'s', 'let', 'lets', 'maddow', 'mal…', 'month',\
													  'many', 'malaysianplanecras…', 'mh', 'mom', 'out…', 'ppl', 'tony', 'ya',\
													  'weren’t', 'vid', '’', '⏩', '➡️⬅️', 'astroawani', 'borodai', 'cant', 'eu',\
													  'mccully', 'mejorvestido', 'nra', 'nsw', 'nz', 'o', 'o\'reilly', 'r', 'sa-11',\
													  'incl', 'inna', 'int\'l', 'jazakallah', 'jaya', 'kiki', 'kunfayakun', 'malaysi…',\
													  '\'excuse', '\'little', '\'no', '\'prime', '\'rather', '\'shot', '\'talk', '\'wash',\
													  'spreadytweetz', 'surface-…', '“we', '•', '►', '➡⬅', '\'d', '\'did', '\'everything',\
													  '-including', '20th', '3rd', '9m-mrd', 'a', 'aa', 'ai113', 'al-f…', 'aust', 'aw', '']

for record in records:

	words = words + record[0].encode('utf-8')

words = [word.lower() for word in nltk.tokenize.word_tokenize(words)]

freqdist = nltk.FreqDist(words)

print type(freqdist)

for key in freqdist.keys():

	print key, '\t', freqdist[key]

	if freqdist[key] < 10:

		del freqdist[key]

		print 'del because frep'

	elif key in stopwords:

		del freqdist[key]

		print 'del because stop'
























