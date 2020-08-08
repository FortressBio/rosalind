#!/usr/bin/env python


## 
#
# Solution to Rosalind problem: Counting DNA Nucleotides
#
# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
#
##


import sys

# DNA sequence taken as input from command line
with open(sys.argv[1], 'r') as input:
    DNA = input.read()

a_count = 0
t_count = 0
g_count = 0
c_count = 0

# Sequence is read and nucleotide content is tallied up
for i in DNA:
	if i == "A":
		a_count += 1
	elif i =="T":
		t_count += 1
	elif i == "G":
		g_count += 1
	elif i == "C":
		c_count += 1

print(a_count, c_count, g_count, t_count)