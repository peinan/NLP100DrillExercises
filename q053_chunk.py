#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-12-14

import sys, CaboCha
from q052_morph_class import Morph
from collections import *

class Chunk(Morph):
  """morphs, dst, srcs"""

  def __init__(self, sentence):
    Morph.__init__(self, sentence)
    self.sentDeps = []
    self.depInfo_of = {}
    self.depInfo_of['morphs'] = []
    for line in self.cabochaResult.splitlines():
      if line[:2].startswith('* ') or line.strip() == 'EOS':
        if len(self.depInfo_of['morphs']) != 0:
          self.sentDeps.append(self.depInfo_of)
          self.depInfo_of = {}
          self.depInfo_of['morphs'] = []
          if line.strip() == 'EOS':
            continue
        self.depInfo = line.split(' ')
        self.depInfo_of['src'] = int(self.depInfo[1])
        self.depInfo_of['dst'] = int(self.depInfo[2][:-1])
      elif not line[:2].startswith('* '):
        srf, result = line.split('\t')
        results = result.split(',')
        base = results[6]
        pos  = results[0]
        pos1 = results[1]
        self.depInfo_of['morphs'].append(\
            {'srf':srf, 'base':base, 'pos':pos, 'pos1':pos1})

  def getDepInfo(self):
    return self.sentDeps


if __name__ == '__main__':
  newMorph = Chunk(sys.stdin.readline())
  print newMorph.getCabochaResult()
  for chunk in newMorph.getDepInfo():
    print 'src: %s, dst: %s, morphs: ' % (chunk['src'], chunk['dst']),
    for morph in chunk['morphs']:
      print morph['srf'],
    print
