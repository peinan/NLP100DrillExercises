#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG

import sys

def lineDiff(filePath):
  from collections import defaultdict
  count_of = defaultdict(lambda: 0)
  for line in open(filePath):
    col1 = line.strip().split()[0]
    count_of[col1] += 1
  
  print len(count_of)

if __name__ == '__main__':
  lineDiff(sys.argv[1])

