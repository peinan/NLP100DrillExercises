#!/usr/bin/env python
#coding:utf-8
#
# Author: Peinan ZHANG
#

import sys
col1 = open(sys.argv[1], "r").readlines()
col2 = open(sys.argv[2], "r").readlines()
pasted_file = open("col1_col2.txt", "w")

pasted = []
if len(col1) != len(col2):
  print >>sys.stderr, "Total lines are not same."
else:
  for line_no in range(len(col1)):
    col1[line_no] = col1[line_no].strip()
    pasted.append("%s\t%s" % (col1[line_no], col2[line_no]))

pasted_file.writelines(pasted)