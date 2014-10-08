#!/usr/bin/env python
#encoding:utf-8
#
# Author: Peinan ZHANG
#

import sys

def line_count(inFilePath):
  print sum([ 1 for line in open(inFilePath) ])

if __name__ == '__main__':
  line_count(sys.argv[1])
