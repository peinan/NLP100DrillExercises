#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-12-06

import sys, MeCab, pickle

def extractVerbs(sentence):
  return [ word['srf'] for word in sentence if word['pos'] == '動詞' ]

if __name__ == '__main__':
  sentences = pickle.load(open('mecab.result'))
  for sentence in sentences:
    verbs = extractVerbs(sentence)
    for verb in verbs:
      print verb
