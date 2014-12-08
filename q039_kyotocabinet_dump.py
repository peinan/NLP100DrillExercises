#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-11-17

import sys
from kyotocabinet import *

def kch_dump(lines):
  db = DB()
  if not db.open('dict.kch', DB.OWRITER | DB.OCREATE):
    print >>sys.stderr, 'set error: ' + str(db.error())
  for line in lines:
    line = line.decode('utf-8')
    prob, w1, w2 = line.strip().split('\t')
    print line
    if not db.set('%s %s' % (w1, w2), prob):
      print >>sys.stderr, 'set error: ' + str(db.error())


if __name__ == '__main__':
  lines = sys.stdin.readlines()
  kch_dump(lines)
