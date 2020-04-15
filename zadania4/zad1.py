import sys


lista = []
for i in range(4,419,4):
    lista.append(i)

print(lista)
plik = open('zadania4/dane1.txt', 'a+')
plik.writelines(str(lista))
plik.close()