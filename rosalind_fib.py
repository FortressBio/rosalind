#!/usr/bin/env python


##
#
# Solution to Rosalind problem: Rabbits and Recurrence Relations
#
# Given: Positive integers n≤40 and k≤5.
# Return: The total number of rabbit pairs that will be present after n months, 
#         if we begin with 1 pair and in each generation, every pair of 
#         reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
#
# http://rosalind.info/problems/fib/
#
##

import sys


with open(sys.argv[1], 'r') as fib_input:
	fib_input = fib_input.read()
	months, litter_size = fib_input.split(" ")
	months = int(months)
	litter_size = int(litter_size)

# First two entries in the sequence are 1 and 1.
count = 1
n1 = 1
n2 = 1
while count <= months - 2:
	n = n1 + (n2 * litter_size)
	n2 = n1
	n1 = n
	count += 1

print(n)