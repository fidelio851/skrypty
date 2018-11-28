#!/usr/bin/python

#a,b,c -first function coefficients; d,e,f - second function coefficients

a = float(input("Podaj wspolczynnik a: "))
b = float(input("Podaj wspolczynnik b: "))
c = float(input("Podaj wspolczynnik c: "))


#computing function`s roots


delta = b**2 - 4*a * c


if(delta >= 0):
    sqrDelta = pow(delta, 0.5)
    case = 1
    x1 = (-(b)-sqrDelta) / (2*(a))
    x2 = (-(b)+sqrDelta) / (2*(a))
    if(x1 == x2):
        print("Funkcja ma jedno miejsce zerowe w punkcie x1: ", x1)
    else:
        print("Funkcje ma dwa miejsca zerowe x1: ",x1," oraz x2: ", x2)
else:
    print 'Funkcja nie ma miejsc zerowych'