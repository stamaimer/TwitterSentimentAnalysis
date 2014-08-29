import re
import codecs

file = codecs.open(argv[1], 'r', 'utf-8')

def preprocess(regex, replace, text):
	
	text = re.sub(regex, replace, text)

	return text

for line in file:

	print preprocess(argv[2], argv[3], line)

file.close()

