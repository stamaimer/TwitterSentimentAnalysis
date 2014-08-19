import mysql.connector
import codecs

connection = mysql.connector.connect(user = "root",
										 password = "",
										 host = "127.0.0.1",
										 database = "twitter")

cursor = connection.cursor()

sql = "SELECT id FROM tweets LIMIT 0, 2500"

cursor.execute(sql)

results = cursor.fetchall()

i = 0

for tid in results:

	sql = "UPDATE tweets SET id = %d WHERE id = %d" % (i, tid[0])

	print sql

	cursor.execute(sql)

	connection.commit();

	i = i + 1

# file = codecs.open('./output.bk', 'r', 'utf-8')

# for line in file:

# 	sql = "UPDATE tweets SET tweet_pre_process_result = \"%s\" WHERE "

