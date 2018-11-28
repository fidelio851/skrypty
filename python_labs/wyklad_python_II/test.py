#!/usr/bin/python
from collections import Counter


def histogram(L):

    return Counter(L).items()

L = histogram([1,2,3,4,4,0])
print L