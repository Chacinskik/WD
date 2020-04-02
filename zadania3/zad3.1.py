x=10
lista1= [liczba+1 for liczba in range(x)]
print(lista1)
lista2=[2**i for i in range(x+1)]
print(lista2)
lista3=[x for x in lista2 if x%4==0]
print(lista3)