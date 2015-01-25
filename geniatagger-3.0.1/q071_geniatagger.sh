#!/bin/bash
for fn in ~/NLP100DrillExercises/corpus/english*.txt; do
  python q022_convert_to_oneLine_ver2.py $fn | ./geniatagger > ${fn%.txt}.genia;
  echo ${fn}' is done.'
done
