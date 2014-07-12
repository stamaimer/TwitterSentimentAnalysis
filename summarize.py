import sys
import json
import nltk
import numpy
import tfidf

#
CLUSTER_THRESHOLD = 5 #distance between words to consider
#

def summarize(text):
	
	keywords = tfidf.gen_keywords(text)

