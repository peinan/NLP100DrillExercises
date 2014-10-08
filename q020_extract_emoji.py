#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-10-02

import sys, re

def extract_emoji(text):
  emojiPtn = re.compile(ur'([\(（])(.+?)([\)|）])')
  kanjiPtn = re.compile(ur'[一-龠]+')
  result   = re.match(emojiPtn, text)
  if re.match(kanjiPtn, result.group(1)) != None:
    return result


if __name__ == '__main__':
  for line in open(sys.argv[1]):
    line = line.strip().decode('utf-8')
    emojis = extract_emoji(line)
    for emoji in emojis:
      print ''.join(emoji).encode('utf-8')
