#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-01-26

import sys
from pymongo import Connection

con = Connection('localhost', 27017)
db = con.nlp100_peinan
clt = db.tweets

for atweet in clt.find({ 'url': '%s' % sys.stdin.readline().strip() }):
  print atweet['body']
