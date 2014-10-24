import nltk
import util
import collections

deal = [1, util.Tokenizer().tokenize, nltk.bigrams, nltk.trigrams]

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

def gen_featvect(twitter, n):

    collocations = get_ngrams(twitter, n)

    labeled = twitter.labeled

    count = labeled.count()

    labeled = labeled.find({}, {'text':1, 'label':1, '_id':0})

    featvect = [None for _ in range(count)]

    for item in labeled:

        featdist = {}

        if 1 == n:

            results = deal[n](item['text'])

        else:

            results = deal[n](deal[1](item['text']))

        for collocation in collocations:

            if collocation in results:

                featdist[collocation] = 1

            else:

                featdist[collocation] = 0

        featvect.append((featdist, item['label']))

    return featvect

def naive_bayes_classifier(twitter, n):

    featvect = gen_featvect(twitter, n)

    for i in range(5):

        testset = featvect[68577 * i : 68577 * (i + 1)]

        del featvect[68577 * i : 68577 * (i + 1)]

        trainset = featvect

        classifier = nltk.NaiveBayesClassifier.train(trainset)

        print 'accuracy of naivebayes classifier : ', nltk.classify.accuracy(classifier, testset), '\n'





























