#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-12-08

import sys
import matplotlib.pyplot as plt

def plotFreq(inputs):
  verb_freq = []
  for line in inputs:
    verb, freq = line.strip().split(' ')
    verb = verb.decode('utf-8')
    freq = int(freq)
    verb_freq.append((verb, freq))
  verbs = list(zip(*verb_freq)[0])
  freqs = list(zip(*verb_freq)[1])
  X = range(len(verbs))

  plt.bar(X, freqs, align='center')
  plt.xticks(X, verbs)
  plt.show()


if __name__ == '__main__':
  inputs = sys.stdin.readlines()
  plotFreq(inputs)
