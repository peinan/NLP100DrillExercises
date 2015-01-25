#!/bin/bash
sent=$1
echo $sent | python q022_convert_to_oneLine_ver3.py | ./geniatagger 
