import nltk
import util

icons = [u'\U0001f600', u'\U0001f601', u'\U0001f602', u'\U0001f603',
         u'\U0001f604', u'\U0001f606', u'\u0001f607', u'\U0001f608',
         u'\U0001f60A', u'\U0001F60B', u'\U0001f60c', u'\U0001f60E',
         u'\U0001f60f', u'\U0001f61b', u'\U0001f61c', u'\U0001f61D',
         u'\U0001f62c', u'\U0001f638', u'\U0001f639', u'\U0001f63A',
         u'\U0001f63C', u'\U0001f642', u'\U0001f648', u'\U0001f649',
         u'\U0001f64B', u'\U0001f60D', u'\U0001f617', u'\U0001f618',
         u'\U0001f619', u'\U0001f61a', u'\U0001f63b', u'\U0001f63d',
         u'\U0001f646', u'\U0001f647', u'\U0001f64f', u'\U0001f613',
         u'\U0001f61f', u'\U0001f628', u'\U0001f630', u'\U0001f631',
         u'\U0001f64a', u'\U0001f605', u'\U0001f62e', u'\U0001f62f',
         u'\U0001f632', u'\U0001f633', u'\U00016f35', u'\U0001f640',
         u'\U0001f614', u'\U0001f616', u'\U0001f61e', u'\U0001f622',
         u'\U0001f623', u'\U0001f625', u'\U0001f626', u'\U0001f627',
         u'\U0001f629', u'\U0001f62b', u'\U0001f62d', u'\U0001f63f',
         u'\U0001f641', u'\U0001f64d', u'\U0001f64e', u'\U0001f610',
         u'\U0001f611', u'\U0001f612', u'\U0001f615', u'\U0001f645',
         u'\U0001f620', u'\U0001f621', u'\U0001f624', u'\U0001f63e', 
         u'\U0001f609']


deal = [1, util.Tokenizer().tokenize, nltk.bigrams, nltk.trigrams]

def get_ngrams(twitter, n):

    if 1 == n:

        collection = twitter.unigram

        records = collection.find({'frequency':{'$gte':1460, '$lte':107699}}, {'collocation':1, '_id':0})

        print 'generate unigram'

    elif 2 == n:

        collection = twitter.bigram

        records = collection.find({'frequency':{'$gte':75, '$lte':98}}, {'collocation':1, '_id':0})

        print 'generate bigram'

    elif 3 == n:

        collection = twitter.trigram

        records = collection.find({'frequency':{'$gte':2, '$lte':2}}, {'collocation':1, '_id':0})

        print 'generate trigram'

    collocations = []

    for record in records:

        if record['collocation'] not in icons:

            collocations.append(record['collocation'])

    return collocations

def gen_featvect(twitter, n):

    collocations = get_ngrams(twitter, n)

    labeled = twitter.labeled

    count = labeled.count()

    labeled = labeled.find({'label':{'$ne':0}}, {'text':1, 'label':1, '_id':0})

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

    for i in range(3):

        testset = featvect[124167 * i : 124167 * (i + 1)]

        del featvect[124167 * i : 124167 * (i + 1)]

        trainset = featvect

        classifier = nltk.NaiveBayesClassifier.train(trainset)

        print 'accuracy of naivebayes classifier : ', nltk.classify.accuracy(classifier, testset)

def max_ent_classifier(twitter, n):

    featvect = gen_featvect(twitter, n)

    for i in range(3):

        testset = featvect[124167 * i : 124167 * (i * 1)]

        del featvect[124167 * i : 124167 * (i + 1)]

        trainset = featvect

        classifier = nltk.MaxentClassifier.train(trainset)

        print 'accuracy of max_ent_classifier : ', nltk.classify.accuracy(classifier, testset)

def svm_classifier(twitter, n):

    featvect = gen_featvect(twitter, n)

    for i in range(3):

        testset = featvect[124167 * i : 124167 * (i * 1)]

        del featvect[124167 * i : 124167 * (i + 1)]

        trainset = featvect

        classifier = nltk.SvmClassifier.train(trainset)

        print 'accuracy of svm_classifier : ', nltk.classify.accuracy(classifier, testset)

def scikit_classifier(twitter, n):

    featvect = gen_featvect(twitter, n)

    for i in range(3):

        testset = featvect[124167 * i : 124167 * (i * 1)]

        del featvect[124167 * i : 124167 * (i + 1)]

        trainset = featvect

        classifier = nltk.SklearnClassifier.train(trainset)

        print 'accuracy of sklearn_classifier : ', nltk.classify.accuracy(classifier, testset)
































