#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-12-16

import sys, CaboCha
from q052_morph_class import *
from q053_chunk import *

if __name__ == '__main__':
  for line in sys.stdin.readlines():
    newMorph = Chunk(line)
    for chunk in newMorph.getDepInfo():
      print 'src: %s, dst: %s, morphs: ' % (chunk['src'], chunk['dst']),
      for morph in chunk['morphs']:
        print morph['srf'],
      print
    print
