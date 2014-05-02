#!/usr/bin/env python
#coding:utf-8
#
# Author: Peinan ZHANG
#

import sys

N = sys.argv[1]
l = open("address.txt").readlines()

for i in range(int(N)):
  print l[i]
