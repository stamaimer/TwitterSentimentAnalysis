import nltk
import collections
import mysql.connector

def myround(var):
	
	return round(var, 2) if var != None else None

def connectsql():
	
	connection = mysql.connector.connect(user = "root",
										 password = "",
										 host = "localhost",
										 database = "twitter")

	return connection

connection = connectsql()

cursor = connection.cursor()

sql = "SELECT tweet_pre_process_result, tweet_classification FROM tweets LIMIT 0, 2400"

cursor.execute(sql)

records = cursor.fetchall()

trainsets = [({'preprocessed':preprocessed}, classification) for (preprocessed, classification) in records]

classifier = nltk.NaiveBayesClassifier.train(trainsets)

for i in range(6):

	sql = "SELECT tweet_pre_process_result, tweet_classification FROM tweets LIMIT %d, %d" % (400 * i, 400 * (i + 1))

	cursor.execute(sql)

	records = cursor.fetchall()

	testsets = [({'preprocessed':preprocessed}, classification) for (preprocessed, classification) in records]

	rset = collections.defaultdict(set)
	tset = collections.defaultdict(set)

	for n, (feature, classification) in enumerate(testsets):

		rset[classification].add(n)

		temp = classifier.classify(feature)

		tset[temp].add(n)

	print nltk.classify.accuracy(classifier, testsets)

	print "precision of 0 : ", myround(nltk.metrics.precision(rset[0], tset[0])), "\trecall of 0 : ", myround(nltk.metrics.recall(rset[0], tset[0])), "\tf_measure of 0 : ", myround(nltk.metrics.f_measure(rset[0], tset[0]))
	print "precision of 1 : ", myround(nltk.metrics.precision(rset[1], tset[1])), "\trecall of 1 : ", myround(nltk.metrics.recall(rset[1], tset[1])), "\tf_measure of 1 : ", myround(nltk.metrics.f_measure(rset[1], tset[1]))
	print "precision of 2 : ", myround(nltk.metrics.precision(rset[2], tset[2])), "\trecall of 2 : ", myround(nltk.metrics.recall(rset[2], tset[2])), "\tf_measure of 2 : ", myround(nltk.metrics.f_measure(rset[2], tset[2]))
	print "precision of 3 : ", myround(nltk.metrics.precision(rset[3], tset[3])), "\trecall of 3 : ", myround(nltk.metrics.recall(rset[3], tset[3])), "\tf_measure of 3 : ", myround(nltk.metrics.f_measure(rset[3], tset[3]))
	print "precision of 4 : ", myround(nltk.metrics.precision(rset[4], tset[4])), "\trecall of 4 : ", myround(nltk.metrics.recall(rset[4], tset[4])), "\tf_measure of 4 : ", myround(nltk.metrics.f_measure(rset[4], tset[4]))
	print "precision of 5 : ", myround(nltk.metrics.precision(rset[5], tset[5])), "\trecall of 5 : ", myround(nltk.metrics.recall(rset[5], tset[5])), "\tf_measure of 5 : ", myround(nltk.metrics.f_measure(rset[5], tset[5]))
	print "precision of 6 : ", myround(nltk.metrics.precision(rset[6], tset[6])), "\trecall of 6 : ", myround(nltk.metrics.recall(rset[6], tset[6])), "\tf_measure of 6 : ", myround(nltk.metrics.f_measure(rset[6], tset[6]))

	print "\n======================================================================\n"

	# print classifier.show_most_informative_features(5)