#!/bin/bash

# https://leetcode.com/problems/valid-phone-numbers/

# Read from the file file.txt and output all valid phone numbers to stdout.
grep -oP "^(\([0-9]{3}\) |([0-9]{3}-)){1}([0-9]{3}-[0-9]{4}){1}$" file.txt
