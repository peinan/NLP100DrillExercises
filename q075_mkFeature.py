#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-01-04

"""Features
hw      = (末尾の単語)
hpos    = (末尾の品詞)
hw|hpos = (末尾の単語)|(末尾の品詞)
fw      = (先頭の単語)
fpos    = (先頭の品詞)
fw|fpos = (先頭の品詞)|(先頭の単語)
w[0]    = (名詞句の単語列)
w[-1]   = (名詞句の１語前の単語)
pos[-1] = (名詞句の１語前の品詞)
w[1]    = (名詞句の１語後の単語)
pos[1]  = (名詞句の１語後の品詞)
"""

import sys, pickle

def printLine(aNP, feature_of):
  import re
  formatFeature = '\t'.join(['%s=%s' % (k, v) for k, v in feature_of.items()])
  if re.match(r'^[aA]n?$', aNP[0]):
    print '# %s\nA\t%s' % (' '.join(aNP), formatFeature)
  elif re.match(r'^[tT]he$', aNP[0]):
    print '# %s\nTHE\t%s' % (' '.join(aNP), formatFeature)
  else:
    print '# %s\nNONE\t%s' % (' '.join(aNP), formatFeature)


def mkFeatures(NPtokens):
  feature_of = {}
  try:
    feature_of['hw'] = NPtokens[-1]['w']
    feature_of['hpos'] = NPtokens[-1]['pos']
    feature_of['hw|hpos'] = '%s|%s' % (feature_of['hw'], feature_of['hpos'])
    if len(NPtokens) != 1:
      feature_of['fw'] = NPtokens[1]['w'] if NPtokens[1]['pos'] == 'DT' else NPtokens[0]['w']
      feature_of['fpos'] = NPtokens[1]['pos'] if NPtokens[1]['pos'] == 'DT' else NPtokens[0]['pos']
    else:
      feature_of['fw'] = NPtokens[0]['w']
      feature_of['fpos'] = NPtokens[0]['pos']
    feature_of['fw|fpos'] = '%s|%s' % (feature_of['fw'], feature_of['fpos'])
    feature_of['w[0]'] = ' '.join([tok['w'] for tok in NPtokens if tok['pos'] != 'DT'])
    feature_of['w[-1]'] = NPtokens[0]['-1']['w'] if NPtokens[0]['-1'] != 'NONE' else 'NONE'
    feature_of['pos[-1]'] = NPtokens[0]['-1']['pos'] if NPtokens[0]['-1'] != 'NONE' else 'NONE'
    feature_of['w[1]'] = NPtokens[-1]['+1']['w'] if NPtokens[-1]['+1'] != 'NONE' else 'NONE'
    feature_of['pos[1]'] = NPtokens[-1]['+1']['w'] if NPtokens[-1]['+1'] != 'NONE' else 'NONE'
  except Exception as e:
    print NPtokens
    print 'type: %s' % str(type(e))
    print 'args: %s' % str(e.args)
    print 'message: %s' % e.message
    print 'error: %s' % str(e)
    sys.exit(-1)
  
  return feature_of 


def extractNPs(geniaResult):
  aNP = []
  NPtokens = []
  for sent in geniaResult:
    for tok in sent:
      if 'NP' not in tok['chk'] and len(aNP) > 0:
        feature_of = mkFeatures(NPtokens)
        printLine(aNP, feature_of)
        aNP = []
        NPtokens = []
      elif 'NP' in tok['chk']:
        BIOs = tok['chk'].split('-')[0]
        if BIOs == 'B' and len(aNP) > 0:
          feature_of = mkFeatures(NPtokens)
          printLine(aNP, feature_of)
          aNP = []
          NPtokens = []
          aNP.append(tok['w'])
          NPtokens.append(tok)
          continue
        aNP.append(tok['w'])
        NPtokens.append(tok)


if __name__ == '__main__':
  geniaResult = pickle.load(open(sys.argv[1]))
  extractNPs(geniaResult)
