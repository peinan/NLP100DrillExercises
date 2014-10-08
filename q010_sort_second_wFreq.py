#!/usr/bin/python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-09-08

import sys
from collections import defaultdict

def sortSecWFreq():
  stringFreq = defaultdict(lambda: 0)
  for line in open('col2.txt'):
    stringFreq[line] += 1
  for k, v in sorted(stringFreq.items(), key=lambda x: x[1], reverse=True):
    sys.stdout.write('%s' % k)

if __name__ == '__main__':
  sortSecWFreq()
