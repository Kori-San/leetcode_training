#!/bin/bash

# https://leetcode.com/problems/transpose-file/

# Read from the file file.txt and print its transposed content to stdout.
file="file.txt"
columns=$(head -n1 "${file}" | wc -w)
for i in $(seq 1 ${columns}); do
    cat "${file}" | cut "-d" " " "-f${i}" | tr "\n" " " | sed "s/ $/\n/g"
done
