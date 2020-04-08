def ile_zakupow(**rzeczy):
    wynik=0
    for cos in rzeczy:
        wynik+=1*int(rzeczy[cos])
    return wynik

print(ile_zakupow(slodycze='5', zelki='8'))