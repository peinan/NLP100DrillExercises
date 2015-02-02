#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-01-25

import sys

lines = sys.stdin.readlines()
NPlines = open('NPs.txt').readlines()

print
print 'NP\tREF\tPRED'
print '-'*30
for i in range(len(lines)):
  ref, pred = lines[i].strip().split('\t')
  print '%s\t%s\t%s' % (NPlines[i].strip(), ref, pred),
  if ref != pred:
    print '# Mistake!',
  print
 
