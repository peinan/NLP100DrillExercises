#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-12-06

import sys, MeCab, pickle

def extractVerbBases(sentence, mode=2):
  if mode == 2:
    return [ '%s %s' % (word['srf'], word['base']) \
        for word in sentence if word['pos'] == '動詞' ]
  elif mode == 1:
    return [ word['base'] for word in sentence if word['pos'] == '動詞' ]

if __name__ == '__main__':
  sentences = pickle.load(open('mecab.result'))
  for sentence in sentences:
    verbBases = extractVerbBases(sentence)
    for verbBase in verbBases:
      print verbBase
