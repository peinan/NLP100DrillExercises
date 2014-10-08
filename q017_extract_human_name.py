#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-09-12

import sys, re

def extractName(line):
  raw_kanji = ur'[一-龠]+'
  raw_hira  = ur'[ぁ-ゞ]+'
  raw_kata  = ur'[ァ-ヾ]+'
  raw_call  = ur'(さん|ちゃん|くん|君)'

  namePattern = re.compile(ur'(%s|%s|%s)%s' % \
                           (raw_kanji, raw_hira, raw_kata, raw_call))

  return re.findall(namePattern, line)


if __name__ == '__main__':
  for line in open(sys.argv[1]):
    line = line.strip().decode('utf-8')
    names = extractName(line)
    # print names
    if len(names) != 0:
      for name in names:
        name_str = ''
        for char in name:
          name_str += char
        sys.stdout.write('%s\n' % name_str.encode('utf-8'))

