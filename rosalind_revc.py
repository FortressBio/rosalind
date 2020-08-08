#!/usr/bin/env python


## 
#
# Solution to Rosalind problem: Complementing a Strand of DNA
#
# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement s^c of s.
#
##

import sys

# DNA sequence taken as input from command line
with open(sys.argv[1], 'r') as input:
    seq = input.read()

# Read the DNA sequence in reverse and create a complement strand
seq_rev = seq[::-1]
seq_comp = ""
for i in seq_rev:
	if i == "A":
		seq_comp = seq_comp + "T"
	if i == "T":
		seq_comp = seq_comp + "A"
	if i == "C":
		seq_comp = seq_comp + "G"
	if i == "G":
		seq_comp = seq_comp + "C"

print(seq_comp)