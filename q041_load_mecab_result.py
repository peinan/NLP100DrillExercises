#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-12-06

import sys, MeCab, pickle

def loadMecabResult(line):
  """surface, base [6], pos [0], pos1 [1]"""
  line = line.strip()
  tagger = MeCab.Tagger('-Ochasen')
  node = tagger.parseToNode(line)
  sentence = []
  while node:
    # print '%s %s' % (node.surface, node.feature)
    features = node.feature.split(',')
    sentence.append({'srf': node.surface, 'base': features[6], \
        'pos': features[0], 'pos1': features[1]})
    node = node.next

  return sentence

if __name__ == '__main__':
  sentences = [ loadMecabResult(line) for line in open(sys.argv[1]) ]
  pickle.dump(sentences, open('mecab.result', 'w'))
