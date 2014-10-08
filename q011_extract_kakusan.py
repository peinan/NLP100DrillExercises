#!/usr/bin/python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-09-08

import sys

def extractKakusan(filePath):
  for line in open(filePath):
    line = line.decode('utf-8')
    if u'拡散希望' in line:
      sys.stdout.write(line.encode('utf-8'))

if __name__ == '__main__':
  extractKakusan(sys.argv[1])
