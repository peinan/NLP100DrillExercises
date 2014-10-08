#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-09-11

import sys, re

def extractParaphrase(line):
  paraSet = re.compile(ur'([一-龠]+)(（|\()([a-zA-Z_\-0-9]+)(）|\))')
  m = paraSet.search(line)
  if m != None:
    return m.groups() 

def openFile(filePath):
  for line in open(filePath):
    line = line.decode('utf-8')
    groups = extractParaphrase(line)
    if groups != None:
      print groups[0], groups[2]

if __name__ == '__main__':
  openFile(sys.argv[1])
