#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-10-24

import sys

def mkWordBigram(words):
  return [ (words[i], words[i + 1]) for i in range(len(words) - 1) ]


def loadTokenFile(filepath):
  sentences = []
  words = []
  for line in open(filepath):
    if line == '\n':
      sentences.append(tuple(words))
      words = []
      continue
    words.append(line.strip())

  return sentences


if __name__ == '__main__':
  sentences = loadTokenFile(sys.argv[1])
  wordBigram = []
  for words in sentences:
    wordBigram += mkWordBigram(words)
  for bigram in wordBigram:
    sys.stdout.write('%s\t%s\n' % (bigram[0], bigram[1]))
