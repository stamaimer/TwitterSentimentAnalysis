import sys
import json
import nltk
import numpy
import tfidf

N = 100 				# number of words yto consider
TOP_SENTENCES = 5		# number of sentences to return for a "top n" summary
CLUSTER_THRESHOLD = 5 	# distance between words to considers

# approach taken from "The Automatic Creation of Literature Abstracts" by H.P. Luhn

def cal_sents_score(sentences, keywords):

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

		if 0 == len(word_idx): continue

		word_idx.sort()
		
		clusters = []

		cluster  = [word_idx[0]]

		i = 1

		while i < len(word_idx):
		 	
		 	if word_idx[i] - word_idx[i - 1] < CLUSTER_THRESHOLD:

		 		cluster.append(word_idx[i])

		 	else:

		 		clusters.append(cluster[:])

		 		cluster = [word_idx[i]]

		 	i += 1

		clusters.append(cluster)

		max_cluster_score = 0

		for cluster in clusters:

			count_of_keywords = len(cluster)

			cluster_length = cluster[-1] - cluster[0] + 1

			score = 1.0 * count_of_keywords * count_of_keywords / cluster_length

			if score > max_cluster_score:

				max_cluster_score = score

		scores.append((sent_idx, max_cluster_score))

	return scores


def summarize(text, path2corpus):
	
	keywords  = tfidf.gen_keywords(text, path2corpus, N)

	keywords  = [element[0] for element in keywords]

	sentences = [sentence.lower() for sentence in nltk.tokenize.sent_tokenize(text)]

	scored_sents = cal_sents_score(sentences, keywords)

	avg = numpy.mean([element[1] for element in scored_sents])
	std = numpy.std([element[1] for element in scored_sents])

	mean_sents = [(sent_idx, score) for (sent_idx, score) in scored_sents if score > avg + 0.5 * std]

	top_n_sents = sorted(scored_sents, key = lambda sentence : sentence[1])[-TOP_SENTENCES:]
	top_n_sents = sorted(top_n_sents, key = lambda sentence : sentence[0])

	return dict(top_n_summary = [sentences[idx] for (idx, score) in top_n_sents],
				mean_summary = [sentences[idx] for (idx, score) in mean_sents])

result = summarize(open(sys.argv[1], 'r').read(), sys.argv[2])

print "top_n_summary\n"
print ' '.join(result["top_n_summary"])
print "mean_summary\n"
print ' '.join(result["mean_summary"])




