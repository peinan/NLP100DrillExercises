#!/bin/sh
sort $1 | uniq -c | sort -n -r
