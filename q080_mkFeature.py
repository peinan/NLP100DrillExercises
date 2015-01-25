#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-01-25

import sys, pickle
from q072_loadGeniaResult import loadGeniaResult
from q075_mkFeature import *

geniaLines = sys.stdin.readlines()
doc = loadGeniaResult(geniaLines)
extractNPs(doc)
