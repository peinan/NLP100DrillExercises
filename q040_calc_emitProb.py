#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-12-06

from kyotocabinet import *
import sys

if __name__ == '__main__':
  db = DB()
  if not db.open('dict.kch', DB.OREADER):
    print >>sys.stderr, 'OpenError: %s' % str(db.error())
  
  lines = sys.stdin.readlines()
  for line in lines:
    words = line.strip().split(' ')
    wordNum = len(words)
    emitProb = 1
    print words
    for i in range(wordNum - 1):
      word = '%s %s' % (words[i], words[i + 1])
      if word in db:
        emitProb *= db.get(word)
      else:
        emitProb = 0
        break
