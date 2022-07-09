#!/bin/bash

# https://leetcode.com/problems/word-frequency/

# Read from the file words.txt and output the word frequency list to stdout.
cat words.txt | tr '\n' ' ' | tr -s ' ' | sed 's/ $/\n/g' | sed 's/ /\n/g' | sort | uniq -c | sort -r | sed 's/^ *//g' | sed 's/\([0-9]*\)\(.*\)/\2 \1/g' | cut -c2-
