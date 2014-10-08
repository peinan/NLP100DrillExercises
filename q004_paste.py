#!/usr/bin/env python
#coding: utf-8
#
# Author: Peinan ZHANG

import sys

def paste(filePath1, filePath2):
  totalLines = sum([ 1 for line in open(filePath1) ])
  file1, file2 = open(filePath1), open(filePath2)
  for i in range(totalLines):
    print '%s\t%s' % (file1.readline().strip(), file2.readline())

if __name__ == '__main__':
  paste(sys.argv[1], sys.argv[2])
