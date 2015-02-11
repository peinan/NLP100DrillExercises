#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-02-11

import os, re, pymongo, urllib
from pymongo import Connection

def parse_qs(aquery_str):
  qpart = aquery_str.split('?')[-1]

  def parse_q(aqset):
    prm, val = aqset.split('=')
    return (prm, val)

  if '&' in qpart:
    qset = qpart.split('&')
    qs = [ parse_q(aqset) for aqset in qset ]
  else:
    qs = [ parse_q(qpart) ]
  
  return qs

query = parse_qs(os.environ['QUERY_STRING'])

if 'QUERY_STRING' in os.environ:
  query = parse_qs(os.environ['QUERY_STRING'])
  qs = urllib.unquote(query[0][1])
else:
  qs = None

con = Connection('localhost', 27017)
db  = con.nlp100_peinan
clt = db.tweets

print 'Content-Type: text/html; charset=UTF-8'
print
print '<p>Your Query: %s</p>' % qs

if qs != None:
  print 'body\tretweeted<br>'
  print '-'*20, '<br>'

  for atweet in clt.find({'body': re.compile(qs.decode('utf-8'))}).sort('freq_rted', pymongo.DESCENDING):
    print '%s\t%s' % (atweet['body'].encode('utf-8'), atweet['freq_rted'])
else:
  print 'No tweets include your queries.'
