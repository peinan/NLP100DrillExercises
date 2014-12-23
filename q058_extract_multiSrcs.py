#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-12-16

import sys, CaboCha
from q053_chunk import *

def extractMultiSrcs(sentence):
  newChunk = Chunk(sentence)
  chunks = newChunk.getDepInfo()

  """Data Format
  chunks  = [ chunk_1, chunk_2, ... , chunk_n ]
  chunk_n = { 'src': int, 'dst': int, 'morphs':[morph_1, ... , morph_n] }
  morph_n = { 'pos': str, 'pos1': str, 'srf': str }
  ---
  dst_to = { 0: [strs], 1: [strs], ... , n: [strs] }
  [strs] = [ <src>, dst_to_1, ... , dst_to_n ]
  """

  dsts_to = defaultdict(lambda: [])
  
  for chunk in chunks:
    if chunk['dst'] == -1:
      dsts_to[chunk['src']].append(['<root>'])
    else:
      dsts_to[chunk['src']].append([ morph['srf'] for morph in chunk['morphs'] ])
    dsts_to[chunk['dst']].append([ morph['srf'] for morph in chunk['morphs'] ])

  return { k:v for k, v in dsts_to.items() if len(v) >= 3 }


if __name__ == '__main__':
  dsts_to = extractMultiSrcs(sys.stdin.readline())
  for k, vs in dsts_to.items():
    print 'src: %d' % k
    for v in vs:
      for s in v: print s,
      print ' | ',
    print
