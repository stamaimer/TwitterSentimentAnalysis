# -*- coding: utf-8 -*-

"""
this code implements a basic twitter-aware preprocesser
"""

import re
import HTMLParser

def remove_duplicate(tweets, count, file):

    set = set()

    for tweet in tweets:

        set.add(tweet)

    for tweet in set:

        if 'RT' not in tweet and 'rt' not in tweet:

            file.write(tweet)

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

    for tweet in tweets:

        tweet = preprocess(tweet)

        file.write(tweet)
