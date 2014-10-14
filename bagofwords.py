import nltk
import pymongo
import utilities
import preprocessim as preprocess

def get_tweets():

    mongo_client = pymongo.MongoClient('127.0.0.1', 27017)

    twitter = mongo_client.twitter

    tweets = twitter.tweets

    return tweets.count(), tweets.find()

def gen_dict():

    counts, tweets = get_tweets()

    tokenizer = utilities.Tokenizer()

    i = 0

    terms = []

    for tweet in tweets:

        tweet = preprocess.preprocess(tweet['text'])

        terms.extend(tokenizer.tokenize(tweet))

        i = i + 1

        print float(i) / counts

    freqdist = nltk.FreqDist(terms)

    return freqdist

