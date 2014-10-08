#!/usr/bin/python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-09-08

import sys, re

def extractRTcomment(filePath):
  # there's no data of tweet commend to RT.
  # so this function will extract RT context.
  RTcommnet = re.compile(ur'.*RT @[a-zA-Z0-9_]+: ')
  for line in open(filePath):
    line = line.decode('utf-8')
    if RTcommnet.match(line):
      print RTcommnet.sub('', line).encode('utf-8')

if __name__ == '__main__':
  extractRTcomment(sys.argv[1])
