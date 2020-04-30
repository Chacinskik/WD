import numpy as np 


def zad7(n):
    a=np.diag([2 for x in range(n)])
    for i in range(2,n+1):
        a+= np.diag([2*i for x in range(n-i+1)],-(i-1))
        a+= np.diag([2*i for x in range(n-i+1)],(i-1))
    return a

print(zad7(5))