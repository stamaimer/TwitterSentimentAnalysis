import nltk
import util
import collections

deal = [1, util.Tokenizer().tokenize, nltk.bigrams, nltk.trigrams]

def get_ngrams(twitter, n):

    if 1 == n:

        collection = twitter.unigram

        records = collection.find({'frequency':{'$gte':1460, '$lte':107699}}, {'collocation':1, '_id':0})

        print 'generate unigram'

    elif 2 == n:

        collection = twitter.bigram

        records = collection.find({'frequency':{'$gte':1460, '$lte':107699}}, {'collocation':1, '_id':0})

        print 'generate bigram'

    elif 3 == n:

        collection = twitter.trigram

        records = collection.find({'frequency':{'$gte':1460, '$lte':107699}}, {'collocation':1, '_id':0})

        print 'generate trigram'

    collocations = []

    for record in records:

        collocations.append(record['collocation'])

    return collocations

def gen_featvect(twitter, n):

    collocations = get_ngrams(twitter, n)

    labeled = twitter.labeled

    count = labeled.count()

    labeled = labeled.find({}, {'text':1, 'label':1, '_id':0})

    featvect = []

    print 'generate featvect'

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

        tmp = (featdist, item['label'])

        featvect.append(tmp)

    return featvect

def naive_bayes_classifier(twitter, n):

    featvect = gen_featvect(twitter, n)

    for i in range(5):

        testset = featvect[68577 * i : 68577 * (i + 1)]

        del featvect[68577 * i : 68577 * (i + 1)]

        trainset = featvect

        classifier = nltk.NaiveBayesClassifier.train(trainset)

        print 'accuracy of naivebayes classifier : ', nltk.classify.accuracy(classifier, testset)

def max_ent_classifier(twitter, n):

    featvect = gen_featvect(twitter, n)

    for i in range(5):

        testset = featvect[68577 * i : 68577 * (i * 1)]

        del featvect[68577 * i : 68577 * (i + 1)]

        trainset = featvect

        classifier = nltk.MaxentClassifier.train(trainset)

        print 'accuracy of max_ent_classifier : ', nltk.classify.accuracy(classifier, testset)






























