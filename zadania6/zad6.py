import numpy as np 


def zad6():
    slowa=['rewor', 'aagjh', 'ftciu', 'awejp', 'łgbna']
    a=np.array([[x for x in slowa[i]] for i in range(5)])
    return a
        

print(zad6())