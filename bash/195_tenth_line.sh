#!/bin/bash

# https://leetcode.com/problems/tenth-line/

# Read from the file file.txt and output the tenth line to stdout.

# `sed` is a stream editor. `10!d` means delete all lines except the 10th line.
sed '10!d' file.txt
