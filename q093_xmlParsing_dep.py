#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-02-05

from lxml import objectify as oby

def getDeps(sentNo=1, tokNo=4):
  sentNo = str(sentNo)
  tokNo = str(tokNo)
  root = oby.parse('work/corenlp_output.xml')

  deps = []
  for sElem in root.iter('sentence'):
    if sElem.get('id') == sentNo:
      for dElem in sElem.iter('dep'):
        if dElem.governor.get('idx') == tokNo:
          deps.append(dElem.dependent.text)

  return deps


def getArgs():
  import argparse

  parser = argparse.ArgumentParser()

  parser.add_argument('-s', dest='sentNo', default=1)
  parser.add_argument('-t', dest='tokNo', default=4)

  return parser.parse_args()


if __name__ == '__main__':
  from pprint import pprint
  args = getArgs()
  pprint(getDeps(args.sentNo, args.tokNo))

