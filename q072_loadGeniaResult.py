#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-01-04

import sys, pickle

# def loadGeniaResult(line):
#   pass


if __name__ == '__main__':
  """Format
  doc = [sent_1, sent_2, ... , sent_n]
  sent = [tok_1, tok_2, ... , tok_n]
  tok_n = {'w': surface, 'lem': lemma, 'pos': POS, 'chk': chunk, \
      '-1': {'w': tok[n-1]['w'], 'pos': tok[n-1]['pos']}, \
      '+1': {'w': tok[n+1]['w'], 'pos': tok[n+1]['pos']}}
  """
  lines = open(sys.argv[1]).readlines()
  doc  = []
  sent = []
  for i in range(len(lines)):
    if lines[i] == '\n':
      if len(sent) == 0:
        continue
      doc.append(sent)
      continue
    cols = lines[i].strip().split('\t')

    # tok[i - 1]
    if lines[i - 1] != '\n':
      tok_before = {'w': sent[-1]['w'], 'pos': sent[-1]['pos']}
    else:
      tok_before = 'NONE'

    # tok[i + 1]
    if lines[i + 1] != '\n':
      cols_after = lines[i + 1].strip().split('\t')
      tok_after = {'w': cols_after[0], 'pos': cols_after[2]}
    else:
      tok_after = 'NONE'

    tok = {'w': cols[0], 'lem': cols[1], 'pos': cols[2], 'chk': cols[3], \
        '-1': tok_before, '+1': tok_after}

    sent.append(tok)

# print doc[0][0]
  pickle.dump(doc, open(sys.argv[2], 'w'))
