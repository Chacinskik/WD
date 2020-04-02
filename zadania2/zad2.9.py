liczba = input("Wpisz liczbe")
iteracje = 0
suma = 0
while iteracje != len(liczba):
    suma = suma + int(liczba[iteracje])
    iteracje +=1
print(suma)
