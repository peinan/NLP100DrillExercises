#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-02-05

from lxml import objectify as oby

def getLemmas(sentNo=1):
  sentNo = str(sentNo)
  root = oby.parse('work/corenlp_output.xml')
  for sElem in root.iter('sentence'):
    if sElem.get('id') == sentNo:
      for tElem in sElem.iter('token'):
        print tElem.lemma.text


def getArgs():
  import argparse
  parser = argparse.ArgumentParser()

  parser.add_argument('-s', dest='sentNo', default=1)

  return parser.parse_args()


if __name__ == '__main__':
  args = getArgs()
  getLemmas(args.sentNo)
