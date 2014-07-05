from __future__ import division
import re
import os
import sys
import math
import nltk

def prepare(path2corpus):
	
	files = os.listdir(path2corpus)

	filelists = []

	for file in files:

		filelist = [term for term in open(file, 'r').read(-1).split()]

		filelists.append(nltk.Text(filelist))

	return filelists

def cal_term_freq(text):

	terms    = [term for term in text.split()]

	length   = len(terms)

	for i in range(0, length):

		terms[i] = re.sub('[\W]', '', terms[i])

	freqdist = nltk.FreqDist(terms)

	for key in freqdist.keys():

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

file = open(sys.argv[1], 'r')

term_freq = cal_term_freq(file.read(-1))

idoc_freq = cal_idoc_freq(term_freq, sys.argv[2])

tfidf = {}

for key in term_freq.keys():

	tfidf[key] = term_freq[key] * idoc_freq[key]

print tfidf.keys()[:10]











