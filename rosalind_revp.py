#!/usr/bin/env python


##
#
# Solution to Rosalind problem: Locating Restriction Sites
#
# Given: Given: A DNA string of length at most 1 kbp in FASTA format.
# Return: The position and length of every reverse palindrome in the string having 
#         length between 4 and 12. You may return these pairs in any order.
#
# http://rosalind.info/problems/revp/
#
##

import sys

# Given a DNA sequence, return the reverse complement.
def rev_comp(seq):
	seq_rev = seq[::-1]
	seq_comp = ""
	complements = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
	for i in seq_rev:
		seq_comp = "".join(complements.get(base, base) for base in seq_rev)
		return(seq_comp)

# Input will consist of a header line and a DNA sequence. Omit the header line,
# get the DNA sequence lines and consolidate them into one line.
sequence = ""
with open(sys.argv[1], 'r') as input:
	for line in input:
		if not line.startswith(">"):
			sequence = sequence+line.rstrip()

# Using each base as a starting point, check lengths of DNA ranging from 4 to
# 12 base pairs in length to see whether the reverse complement is identical.
# When a reverse palindrome is found, print its start point and length.
for i in range(len(sequence)-3):
	for w in range(4, 13):
		t = rev_comp(sequence[i:i+w])
		if t == sequence[i:i+w]:
			print(str(i+1)+" "+str(len(t)))