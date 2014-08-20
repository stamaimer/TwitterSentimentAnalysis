import mysql.connector
import codecs

connection = mysql.connector.connect(user = "root",
										 password = "",
										 host = "127.0.0.1",
										 database = "twitter")

cursor = connection.cursor()

file = codecs.open('./output', 'r', 'utf-8')

i = 0

for line in file:

 	sql = "UPDATE tweets SET tweet_pre_process_result = \"%s\" WHERE id = %d" % (line, i)

 	print sql

 	cursor.execute(sql)

 	connection.commit()

 	i = i + 1
