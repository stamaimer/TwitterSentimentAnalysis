# -*- coding: utf-8 -*-

"""
this code implements a basic twitter-aware preprocesser
"""

import re
import sys
import codecs
import HTMLParser

def preprocess(text):

	text = re.sub(u'\u2026', ' ', text)                             #deal with horizontal ellipsis
	text = re.sub(u'[\u201c\u201d]', '"', text)                     #deal with double quotation mark
	text = re.sub(u'[\u2018\u2019]', '\'', text)                    #deal with single quotation mark

	text = re.sub('h…', 'URL', text)                                #deal with truncated url
	text = re.sub('ht?….*$', 'URL', text)                           #deal with truncated url 
	text = re.sub('(^|)?http?s?:?/?/?.*?( |$)', 'URL', text)        #deal with compelted url

	text = re.sub(u'(RT |\\\\|\u201c)"?@.*?[: ]', ' ', text)        #deal with retweet
	text = re.sub('\.?@.*?( |:|$)', 'USERNAME ', text)              #deal with username


	text = HTMLParser.HTMLParser().unescape(text)                   #deal with character entity
	text = re.sub('[][!"#$*,/;<=>?@\\\\^_`{|}~]', ' ', text)        #deal with punctuation

	text = re.sub('( - )', ' ', text)
	text = re.sub('---', ' ', text)
	text = re.sub('\.\.\.', ' ', text)
	text = re.sub('(, |\.( |$))', ' ', text)


	return text

argc = 3

if argc != len(sys.argv):

    print 'usage: python preprocessim.py ifilename ofilename'

    exit(1)

ifile = codecs.open(sys.argv[1], 'r', 'utf-8')
ofile = codecs.open(sys.argv[2], 'w', 'utf-8')

for line in ifile:

    ofile.write(preprocess(line))
    ofile.write('\n')
    ofile.write(line)
    ofile.write('\n')

print "finished"
