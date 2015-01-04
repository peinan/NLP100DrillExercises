#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-01-04

import sys
from geniatagger import *
from q022_convert_to_oneLine_ver2 import convert2oneLine


if __name__ == '__main__':
  tagger = GeniaTagger('/home/peinan/geniatagger-3.0.1/geniatagger')
  for line in sys.stdin.readlines():
    lines = convert2oneLine(line.strip()).split('\n')
    for l in lines:
      print tagger.parse(l)
