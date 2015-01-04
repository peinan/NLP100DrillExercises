#!/bin/bash
for fn in work/english*.genia; do
  python q072_loadGeniaResult.py $fn ${fn%.genia}.pkl;
done
