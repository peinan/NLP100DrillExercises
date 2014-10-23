#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2014-10-23

import sys, marshal
from q031_view_words_detail import mkList

if __name__ == '__main__':
  marshal.dump(mkList(), open(sys.argv[1], 'w'))
