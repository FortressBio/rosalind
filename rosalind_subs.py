#!/usr/bin/env python


##
#
# Solution to Rosalind problem: Finding a Motif in DNA
#
# Given: Two DNA strings s and t (each of length at most 1 kbp).
# Return: All locations of t as a substring of s.
#
##

import sys

# Input is understood to consist of two DNA sequences stored in a .txt file. Script finds
# all of the places a substring exists within a larger string.

# DNA sequences taken as input from command line and cleaned up
with open(sys.argv[1], 'r') as input:
	lines = input.readlines()
s = lines[0].rstrip()
t = lines[1].rstrip()

locations = ""
# Iterate over s, check to see whether t exists at a given location, store the location data
# in the asked-for format
for i in range(len(s)):
	if s[i:i + len(t)] == t:
		locations = locations + " " + str(i+1)
print(locations)
