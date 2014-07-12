import sys
import json
import nltk
import numpy
import tfidf

N = 100 				# number of words yto consider
CLUSTER_THRESHOLD = 5 	# distance between words to considers

# approach taken from "The Automatic Creation of Literature Abstracts" by H.P. Luhn

def placeholder(sentences, keywords):

	scores = []

	sent_idx = -1

	for sentence in [nltk.tokenize.word_tokenize(sentence) for sentence in sentences]:

		sent_idx += 1

		word_idx = []

		for word in keywords:

			try:

				word_idx.append(sentence.index(word))

			except ValueError, e:
				
				pass

		word_idx.sort()
		
		if 0 == len(word_idx): continue

		 

def summarize(text, path2corpus):
	
	keywords  = tfidf.gen_keywords(text, path2corpus, N)

	sentences = [sentence.lower() for sentence in nltk.tokenize.sent_tokenize(text)]

	sentences = placeholder(sentences, keywords)

