#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-10-07

import sys, re

def splitToWords(line):
  line = line.strip()
  line = line.replace(' ', '\n')
  line = re.sub(r'([\$\%\)\,\.])', r'\n\1', line)
  line = re.sub(r'([\(])', r'\1\n', line)
  return line


if __name__ == '__main__':
  for line in open(sys.argv[1]):
    print splitToWords(line)
    print
