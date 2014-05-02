#!/usr/bin/env python
#encoding:utf-8
#
# Author:   Peinan ZHANG
#

import sys
address = {}
for line in open(sys.argv[1]):
	address[line.split('\t')[0] + '\n'] = line.split('\t')[1]
	open('col1.txt', 'w').writelines(address.keys())
	open('col2.txt', 'w').writelines(address.values())
