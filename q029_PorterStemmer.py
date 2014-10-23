#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-10-23

from nltk.stem import *

stemmer = PorterStemmer()

plurals = [ 'caresses', 'flies', 'dies', 'mules', 'denied',
            'died', 'agreed', 'owned', 'humbled', 'sized',
            'meeting', 'stating', 'siezing', 'itemization',
            'sensational', 'traditional', 'reference', 'colonizer',
            'plotted' ]

singles = [ stemmer.stem(plural) for plural in plurals ]

print '%s%s%s' % ('plurals', ' '*(15 - len('plurals')), 'singels')
print '-'*22
for plural, single in zip(plurals, singles):
  print '%s%s%s' % (plural, ' '*(15 - len(plural)), single)
