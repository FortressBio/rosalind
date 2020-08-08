#!/usr/bin/env python


## 
#
# Solution to Rosalind problem: Counting Point Mutations
#
# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
# Return: The Hamming distance d_H(s,t).
#
##

import sys

# Input is understood to consist of two DNA sequences stored in a .txt file. Script calculates
# the number of mismatched nucleotides given two sequences of equal length.

# DNA sequences taken as input from command line
with open(sys.argv[1], 'r') as input:
	lines = input.readlines()

counter = 0

# Iterate over positions and check to see whether sequences differ at that position. Tally up 
# number of differences.
for i in range(len(lines[0])):
	if lines[0][i] != lines[1][i]:
		counter += 1
print(counter)