#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-12-06

import sys, MeCab, pickle, argparse
from q042_extract_verbs import extractVerbs
from q043_extract_verbBases import extractVerbBases
from q044_extract_SahenNoun import extractSahenNoun
from q045_extract_AnoB import extractAnoBs
from q046_extract_chainNoun import findLongestNoun

if __name__ == '__main__':
  sentences = pickle.load(open('mecab.result'))

  parser = argparse.ArgumentParser(description='Process some Japanese sentences')
  parser.add_argument('-v', '--verbs', dest='arg_verbs',\
      action='store_true', default='false',\
      help='extract all verbs in the sentences')
  parser.add_argument('-b', '--verb-bases', dest='arg_verbBases',\
      action='store_true', default='false',\
      help='extract all bases of verbs in the sentences')
  parser.add_argument('-s', '--sahen-noun', dest='arg_sahenNoun',\
      action='store_true', default='false',\
      help='extract all sahen nouns in the sentences')
  parser.add_argument('-n', '--noConj-noun', dest='arg_noConjNoun',\
      action='store_true', default='false',\
      help='extract all "no" conjuncted noun in the sentences')
  parser.add_argument('-c', '--chain-noun', dest='arg_chainNoun',\
      action='store_true', default='false',\
      help='extract all chain noun in the sentences')
  args = parser.parse_args()

  if not args.arg_verbs or not args.arg_verbBases or not args.arg_sahenNoun or\
      not args.arg_noConjNoun or not args.arg_chainNoun:
    parser.print_help()
    sys.exit(-1)

  for sentence in sentences:
    if args.arg_verbs:
      print '\nExtracting All Verbs'
      print '-'*30
      verbs = extractVerbs(sentence)
      for verb in verbs:
        print verb.decode('utf-8')
    if args.arg_verbBases:
      print '\nExtracting All Verbs\' Bases'
      print '-'*30
      verbBases = extractVerbBases(sentence)
      for verbBase in verbBases:
        print verbBase.decode('utf-8')
    if args.arg_sahenNoun:
      print '\nExtracting All Sahen Nouns'
      print '-'*30
      sahenNouns = extractSahenNoun(sentence)
      for sahenNoun in sahenNouns:
        print sahenNoun.decode('utf-8')
    if args.arg_noConjNoun:
      print '\nExtracting All NO-conjuncted Nouns'
      print '-'*30
      noConjNouns = extractAnoBs(sentence)
      for noConjNoun in noConjNouns:
        print noConjNoun.decode('utf-8')
    if args.arg_chainNoun:
      print '\nExtracting All Chain Noun'
      print '-'*30
      chainNouns = findLongestNoun(sentence)
      for chainNoun in chainNouns:
        print chainNoun.decode('utf-8')
