#!/usr/bin/python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-09-11

import sys, re

def extractUsers(filePath):
  user = re.compile(ur'@[a-zA-Z0-9_]+')
  users = [ user.findall(line) for line in open(filePath) \
            if len(user.findall(line)) != 0 ]
  return users

if __name__ == '__main__':
  users = extractUsers(sys.argv[1])
  for user in users:
    print user
