#!/usr/bin/env python


##
#
# Solution to Rosalind problem: Computing GC Content
#
# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the 
#         GC-content of that string. Rosalind allows for a default error of 0.001
#          in all decimal answers unless otherwise stated.
#
# http://rosalind.info/problems/gc/
#
##

import sys
from Bio import SeqIO

seq_dict = {}
GC_count = 0
# Input, read from command line, is in fasta format. Biopython used to parse fasta.
with open(sys.argv[1], 'r') as input:
	for seq_record in SeqIO.parse(input, "fasta"):
		# GC content for each sequence is tallied.
		for i in seq_record.seq:
			if i == 'G' or i == 'C':
				GC_count += 1
		# Dictionary consists of fasta IDs and GC content.
		seq_dict[seq_record.id] = GC_count/len(seq_record.seq)
		GC_count = 0

# Find the entry with the highest GC content and print.
max_GC = max(seq_dict, key=seq_dict.get)
print(max_GC)
print(seq_dict[max_GC] * 100)