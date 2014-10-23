#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-10-23

import sys

def mkList(filepath='data/inflection.table.txt'):
  wordsList = []
  for line in open(filepath):
    cols = line.strip().split('|')
    wordsList.append((cols[0], cols[1], cols[6]))
  return wordsList


def searchWord(query, wordsList):
  return [ item for item in wordsList if query == item[0] ]


if __name__ == '__main__':
  wordsList = mkList()
  print 'enter "exit" to quit'
  while True:
    word = raw_input('search for what? > ')
    if word == 'exit':
      print 'good bye!\n'
      break
    searchResult = searchWord(word, wordsList)
    if len(searchResult) > 1:
      seeAll = raw_input('more than 1 result. want see all? [Y/N] > ')
      if seeAll == 'Y' or seeAll == 'y':
        print
        for item in searchResult:
          sys.stdout.write('query:"%s" POS:"%s" original:"%s"\n' \
              % (item[0], item[1], item[2]))
      else:
        print
        for item in searchResult:
          sys.stdout.write('query:"%s" POS:"%s" original:"%s"\n' \
              % (item[0], item[1], item[2]))
          break
    else:
      print
      for item in searchResult[0]:
        sys.stdout.write('query:"%s" POS:"%s" original:"%s"\n' \
            % (item[0], item[1], item[2]))
    print
