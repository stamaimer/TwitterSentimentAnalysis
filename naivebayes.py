import nltk
import mysql.connector

def connectsql():
	
	connection = mysql.connector.connect(user = "root",
										 password = "",
										 host = "localhost",
										 database = "twitter")

	return connection

connection = connectsql()

cursor = connection.cursor()

sql = "SELECT tweet_pre_process_result, tweet_classification FROM test LIMIT 0, 2000"

cursor.execute(sql)

records = cursor.fetchall()

# print records
 
# for (text, preprocessed, classification) in records:

# 	print text, preprocessed, classification, '\n'

trainsets = [({'preprocessed':preprocessed}, classification) for (preprocessed, classification) in records]

# for record in testsets:

# 	print record

classifier = nltk.NaiveBayesClassifier.train(trainsets)

sql = "SELECT tweet_text, tweet_pre_process_result FROM test LIMIT 0,100"

cursor.execute(sql)

records = cursor.fetchall()

for (text, preprocessed) in records:

	print text, classifier.classify({'preprocessed':preprocessed})

testsets = [({'preprocessed':preprocessed}, classification) for (preprocessed, classification) in records]

print nltk.classify.accuracy(classifier, testsets)

print classifier.show_most_informative_features(5)