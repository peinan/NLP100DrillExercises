#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-12-16

import sys, CaboCha
from q053_chunk import *

def extractNounOnVerb(sentence):
  newChunk = Chunk(sentence)
  chunks = newChunk.getDepInfo()
  SrcDst_pairs = []
  for chunk in chunks:
    if chunk['dst'] == -1:
      SrcDst_pairs.append((\
          [ morph['srf'] for morph in chunk['morphs'] ], ['<root>']))
      continue
    if '名詞' in [ morph['pos'] for morph in chunk['morphs'] ] and\
      '動詞' in [ morph['pos'] for morph in chunks[chunk['dst']]['morphs'] ]:
      SrcDst_pairs.append((\
          [ morph['srf'] for morph in chunk['morphs'] ],\
          [ morph['srf'] for morph in chunks[chunk['dst']]['morphs'] ]))

  return SrcDst_pairs

if __name__ == '__main__':
  pairs = extractNounOnVerb(sys.stdin.readline())
  for pair in pairs:
    for morph in pair[0]:
      print morph,
    print '\t',
    for morph in pair[1]:
      print morph,
    print
