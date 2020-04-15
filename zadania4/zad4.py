class NaZakupy:
    def __init__(self, nazwa, ilosc, jednostka, cena_jed):
        self.nazwa_produktu = str(nazwa)
        self.ilosc = ilosc
        self.jednostka_miary = str(jednostka)
        self.cena_jed = cena_jed
    
    def wyswietl_produkt(self):
        print("Nazwa:", self.nazwa_produktu)
        print("Ile: ", self.ilosc)
        print("Czego?: ", self.jednostka_miary)
        print("Cena: ", self.cena_jed)
    
    def ile_produktu(self):
        print(self.ilosc, self.jednostka_miary)

    def ile_kosztuje(self):
        print(self.ilosc * self.cena_jed, "zl")
        return self.ilosc * self.cena_jed

zakupy1 = NaZakupy('chleb', 2, 'szt', 3)
zakupy1.wyswietl_produkt()
zakupy1.ile_produktu()
zakupy1.ile_kosztuje()
