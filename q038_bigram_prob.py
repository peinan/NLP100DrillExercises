#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-10-24

import sys
from q010_sort_second_wFreq import sortSecWFreq
from collections import defaultdict

def calcBigramFreq(lines, unigram_freq):
  bigram_freq = {}
  for line in lines:
    count, c_word, n_word = line.strip().decode('utf-8').split('\t')
    bigram_freq['%s\t%s' % (c_word, n_word)] = \
        float(count) / unigram_freq[c_word]
  return bigram_freq


if __name__ == '__main__':
  unigram_freq = sortSecWFreq('data/medline.txt.sent.tok')
  bigram_freq  = calcBigramFreq(sys.stdin.readlines(), unigram_freq)
  for k, v in sorted(bigram_freq.items(), key=lambda x: x[1], reverse=True):
    sys.stdout.write('%f\t%s\n' % (v, k.encode('utf-8')))
