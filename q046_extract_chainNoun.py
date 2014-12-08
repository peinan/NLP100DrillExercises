#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-12-06

import sys, MeCab, pickle

def findLongestNoun(sentence):
  nouns = []
  noun = []
  for word in sentence:
    if word['pos'] == '名詞':
      noun.append(word['srf'])
    elif word['pos'] != '名詞':
      if len(noun) != 0:
        nouns.append(' '.join(noun))
        noun = []

  return nouns


if __name__ == '__main__':
  sentences = pickle.load(open('mecab.result'))
  for sentence in sentences:
    nouns = findLongestNoun(sentence)
    for noun in nouns:
      print noun
