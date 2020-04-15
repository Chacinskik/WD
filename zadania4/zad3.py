with open("zadania4/dane2.txt", 'w+') as plik:
    plik.write("Mam dobry dzien\nBo dobrze sie czuje\nNic mnie nie kluje\nAle zaden ze mnie len!")
    plik.seek(0,0)
    for linia in plik:
        print(linia, end="")

    