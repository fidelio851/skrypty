#!/usr/bin/python

import random

matrix1 = [[random.randrange(100) for i in range (128)] for j in range (128)]
matrix2 = [[random.randrange(100) for i in range (128)] for j in range (128)]

def sum(m1, m2):
	m3 = [[0 for i in range (128)] for j in range (128)]
	for i in range (len(m1)):
		for j in range (len(m2)):
			m3[i][j] = m1[i][j] + m2[i][j]
	return m3

print sum(matrix1, matrix2)


