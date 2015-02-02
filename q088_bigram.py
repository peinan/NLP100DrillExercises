#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-02-02

import sys
import pymongo
from pymongo import *

con = Connection('localhost', 27017)
db = con.nlp100_peinan
col = db.tweets

for data in col.find():
  pre_char = "<s>"
  bigrams = []
  for char in data["body"]:
    bigrams.append(pre_char+char)
    pre_char = char
    bigrams.append(pre_char+"</s>")
    data["bigram"] = bigrams
    col.save(data)
col.create_index([("bigram", ASCENDING)])
