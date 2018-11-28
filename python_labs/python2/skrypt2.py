#!/usr/bin/python

class ComplexNumber:
    def __init__(self, re, im):
        self.Re = re
        self.Im = im

    def __add__(self, other):
        return ComplexNumber(other.Re + self.Re, other.Im + self.Im)

    def __sub__(self, other):
        return ComplexNumber(self.Re - other.Re, self.Im - other.Im)

    def __str__(self):
        return str(self.Re) + " + " + str(self.Im) + "i"


z1 = ComplexNumber(4,5)

z2 = ComplexNumber(1,-5)

print "Liczba z1 = 4+5i, liczba z2= 1-5i, dodawanie: \n"
print z1 + z2
print "odejmowanie:"
print z1 - z2
