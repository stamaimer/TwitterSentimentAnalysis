import util
import nltk
from nltk.stem.wordnet import WordNetLemmatizer

stopwords = nltk.corpus.stopwords.words('english') + ['']

tokenizer = util.Tokenizer()

def del_stopwords(tweet):

    for term in tweet:

        if term in stopwords:

            tweet.remove(term)

    return tweet

def lemmatize(tweet):

    lmtzr = WordNetLemmatizer()

    for i in range(len(tweet)):

        tweet[i] = lmtzr.lemmatize(tweet[i])

    return tweet
