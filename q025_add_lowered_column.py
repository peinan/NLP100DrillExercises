#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-10-22

import sys

def addLoweredColumn(line):
  return line.lower()

if __name__ == '__main__':
  for line in open(sys.argv[1]):
    sys.stdout.write('%s\t%s' % (line.strip(), addLoweredColumn(line)))
