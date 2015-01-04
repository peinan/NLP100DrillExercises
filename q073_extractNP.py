#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-01-04

import sys, pickle

if __name__ == '__main__':
  geniaResult = pickle.load(open(sys.argv[1]))
  aNP = []
  for sent in geniaResult:
    for tok in sent:
      if 'NP' not in tok['chk'] and len(aNP) > 0:
        print '# %s' % (' '.join(aNP))
        aNP = []
      elif 'NP' in tok['chk']:
        BIOs = tok['chk'].split('-')[0]
        if BIOs == 'B' and len(aNP) > 0:
          print '# %s' % (' '.join(aNP))
          aNP = []
          aNP.append(tok['w'])
          continue
        aNP.append(tok['w'])
