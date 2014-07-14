from __future__ import division
import re
import os
import sys
import math
import nltk

stopwords = nltk.corpus.stopwords.words('english') + ['.', ',', '?', '(', ')', ':', '"', '-', '{', '}', '\'',	'--', '\'s', '\'re']

pos = ('JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS', 'RB', 'RBR', 'RBS', 'RP', 'SYM', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ')

def prepare(path2corpus):
	
	files = os.listdir(path2corpus)

	filelists = []

	for file in files:

		filelist = [term.lower() for term in open(('/').join([path2corpus, file]), 'r').read(-1).split()]

		filelists.append(nltk.Text(filelist))

	return filelists

def cal_term_freq(text):

	sentences = nltk.tokenize.sent_tokenize(text)

	terms    = [term.lower() for sentence in sentences for term in nltk.tokenize.word_tokenize(sentence)]

	length   = len(terms)

	freqdist = nltk.FreqDist(terms)

	for key in freqdist.keys():

		if key in stopwords:						#del stop words
			
			del freqdist[key]

		else:

			freqdist[key] = freqdist[key] / length

	return freqdist

def cal_idoc_freq(dist2cal, path2corpus):

	filelists = prepare(path2corpus)

	for key in dist2cal.keys():

		count = 0

		for filelist in filelists:								#speed up

			if filelist.count(key) != 0:
				
				count = count + 1

		dist2cal[key] = math.log10(len(filelists) / (count + 1))

	return dist2cal

def gen_keywords(text, path2corpus, n):
	
	term_freq = cal_term_freq(text)

	idoc_freq = cal_idoc_freq(term_freq, path2corpus)

	tfidf = {}

	for key in term_freq.keys():

		tfidf[key] = term_freq[key] * idoc_freq[key]

	tmp = sorted(tfidf, key = tfidf.get)				#sort by tfidf

	tmp = [[term] for term in tmp]						#pre-process

	tmp = [nltk.pos_tag(term) for term in tmp]			#tegged

	keywords = []

	for term in tmp:

		if term[0][1] in pos:

			keywords.append(term)

	return keywords[-int(n):]

#print gen_keywords(open(sys.argv[1], 'r').read(), sys.argv[2], sys.argv[3])














