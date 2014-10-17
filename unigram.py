import nltk
import util
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

    print "calculate frequency"

    bar = progressbar.ProgressBar(maxval = count, widgets = [progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()]).start()

    i = 0

    for key in freqdist.keys():

        twitter.unigram.insert({'collocation':key, 'frequency':freqdist[key]})

        bar.update(i + 1)

        i = i + 1

    bar.finish()

