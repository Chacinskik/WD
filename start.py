import math as m
print('hello world!')
print("Wy"+"raz")
#listy
lista = [1,2,3,4,5,6]
print(lista)
lista.append(7)
print(lista)
wyraz = "abcdefghij"
wyraz2 = wyraz[::]
print(wyraz[4:1:-1])
wyraz = wyraz.swapcase()
print(wyraz)
print(wyraz2)
lista3 = [1, 'Ala', 4.5, None, True, [1,2]]
print(lista3[5][1])
macierz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(macierz[1][1]) # 5
lista4 = lista3 + list(wyraz2)
print(lista4)
#slownik
slownik = {}
slownik['imie'] = 'Krzysztof'
slownik[0] = 'Krzysztof'
print(slownik)
slownik2 = {
    'imie' : 'Adam',
    1: 'uno'
}
print(slownik2[1])
print(slownik2.keys())
print(slownik2.values())
print(m.pi)
for litera in wyraz:
    print(litera)

