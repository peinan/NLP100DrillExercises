#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-10-07

import sys

for line in open(sys.argv[1]):
  for sentence in line.strip().rstrip('.').split('. '):
    print sentence + '.'
