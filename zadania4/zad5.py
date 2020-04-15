class CiagArytmetyczny:
    def __init__(self, a0, r, ile):
        self.a0 = a0
        self.r = r
        self.ile = ile
    
    def wyswietl_dane(self):
        for i in range(self.ile):
            print(self.a0+(self.r*i))
    
    def pobierz_elementy(self, ile):
        lista = []
        for i in range(ile):
            a = int(input("Podaj element ciagu: "))
            lista.append(a)
        return lista
        
    def pobierz_parametry(self):
        self.a0 = int(input("Pierwsza wartosc: \n"))
        self.r = int(input("Roznica: \n"))
        self.ile = int(input("Ile elementow: \n"))
    
    def policz_sume(self):
        return ((2*self.a0+(self.ile-1)*self.r)/2)*self.ile
    
    def policz_elementy(self, a0, r):
        for i in range(10):
            print(a0+(r*i))
    

ciag1 = CiagArytmetyczny(3,2,5)
ciag1.wyswietl_dane()
print(ciag1.policz_sume())

