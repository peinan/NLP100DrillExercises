#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-01-04

import sys, pickle

def printLine(aNP):
  import re
  if re.match(r'^[aA]n?$', aNP[0]):
    print '# %s\nA' % (' '.join(aNP))
  elif re.match(r'^[tT]he$', aNP[0]):
    print '# %s\nTHE' % (' '.join(aNP))
  else:
    print '# %s\nNONE' % (' '.join(aNP))


if __name__ == '__main__':
  geniaResult = pickle.load(open(sys.argv[1]))
  aNP = []
  for sent in geniaResult:
    for tok in sent:
      if 'NP' not in tok['chk'] and len(aNP) > 0:
        printLine(aNP)
        aNP = []
      elif 'NP' in tok['chk']:
        BIOs = tok['chk'].split('-')[0]
        if BIOs == 'B' and len(aNP) > 0:
          printLine(aNP)
          aNP = []
        aNP.append(tok['w'])
    if 'NP' in tok['chk'] and len(aNP) > 0:
      printLine(aNP)
    aNP = []
    
