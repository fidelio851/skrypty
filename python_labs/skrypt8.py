#!/usr/bin/python

import random


def bubbleSort(list):
    length = len(list)
    for i in range(length):

        for j in range(0, length - i - 1):

            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]


def main():
	my_randoms = random.sample(xrange(100), 10)
	print my_randoms
	bubbleSort(my_randoms)
	print my_randoms

if __name__ == '__main__':
	main()
