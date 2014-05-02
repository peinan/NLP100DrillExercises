#!/usr/bin/env python
#coding:utf-8
#
# Author: Peinan ZHANG
#

text = {}
for line in open("address.txt", "r"):
  fore, rear = line.split("\t")
  text[fore] = rear

for k, v in sorted(text.items(), key = lambda x: x[1], reverse = True):
  print k, v