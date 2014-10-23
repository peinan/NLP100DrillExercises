#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-10-23

import sys, os
from q027_top100 import topN
from q010_sort_second_wFreq import sortSecWFreq

def mkBigramFile(filepath):
  with open('bigram.temp', 'w') as bigramFile:
    for line in open(filepath):
      line = line.strip().decode('utf-8')
      if len(line) <= 2:
        bigramFile.write(line.encode('utf-8') + '\n')
        continue
      for i in range(len(line) - 1):
        bigramFile.write('%s%s\n' % \
            (line[i].encode('utf-8'), line[i + 1].encode('utf-8')))

if __name__ == '__main__':
  mkBigramFile(sys.argv[1])
  for item in topN(sortSecWFreq('bigram.temp')):
    sys.stdout.write(item)
  os.remove('bigram.temp')
