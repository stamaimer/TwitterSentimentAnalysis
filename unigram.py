import nltk
import util
from nltk.stem.wordnet import WordNetLemmatizer

def del_stopwords(tweet):

    stopwords = nltk.corpus.stopwords.words('english') + ['']

    for term in tweet:

        if term in stopwords:

            tweet.remove(term)

    return tweet

def lemmatize(tweet):

    lmtzr = WordNetLemmatizer()

    for i in range(len(tweet)):

        tweet[i] = lmtzr.lemmatize(tweet[i])

    return tweet

def gen_dict(tweets, count, file):

    tokenizer = util.Tokenizer()

    terms = []

    for tweet in tweets:

        terms.extend(tokenizer.tokenize(tweet))

    freqdist = nltk.FreqDist(terms)

    return freqdist

