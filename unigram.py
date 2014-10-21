import nltk
import util
import operator
import progressbar

def gen_dict(twitter):

    preprocessed = twitter.preprocessed

    count = preprocessed.count()

    tweets = preprocessed.find({}, {'text':1, '_id':0})

    tokenizer = util.Tokenizer()

    terms = []

    print "generate dictionary"

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
