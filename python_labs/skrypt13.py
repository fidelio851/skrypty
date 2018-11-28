#!/usr/bin/python

import random

matrix1 = [[random.randrange(100) for i in range (8)] for j in range (8)]
matrix2 = [[random.randrange(100) for i in range (8)] for j in range (8)]

def iloczyn(m1, m2):
	m3 = [[0 for i in range (128)] for j in range (128)]
	for i in range(len(m1)):
	   # iterate through columns of Y
	   for j in range(len(m2[0])):
	       # iterate through rows of Y
	       for k in range(len(m2)):
	           result[i][j] += m1[i][k] * m2[k][j]
	return result