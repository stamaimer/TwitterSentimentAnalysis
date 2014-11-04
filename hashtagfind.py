import nltk
import codecs
import operator

def hashtagfind(twitter, frequency):

    tweets = twitter.tweets

    hashtags = tweets.find({}, {'entities.hashtags':1, '_id':0})

    tmp = []

    for hashtag in hashtags:

        tmp.extend(hashtag['entities']['hashtags'])

    hashtags = []

    for i in tmp:

        hashtags.append(i['text'].lower())

    freqdist = nltk.FreqDist(hashtags)

    sorted_freqdist = sorted(freqdist.items(), key=operator.itemgetter(1), reverse=True)

    file = codecs.open('hashtags', 'w', 'utf-8')

    for item in sorted_freqdist:

        file.write('%s\t%d' % (item[0], item[1]))

        file.write('\n')

    file.close()

