#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-12-12

import CaboCha, sys

def cabochaParse(sentence):
  c = CaboCha.Parser()
  tree = c.parse(sentence)
  return tree.toString(CaboCha.FORMAT_LATTICE)

if __name__ == '__main__':
  print cabochaParse(sys.stdin.readline())
  # print raw_input()
