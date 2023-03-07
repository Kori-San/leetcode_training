#!/bin/bash

# https://leetcode.com/problems/word-frequency/

# Read from the file words.txt and output the word frequency list to stdout.
cat words.txt | tr '\n' ' ' | tr -s ' ' | sed 's/ $/\n/g' | sed 's/ /\n/g' | sort | uniq -c | sort -r | sed 's/^ *//g' | sed 's/\([0-9]*\)\(.*\)/\2 \1/g' | cut -c2-

# First we send the whole content of words.txt to stdout and redirect it with a pipe to the tr command
# We use tr and sed multiple times to put every word of the words.txt text in a single line
# We sort the output and make it uniq and count every occurence of the word
# We then adapt this last output to the one asked by the problem.
