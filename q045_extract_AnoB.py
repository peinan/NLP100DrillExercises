#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-12-06

import sys, MeCab, pickle

def extractAnoBs(sentence):
  return [ '%s %s %s' \
      % (sentence[i - 1]['srf'], sentence[i]['srf'], sentence[i + 1]['srf']) \
      for i in xrange(len(sentence)) if sentence[i]['srf'] == 'の' \
      if sentence[i - 1]['pos'] == '名詞' and sentence[i + 1]['pos'] == '名詞' ]

if __name__ == '__main__':
  sentences = pickle.load(open('mecab.result'))
  for sentence in sentences:
    AnoBs = extractAnoBs(sentence)
    for AnoB in AnoBs:
      print AnoB
