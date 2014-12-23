#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-12-22

import sys

def graphvizRelation():
  dot = open('q060.dot', 'w')
  dot.write('digraph "g" {\n')
  for line in sys.stdin:
    items = line.strip().split('\t')
    if len(items) > 1:
      dot.write('\t"%s" -> "%s" ;\n' % (items[0], items[1]))
  dot.write('}')

if __name__ == '__main__':
  graphvizRelation()
