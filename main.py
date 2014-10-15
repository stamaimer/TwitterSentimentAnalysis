import progressbar
import preprocess
import pymongo
import codecs

def get_tweets_from_mongodb():

    mongo_client = pymongo.MongoClient('127.0.0.1', 27017)

    twitter = mongo_client.twitter

    tweets = twitter.tweets

    count = tweets.count()

    tweets = tweets.find({}, {'text':1, '_id':0})

    tweet_texts = []

    print "get tweets from mongodb"

    bar = progressbar.ProgressBar(maxval = count, widgets = [progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])

    i = 0

    for tweet in tweets:

        tweet_texts.extend(tweet['text'])

        bar.update(i + 1)

        i = i + 1

    return tweet_texts, count

def get_tweets_from_file(filename):

    file = codecs.open(filename, 'r', 'utf-8')

    tweet_texts = file.readlines()

    count = len(tweet_texts)

    file.close()

    return tweet_texts, count

def main():

    tweets, count = get_tweets_from_mongodb()

    ofile = codecs.open('./data/sourced', 'w', 'utf-8')

    try:

        print 'write source tweets to file'

        bar = progressbar.ProgressBar(maxval = count, widgets = [progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])

        i = 0

        for tweet in tweets:

            ofile.writeline(tweet)

            bar.update(i + 1)

            i = i + 1

        print '%d tweets sourced' % count

    finally:

        ofile.close()

    ofile = codecs.open('./data/removed', 'w', 'utf-8')

    try:

        preprocess.remove(tweets, count, ofile)

        print '%d tweets removed' % count - len(ofile.readlines())

    finally:

        ofile.close()

    ifile = codecs.open('./data/removed', 'r', 'utf-8')
    ofile = codecs.open('./data/preprocessed', 'w', 'utf-8')

    try:

        count = len(ifile.readlines())

        preprocess.preprocess(ifile, count, ofile)

        print '%d tweets preprocessed' % count

    finally:

        ifile.close()
        ofile.close()

if __name__ == '__main__':

    main()
