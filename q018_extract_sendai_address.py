#!/usr/bin/env python
# coding:utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-09-30

import sys, re

def loadSendaiAddress(adrFilePath):
  from collections import defaultdict
  sendaiAddress = defaultdict(lambda: [])
  for line in open(adrFilePath):
    line = line.strip().decode('utf-8')
    cols = line.split()
    if len(cols) != 2:
      continue
    glb, loc = cols
    if u'仙台市' in glb:
      # print glb.encode('utf-8')
      pref, zone = glb.split(u'仙台市')
      # print zone.encode('utf-8')
      sendaiAddress[zone].append(loc)

  return sendaiAddress


def extractSendaiAddress(line, addressDict):
  locations = []
  for location in addressDict.values():
    locations += location
  locations += addressDict.keys()
  
  sendaiPtn = re.compile(ur'(%s)' % ('|'.join(locations)))
  return re.findall(sendaiPtn, line)


if __name__ == '__main__':
  adrDict = loadSendaiAddress(sys.argv[2])
  for line in open(sys.argv[1]):
    line = line.strip().decode('utf-8')
    sendaiAdrs = extractSendaiAddress(line, adrDict)
    # print sendaiAdrs
    if len(sendaiAdrs) != 0:
      for sendaiAdr in sendaiAdrs:
        print sendaiAdr
