#!/usr/bin/env python
#encoding:utf-8
#
# Author:   Peinan ZHANG
#

import sys
for line in open(sys.argv[1]):
	line = (line.strip()).replace('\t', ' ')
	print line
