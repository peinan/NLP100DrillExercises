#!/bin/sh
# sed -e 's/<C-v><tab>/ /g' address.txt
sed -e 's/  / /g' address.txt
# cat address.txt | tr '\t' ' '
# expand -t 1 address.txt
