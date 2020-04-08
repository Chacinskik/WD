import random


macierz=[]
for i in range(16):
    macierz.append(random.randint(1,9))
przekatne = [macierz[x*4] for x in range(len(macierz)//4)]
print(macierz)
print(przekatne)