#!/bin/sh
cut -f 1 $1 | sort | uniq | wc -l
