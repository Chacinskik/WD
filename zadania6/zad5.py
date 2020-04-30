import numpy as np 


def zad5(n):
    a = np.arange(1, n+1)
    wynik = a[::-1]
    return wynik

print(zad5(3))
b = np.diag(zad5(3))
print(b)
