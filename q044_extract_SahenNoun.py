#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-12-06

import sys, MeCab, pickle

def extractSahenNoun(sentence):
  return [ word['srf'] for word in sentence if word['pos1'] == 'サ変接続' ]

if __name__ == '__main__':
  sentences = pickle.load(open('mecab.result'))
  for sentence in sentences:
    sahenNouns = extractSahenNoun(sentence)
    for sahenNoun in sahenNouns:
      print sahenNoun
