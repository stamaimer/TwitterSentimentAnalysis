# -*- coding: utf-8 -*-

"""
this code implements a basic twitter-aware preprocesser
"""

import re
import HTMLParser
import progressbar

def remove(twitter):

    tweets = twitter.tweets

    count = tweets.count()

    tweets = tweets.find({}, {'text':1, '_id':0})

    container = set()

    print "remove duplicate tweets"

    bar = progressbar.ProgressBar(maxval = count, widgets = [progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()]).start()

    i = 0

    for tweet in tweets:

        container.add(tweet['text'])

        bar.update(i + 1)

        i = i + 1

    bar.finish()

    print "remve rt tweets"

    bar = progressbar.ProgressBar(maxval = len(container), widgets = [progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()]).start()

    i = 0

    for tweet in container:

        if 'RT' not in tweet and 'rt' not in tweet:

            twitter.removed.insert({'text':tweet})

        bar.update(i + 1)

        i = i + 1

    bar.finish()

def process(tweet):

	tweet = re.sub(u'\u2026', ' ', tweet)                             #deal with horizontal ellipsis
	tweet = re.sub(u'[\u201c\u201d]', '"', tweet)                     #deal with double quotation mark
	tweet = re.sub(u'[\u2018\u2019]', '\'', tweet)                    #deal with single quotation mark

	tweet = re.sub('h…', 'URL', tweet)                                #deal with truncated url
	tweet = re.sub('ht?….*$', 'URL', tweet)                           #deal with truncated url 
	tweet = re.sub('(^|)?http?s?:?/?/?.*?( |$)', 'URL', tweet)        #deal with compelted url

	tweet = re.sub(u'(RT |\\\\|\u201c)"?@.*?[: ]', ' ', tweet)        #deal with retweet
	tweet = re.sub('\.?@.*?( |:|$)', 'USERNAME ', tweet)              #deal with username

	tweet = HTMLParser.HTMLParser().unescape(tweet)                   #deal with character entity
	tweet = re.sub('[][!"#$*,/;<=>?@\\\\^_`{|}~]', ' ', tweet)        #deal with punctuation

	tweet = re.sub('( - )', ' ', tweet)
	tweet = re.sub('---', ' ', tweet)
	tweet = re.sub('\.\.\.', ' ', tweet)
	tweet = re.sub('(, |\.( |$))', ' ', tweet)

	return tweet

def preprocess(twitter):

    tweets = twitter.removed

    count = tweets.count()

    tweets = tweets.find({}, {'text':1, '_id':0})

    print "preprocess tweets"

    bar = progressbar.ProgressBar(maxval = count, widgets = [progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()]).start()

    i = 0

    for tweet in tweets:

        tweet = process(tweet['text'])

        twitter.preprocessed.insert({'text':tweet})

        bar.update(i + 1)

        i = i + 1

    bar.finish()
