#!/usr/bin/python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-09-08

import sys

def extractEndNau(filePath):
  for line in open(filePath):
    line = line.strip().decode('utf-8')
    if line[-2:] == u'なう':
      sys.stdout.write('%s\n' % line.encode('utf-8'))

if __name__ == '__main__':
  extractEndNau(sys.argv[1])
