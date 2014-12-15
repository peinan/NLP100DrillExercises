#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-12-08

import sys
import matplotlib.pyplot as plt
from collections import *

def plotFreq(inputs):
  verb_of = defaultdict(lambda: [])
  for line in inputs:
    verb, freq = line.strip().split(' ')
    verb = verb.decode('utf-8')
    freq = int(freq)
    verb_of[freq].append(verb)
   
  oVerb_of = OrderedDict(sorted(verb_of.items()))
  X = range(len(oVerb_of.keys())) # x-axis: times of appearance
  Y = [ len(v) for k, v in oVerb_of.items() ] # y-axis: counts of freq

  plt.bar(X, Y)
  plt.xticks(X, verb_of.keys())
  plt.show()


if __name__ == '__main__':
  inputs = sys.stdin.readlines()
  plotFreq(inputs)
