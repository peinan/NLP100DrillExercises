#!/usr/bin/python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-09-11

import re, sys

def replaceUsersLink(filePath):
  userRe = re.compile(r'(@([a-zA-Z0-9_]+)):')
  # don't forget 'r' in the method re.sub
  return [ userRe.sub(r'<a href="https://twitter.com/#!/\2">\1</a>', line)\
           for line in open(filePath) ]

if __name__ == '__main__':
  replaced = replaceUsersLink(sys.argv[1])
  for line in replaced:
    print line
