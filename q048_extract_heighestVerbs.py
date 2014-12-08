#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-12-08

from q047_integrated import *
from collections import Counter

def extractFreqVerbs(sentences, mode='base'):
  verbs = []
  bases = []
  for sentence in sentences:
    verbs += extractVerbs(sentence)
    bases += extractVerbBases(sentence, mode=1)
  verbCounter = Counter(verbs)
  baseCounter = Counter(bases)

  if mode == 'verb':
    return verbCounter
  elif mode == 'base':
    return baseCounter


if __name__ == '__main__':
  sentences = pickle.load(open('mecab.result'))
  freqCounter = extractFreqVerbs(sentences)
  for k, v in sorted(freqCounter.most_common(), key=lambda x:x[1], reverse=True):
    print k, v

