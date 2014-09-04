# -*- coding: utf-8 -*-

import mysql.connector
import preprocessim
import collections
import utilities
import nltk

def myround(var):
	
	return round(var, 2) if var != None else None

def connectsql():
	
	connection = mysql.connector.connect(user = "root",
										 password = "",
										 host = "127.0.0.1",
										 database = "twitter")

	return connection

connection = connectsql()

cursor = connection.cursor()

sql = "SELECT tweet_text, tweet_classification FROM tweets LIMIT 0, 2400"

cursor.execute(sql)

records = cursor.fetchall()

tokenizer = utilities.Tokenizer()

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
													  '-including', '20th', '3rd', '9m-mrd', 'a', 'aa', 'ai113', 'al-f…', 'aust', 'aw', 'ac360'] + ['mh17', 'says', 'url', 'username', u'\u2026', '\'', '&', 'via', 'must', 'may', 'it\'s', 'u', '-', 'another', 'please', 'say', 'many', '9', '6', '4', '3', '2', '1', '+', 'goes', 'i\'m', ':', '.', ',', '17', 'prayformh', 'news', 'gaza', 'mh370', 'people', 'black', 'us', 'world', 'flight', 'airlines', 'passengers', 'plane', 'families', 'aids', 'lost', 'crew', 'one', 'train', 'air', '']

for record in records:

	print preprocessim.preprocess(record[0])

	words = words + preprocessim.preprocess(record[0])

words = [word for word in tokenizer.tokenize(words)]

freqdist = nltk.FreqDist(words)

for item in freqdist.items():

	if (item[0] in stopwords) or (item[1] < 60):

		freqdist.pop(item[0])

featvects = [None for _ in range(2400)]

for i in range(2400):

	featvect = [0 for _ in range(len(freqdist))]

	words = [word for word in tokenizer.tokenize(preprocessim.preprocess(records[i][0]))]

	for j in range(len(freqdist)):

		if freqdist.keys()[j] in words:

			featvect[j] = 1

	featvects[i] = featvect

for i in range(6):

	sets = [None for _ in range(2400)]

	for j in range(2400):

		sets[j] = ({'featvect':tuple(featvects[j])}, records[j][1])

	print "length of tweets : ", len(sets)

	print "range of testset : ", 400 * i, 400 * (i + 1)

	testset = sets[400 * i : 400 * (i + 1)]

	del sets[400 * i : 400 * (i + 1)]

	trainset = sets

	classifier = nltk.NaiveBayesClassifier.train(trainset)

	rset = collections.defaultdict(set)
	tset = collections.defaultdict(set)
	
	for n, (feature, classification) in enumerate(testset):

			rset[classification].add(n)

			temp = classifier.classify(feature)

			tset[temp].add(n)

	print "accuracy of classifier : ", myround(nltk.classify.accuracy(classifier, testset)), "\n"

	print "precision of 0 : ", myround(nltk.metrics.precision(rset[0], tset[0])), "\trecall of 0 : ", myround(nltk.metrics.recall(rset[0], tset[0])), "\tf_measure of 0 : ", myround(nltk.metrics.f_measure(rset[0], tset[0]))
	print "precision of 1 : ", myround(nltk.metrics.precision(rset[1], tset[1])), "\trecall of 1 : ", myround(nltk.metrics.recall(rset[1], tset[1])), "\tf_measure of 1 : ", myround(nltk.metrics.f_measure(rset[1], tset[1]))
	print "precision of 2 : ", myround(nltk.metrics.precision(rset[2], tset[2])), "\trecall of 2 : ", myround(nltk.metrics.recall(rset[2], tset[2])), "\tf_measure of 2 : ", myround(nltk.metrics.f_measure(rset[2], tset[2]))
	print "precision of 3 : ", myround(nltk.metrics.precision(rset[3], tset[3])), "\trecall of 3 : ", myround(nltk.metrics.recall(rset[3], tset[3])), "\tf_measure of 3 : ", myround(nltk.metrics.f_measure(rset[3], tset[3]))
	print "precision of 4 : ", myround(nltk.metrics.precision(rset[4], tset[4])), "\trecall of 4 : ", myround(nltk.metrics.recall(rset[4], tset[4])), "\tf_measure of 4 : ", myround(nltk.metrics.f_measure(rset[4], tset[4]))
	print "precision of 5 : ", myround(nltk.metrics.precision(rset[5], tset[5])), "\trecall of 5 : ", myround(nltk.metrics.recall(rset[5], tset[5])), "\tf_measure of 5 : ", myround(nltk.metrics.f_measure(rset[5], tset[5]))
	print "precision of 6 : ", myround(nltk.metrics.precision(rset[6], tset[6])), "\trecall of 6 : ", myround(nltk.metrics.recall(rset[6], tset[6])), "\tf_measure of 6 : ", myround(nltk.metrics.f_measure(rset[6], tset[6]))

	print "\n======================================================================\n"

























