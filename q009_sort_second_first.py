#!/usr/bin/python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-09-08

import sys

def sortSecFir(filePath):
  line_of = {}
  for line in open(filePath):
    col1, col2 = line.split('\t')
    line_of[col1] = col2
  for k, v in sorted(line_of.items(), key=lambda x: (x[1], x[0]), reverse=True):
    sys.stdout.write('%s\t%s' % (k, v))

if __name__ == '__main__':
  sortSecFir(sys.argv[1])
