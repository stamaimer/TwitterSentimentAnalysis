import os
import nltk
from __future__ import division

def prepare(path2corpus):
	
	files = os.listdir(path2corpus)

	filelists = {}

	for file in files:

		filelists[file] = [term for term in open(file, 'r').read(-1).split()]

	return filelists

def cal_term_freq(text):

	terms    = [term for term in text.split()]

	length   = len(terms)

	freqdist = nltk.FreqDist(terms)

	for key in freqdist.keys():

		freqdist[key] = freqdist[key] / length

	return freqdist

def cal_idoc_freq(dist2cal, path2corpus):

	filelists = prepare(path2corpus)

	for key in dist2cal.keys():

		









