#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-10-07

import sys, re

def convert2oneLine(line):
  sentenceBoundary = re.compile(r'\. ([A-Z])')
  line = line.strip()
  return re.sub(r'\. ([A-Z])', r'.\n\1', line) 

if __name__ == '__main__':
  for line in sys.stdin.readlines():
    print convert2oneLine(line.strip())
