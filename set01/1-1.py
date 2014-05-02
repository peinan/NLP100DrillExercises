#!/usr/bin/env python
#encoding:utf-8
#
# Author:   Peinan ZHANG
#

import sys
print sum(1 for line in open(sys.argv[1], 'r'))
