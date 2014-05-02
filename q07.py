#!/usr/bin/env python
#coding:utf-8
#
# Author: Peinan ZHANG
#

import sys
from collections import defaultdict
l = open(sys.argv[1], "r").readlines()

col1 = []
for i in l:
  col1.append(i.split()[0])

count_of = defaultdict(lambda: 0)
for line in col1:
  for i in line:
    count_of[i] += 1

print len(count_of.keys())