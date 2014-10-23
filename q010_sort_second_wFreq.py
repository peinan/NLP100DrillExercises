#!/usr/bin/python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-09-08

import sys
from collections import defaultdict

def sortSecWFreq(filepath):
  stringFreq = defaultdict(lambda: 0)
  for line in open(filepath):
    stringFreq[line.strip().decode('utf-8')] += 1
  return stringFreq

if __name__ == '__main__':
  stringFreq = sortSecWFreq(sys.argv[1])
  for k, v in sorted(stringFreq.items(), key=lambda x: x[1], reverse=True):
    sys.stdout.write('%3d %s\n' % (v, k.encode('utf-8')))
