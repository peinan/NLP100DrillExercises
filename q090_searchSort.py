#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-02-11

import sys, pymongo
from pymongo import Connection

con = Connection('localhost', 27017)
db  = con.nlp100_peinan
clt = db.tweets

print 'body\tretweeted'
print '-'*17
for atweet in clt.find({'body': sys.argv[1]}).sort('freq_rted', pymongo.DESCENDING):
  print '%s\t%s' % (atweet['body'], atweet['freq_rted'])
