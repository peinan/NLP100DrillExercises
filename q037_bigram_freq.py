#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-10-24

import sys

def countFreq(lines):
  from collections import defaultdict
  count_of = defaultdict(lambda: 0)
  for line in lines:
    count_of[line] += 1
  return count_of

if __name__ == '__main__':
  lines = sys.stdin.readlines()
  freq_of = countFreq(lines)
  for k, v in sorted(freq_of.items(), key=lambda x: x[1], reverse=True):
    sys.stdout.write('%d\t%s' % (v, k))
