#!/usr/bin/env python


##
#
# Solution to Rosalind problem: Translating RNA into Protein
#
# Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
# Return: The protein string encoded by s.
#
# http://rosalind.info/problems/prot/
#
##

import sys

# Codon-to-amino acid conversion. Stop codons do not return any text.
codon_table = { 'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V', 
				'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
				'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
				'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
				'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
				'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
				'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
				'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
				'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
				'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
				'UAA': '', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
				'UAG': '', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
				'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
				'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
				'UGA': '', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
				'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G' }

# Take an RNA sequence as input.
with open(sys.argv[1], 'r') as input:
	mrna = input.readline().rstrip()

# Separate the sequence into sets of three.
codons = [mrna[i:i+3] for i in range(0, len(mrna), 3)]

# Use the above table to translate codons into an amino acid sequence.
prot = "".join(codon_table.get(x, "[error]") for x in codons)

print(prot)