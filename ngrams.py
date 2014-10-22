import nltk
import util
import codecs
import operator
import progressbar
from nltk.collocations import *

def get_unigram(twitter):

    preprocessed = twitter.preprocessed

    count = preprocessed.count()

    tweets = preprocessed.find({}, {'text':1, '_id':0})

    tokenizer = util.Tokenizer()

    terms = []

    print "generate unigram"

    bar = progressbar.ProgressBar(maxval = count, widgets = [progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()]).start()

    i = 0

    for tweet in tweets:

        terms.extend(tokenizer.tokenize(tweet['text']))

        bar.update(i + 1)

        i = i + 1

    bar.finish()

    freqdist = nltk.FreqDist(terms)

    sorted_freqdist = sorted(freqdist.items(), key=operator.itemgetter(1))

    print "calculate frequency"

    bar = progressbar.ProgressBar(maxval = len(freqdist), widgets = [progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()]).start()

    i = 0

    for item in sorted_freqdist:

        twitter.unigram.insert({'collocation':item[0], 'frequency':item[1]})

        bar.update(i + 1)

        i = i + 1

    bar.finish()

def get_bigram(twitter):

#    bigram_measures = BigramAssocMeasures()

    preprocessed = twitter.preprocessed

    count = preprocessed.count()

    tweets = preprocessed.find({}, {'text':1, '_id':0})

    tokenizer = util.Tokenizer()

    bigrams = []

    print "generate bigrams"

    bar = progressbar.ProgressBar(maxval = count, widgets = [progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()]).start()

    i = 0

    for tweet in tweets:

        bigram = [collocation for collocation in nltk.bigrams(tokenizer.tokenize(tweet['text']))]

        bigrams.extend(bigram)

        bar.update(i + 1)

        i = i + 1

    bar.finish()

    freqdist = nltk.FreqDist(bigrams)

    sorted_freqdist = sorted(freqdist.items(), key=operator.itemgetter(1))

    print "calculate frequency"

    bar = progressbar.ProgressBar(maxval = len(freqdist), widgets = [progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()]).start()

    i = 0

    file = codecs.open('bigram', 'w', 'utf-8')

    for item in sorted_freqdist:

        twitter.bigram.insert({'collocation':item[0], 'frequency':item[1]})

        file.write('%s\t%d\n' % (item[0], item[1]))

        bar.update(i + 1)

        i = i + 1

    bar.finish()

def get_trigram(twitter):

#    trigram_measures = TrigramAssocMeasures()

    preprocessed = twitter.preprocessed

    count = preprocessed.count()

    tweets = preprocessed.find({}, {'text':1, '_id':0})

    tokenizer = util.Tokenizer()

    trigrams = []

    print "generate trigrams"

    bar = progressbar.ProgressBar(maxval = count, widgets = [progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()]).start()

    i = 0

    for tweet in tweets:

        trigram = [collocation for collocation in nltk.trigrams(tokenizer.tokenize(tweet['text']))]

        trigrams.extend(trigram)

        bar.update(i + 1)

        i = i + 1

    bar.finish()

    freqdist = nltk.FreqDist(trigrams)

    sorted_freqdist = sorted(freqdist.items(), key=operator.itemgetter(1))

    print "calculate frequency"

    bar = progressbar.ProgressBar(maxval = len(freqdist), widgets = [progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()]).start()

    i = 0

    file = codecs.open('trigram', 'w', 'utf-8')

    for item in sorted_freqdist:

        twitter.trigram.insert({'collocation':item[0], 'frequency':item[1]})

        file.write('%s\t%d\n' % (item[0], item[1]))

        bar.update(i + 1)

        i = i + 1

    bar.finish()
