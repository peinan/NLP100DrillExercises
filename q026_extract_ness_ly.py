#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-10-22

import sys, re

def extractNessLy(line):
  re_nessly = re.compile(r'.*(ly$|ness$)')
  if re_nessly.match(line):
    return line
  return None

if __name__ == '__main__':
  for line in open(sys.argv[1]):
    if extractNessLy(line) != None:
      print line
