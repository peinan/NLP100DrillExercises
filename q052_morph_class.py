#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-12-12

import CaboCha, sys
from q051_cabocha import cabochaParse

class Morph:
  def __init__(self, sentence):
    self.sentence = sentence
    self.cabochaResult = cabochaParse(sentence)
    self.parsedMorphs = []
    for line in self.cabochaResult.splitlines():
      if line[0] != '*' and line.strip() != 'EOS':
        srf, result = line.split('\t')
        results = result.split(',')
        base = results[6]
        pos  = results[0]
        pos1 = results[1]
        self.parsedMorphs.append(\
            {'srf':srf, 'base':base, 'pos':pos, 'pos1':pos1})

  def getParsedMorphs(self):
    return self.parsedMorphs

  def getSurfaces(self):
    return [ morph['srf'] for morph in self.parsedMorphs ]

  def getBases(self):
    return [ morph['base'] for morph in self.parsedMorphs ]

  def getPoses(self):
    return [ morph['pos'] for morph in self.parsedMorphs ]

  def getPos1s(self):
    return [ morph['pos1'] for morph in self.parsedMorphs ]

  def getCabochaResult(self):
    return self.cabochaResult


if __name__ == '__main__':
  newMorph = Morph(sys.stdin.readline())
  print newMorph.getCabochaResult()
  print newMorph.getParsedMorphs()
  print newMorph.getSurfaces()
  print newMorph.getPoses()
  print newMorph.getPos1s()
  print newMorph.getBases()
