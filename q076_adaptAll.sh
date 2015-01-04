#!/bin/bash
for fn in work/english*.pkl; do
  python q075_mkFeature.py $fn > ${fn%.pkl}.f;
done
