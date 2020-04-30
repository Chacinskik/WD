import numpy as np 


def zad4(a, n):
    wynik = np.logspace(1, n, n, base=a, dtype='int')
    return wynik

print(zad4(2,4))