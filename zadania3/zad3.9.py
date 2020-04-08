def iloczyn(* liczby):
    if len(liczby)==0:
        return 0.0
    else:
        wynik = 1.0
        for i in liczby:
            wynik *= i
        return wynik

print(iloczyn(1,2,3,4,5))

