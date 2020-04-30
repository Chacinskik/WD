import numpy as np 


def zad8(a,kierunek):
    w=True
    if kierunek=="pion":
        if a.shape[1]%2==0:
            b=int(a.shape[1]/2)
            a1=a[:,:b]
            a2=a[:,b:]
        else:
            w=False
    elif kierunek=="poziom":
        if a.shape[0]%2==0:
            b=int(a.shape[0]/2)
            a1=a[:b,:]
            a2=a[b:,:]
        else:
            w=False
    else:
        print("Nieprawidlowe dane!")
    if w==True:
        return a1,a2
    else:
        print("Wymiary tablicy nie pozwalaja na taki podzial")
        return 0,0

a=np.array([[ y for y in range(x*4+1,x*4+4+1)] for x in range(0,4)] )
print(a)
b1,b2=zad8(a,"pion")
print(b1)
print(b2)
b1,b2=zad8(a,"poziom")
print(b1)
print(b2)