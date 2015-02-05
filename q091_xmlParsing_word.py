#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-02-05

from lxml import objectify as oby

def sentTokSearch(sentNo=2, tokNo=5):
  sentNo = str(sentNo)
  tokNo  = str(tokNo)
  root = oby.parse('work/corenlp_output.xml')
  for sElem in root.iter('sentence'):
    if sElem.get('id') == sentNo:
      for tElem in sElem.iter('token'):
        if tElem.get('id') == tokNo:
          print tElem.word.text


def getArgs():
  parser = argparse.ArgumentParser()

  parser.add_argument('-s', dest='sentNo', default=2)
  parser.add_argument('-t', dest='tokNo', default=5)

  return parser.parse_args()


if __name__ == '__main__':
  import sys, argparse
  args = getArgs()
  sentTokSearch(args.sentNo, args.tokNo)

