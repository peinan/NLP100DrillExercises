#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-10-07

import sys

def splitToWords(line):
  return line.strip().split()


if __name__ == '__main__':
  for line in open(sys.argv[1]):
    words = splitToWords(line)
    for word in words:
      print word
    print
