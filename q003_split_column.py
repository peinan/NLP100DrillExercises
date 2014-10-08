#!/usr/bin/env python
#encoding:utf-8
#
# Author: Peinan ZHANG
#

import sys

def split_column(inFilePath):
  col1 = open('col1.txt', 'w')
  col2 = open('col2.txt', 'w')
  for line in open(inFilePath):
    line = line.rstrip()
    try:
      col_1, col_2 = line.split('\t')
    except:
      col_1 = line
      col_2 = ''
    col1.write('%s\n' % col_1)
    col2.write('%s\n' % col_2)
  col1.close()
  col2.close()


if __name__ == '__main__':
  split_column(sys.argv[1])
