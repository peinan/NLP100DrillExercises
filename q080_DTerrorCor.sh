#!/bin/bash
# sent=$1
sent=$(cat -)
# echo $sent
echo $sent \
  | python q022_convert_to_oneLine_ver3.py \
  | ./geniatagger-3.0.1/geniatagger \
  | python q080_mkFeature.py \
  | classias-tag -st -m english.model -r \
  | python q080_DTerrorCor.py

