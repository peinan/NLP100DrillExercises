#!/usr/bin/env python
#encoding:utf-8
#
# Author: Peinan ZHANG
#

import sys

def replace_tab_space(inFilePath):
  for line in open(inFilePath):
    sys.stdout.write(line.replace('\t', ' '))

if __name__ == '__main__':
  replace_tab_space(sys.argv[1])
