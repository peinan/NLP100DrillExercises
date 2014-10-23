#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-10-23

import sys, re
from nltk.stem import *

def stemWords(line):
  alpha = re.compile(r'[a-zA-Z\-\_]+')
  if alpha.match(line):
    stemmer = PorterStemmer()
    return stemmer.stem(line)
  return line

if __name__ == '__main__':
  for line in sys.stdin.readlines():
    try:
      col1, col2 = line.strip().split('\t')
      sys.stdout.write('%s\t%s\t%s\n' % (col1, col2, stemWords(col2)))
    except ValueError:
      sys.stdout.write(line)
