import nltk
import collections

def get_ngrams(twitter, n):

    if 1 == n:

        collection = twitter.unigram

    elif 2 == n:

        collection = twitter.bigram

    elif 3 == n:

        collection = twitter.trigram

    records = collection.find({}, {'collocation':1, '_id':0})

    collocations = []

    for record in records:

        collocations.append(record['collocation'])

    return collocations

def gen_featvects(twitter, n):

    labeled = twitter.labeled

    count = labeled.count()

    labeled = labeled.find({}, {'text':1, 'label':1, '_id':0})

    for item in labeled:



def naive_bayes_classifier(twitter):
