import nltk

def cal_term_freq(text):

	return nltk.FreqDist([term for term in text.split()])

def cal_idoc_freq(dist):
	pass
