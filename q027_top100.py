#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-10-23

import sys

def topN(freqDict, N=100, c=True):
  from q010_sort_second_wFreq import sortSecWFreq
  count = 0
  return_list = []
  for k, v in sorted(freqDict.items(), key=lambda x: x[1], reverse=True):
    if count < N:
      if c == True:
        return_list.append('%3d %s\n' % (v, k.encode('utf-8')))
      if c == False:
        return_list.append('%s\n' % k.encode('utf-8'))
      count += 1
    else:
      break
  return return_list

if __name__ == '__main__':
  for item in topN(sortSecWFreq(sys.argv[1])):
    sys.stdout.write(item)

