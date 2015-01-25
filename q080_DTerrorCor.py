#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-01-25

import sys

lines = sys.stdin.readlines()

# ref, pred
for line in lines:
  ref, pred = line.strip().split('\t')
  print '%s\t%s' % (ref, pred),
  if ref != pred:
    print '# Mistake!',
  print
