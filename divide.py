#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Carwest Sung <carwestsam@gmail.com>
#
# Distributed under terms of the MIT license.

"""
DivideEmoticons
0 for cannote identify
1-8 for emotions
"""

ecstaIcons=[ u'\U0001f600', u'\U0001f601', u'\U0001f602', u'\U0001f604', u'\U0001f606', u'\u0001f607', u'\U0001f608', u'\U0001f60A', u'\U0001F60B', u'\U0001f60c', u'\U0001f60E', u'\U0001f60f', u'\U0001f61b', u'\U0001f61c', u'\U0001f61D', u'\U0001f62c', u'\U0001f638', u'\U0001f639', u'\U0001f63A', u'\U0001f63C', u'\U0001f642', u'\U0001f648', u'\U0001f649', u'\U0001f64B']
admirIcons=[u'\U0001f617', u'\U0001f618', u'\U0001f619', u'\U0001f61a', u'\U0001f63b', u'\U0001f63d', u'\U0001f646', u'\U0001f647', u'\U0001f64f']
terrrIcons=[u'\U0001f613', u'\U0001f61f', u'\U0001f628', u'\U0001f630', u'\U0001f631', u'\U0001f64a']
amazeIcons=[u'\U0001f605', u'\U0001f62e', u'\U0001f62f', u'\U0001f632',
u'\U0001f633', u'\U0001f640']
griefIcons=[u'\U0001f614', u'\U0001f61e', u'\U0001f622', u'\U0001f623', u'\U0001f625', u'\U0001f626', u'\U0001f627', u'\U0001f629', u'\U0001f62b', u'\U0001f62d', u'\U0001f63f', u'\U0001f641', u'\U0001f64d', u'\U0001f64e']
loathIcons=[u'\U0001f610',u'\U0001f612', u'\U0001f615']
angerIcons=[u'\U0001f620', u'\U0001f621']
vigilIcons=[u'\U0001f609']


ecstaEmo = {'filename': 'ecstaEmo.txt', 'Icons': ecstaIcons, 'cnt':0, 'fileptr':0, 'label':'1'}
admirEmo = {'filename': 'admirEmo.txt', 'Icons': admirIcons, 'cnt':0, 'fileptr':0, 'label':'2'}
terrrEmo = {'filename': 'terrrEmo.txt', 'Icons': terrrIcons, 'cnt':0, 'fileptr':0, 'label':'3'}
amazeEmo = {'filename': 'amazeEmo.txt', 'Icons': amazeIcons, 'cnt':0, 'fileptr':0, 'label':'4'}
griefEmo = {'filename': 'griefEmo.txt', 'Icons': griefIcons, 'cnt':0, 'fileptr':0, 'label':'5'}
loathEmo = {'filename': 'loathEmo.txt', 'Icons': loathIcons, 'cnt':0, 'fileptr':0, 'label':'6'}
angerEmo = {'filename': 'angerEmo.txt', 'Icons': angerIcons, 'cnt':0, 'fileptr':0, 'label':'7'}
vigilEmo = {'filename': 'vigilEmo.txt', 'Icons': vigilIcons, 'cnt':0, 'fileptr':0, 'label':'8'}

Emotions = [ecstaEmo, admirEmo, terrrEmo,amazeEmo, griefEmo, loathEmo, angerEmo, vigilEmo ];

def DivideEmotion( text ):
    if not text:
        return 0

    vote = [0,]
    for emo in Emotions:
        vote.append( 0 )

    totalvote = 0
    maxvote = 0
    maxpos = 0
    for emo in Emotions:
        label = int( emo['label'] )
        for icon in emo['Icons']:
            if icon in text:
                vote[ label ] += 1
                totalvote += 1
                if vote[label] > maxvote:
                    maxvote = vote [label]
                    maxpos = label

    if maxvote * 2 > totalvote:
        return maxpos
    else :
        return 0

