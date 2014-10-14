# -*- coding: utf-8 -*-

"""
this code implements a basic twitter-aware preprocesser
"""

import re
import HTMLParser
import progressbar

def remove_duplicate(tweets, count, file):

    set = set()

    print "remove duplicate"

    progressbar = progressbar.ProgressBar(maxval = count, widgets = [progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])

    i = 0

    for tweet in tweets:

        set.add(tweet)

        progressbar.update(i + 1)

        i = i + 1

    print "remve rt"    

    progressbar = progressbar.ProgressBar(maxval = len(set), widgets = [progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])

    i = 0

    for tweet in set:

        if 'RT' not in tweet and 'rt' not in tweet:

            file.writeline(tweet)

        progressbar.update(i + 1)

        i = i + 1

def preprocess(tweet):

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

def preprocess(tweets, count, file):

    print "preprocess"

    progressbar = progressbar.ProgressBar(maxval = count, widgets = [progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])

    i = 0

    for tweet in tweets:

        tweet = preprocess(tweet)

        file.writeline(tweet)

        progressbar.update(i + 1)

        i = i + 1
