#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG

import sys

def tailN(filePath, N):
  fileLine = open(filePath).readlines()
  for i in range(-(N - len(fileLine)), len(fileLine)):
    sys.stdout.write(fileLine[i])

if __name__ == '__main__':
  tailN(sys.argv[1], int(sys.argv[2]))
