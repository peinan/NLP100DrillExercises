#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-01-25

import sys
import simplejson as sj
from pymongo import Connection

tweets = sj.load(open(sys.argv[1]))

c = Connection('localhost', 27017)
db = c.soccor
clt = db.tweets

for atweet in tweets:
  url = 'http://twitter.com/%s/status/%s' % (atweet['user']['screen_name'], atweet['id_str'])
  date = atweet['created_at']
  user = atweet['user']['id_str']
  nickname = atweet['user']['name']
  body = atweet['text']
  rt_url = 'http://twitter.com/%s/status/%s' \
      % (atweet['retweeted_status']['user']['screen_name'], \
          atweet['retweeted_status']['id_str']) \
      if 'retweeted_status' in atweet else None
  reply_url = 'http://twitter.com/%s/status/%s' \
      % (atweet['in_reply_to_screen_name'], atweet['in_reply_to_status_id_str']) \
      if atweet['in_reply_to_screen_name'] is not None else None
  # qt_url
  freq_rted = atweet['retweet_count']
  # freq_replied
  # freq_qt
  clt.save({'url': url, 'date': date, 'user': user, 'nickname': nickname, \
      'body': body, 'rt_url': rt_url, 'reply_url': reply_url, 'freq_rted': freq_rted})

