#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-10-23

import sys, marshal
from q031_view_words_detail import searchWord

if __name__ == '__main__':
  wordsDict = marshal.load(open('data/word.dict'))
  for line in open(sys.argv[1]):
    try:
      print searchWord(line.strip().split('\t')[2], wordsDict)
    except IndexError:
      pass
