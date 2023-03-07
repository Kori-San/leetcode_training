#!/bin/bash

# https://leetcode.com/problems/transpose-file/

# Read from the file file.txt and print its transposed content to stdout.

# Assigning the value of file.txt to the variable file.
file="file.txt"

# Getting the number of columns in the file.
columns=$(head -n1 "${file}" | wc -w)

# The above code is printing the contents of the file in a columnar format.
for i in $(seq 1 ${columns}); do
    cat "${file}" | cut "-d" " " "-f${i}" | tr "\n" " " | sed "s/ $/\n/g"
done
