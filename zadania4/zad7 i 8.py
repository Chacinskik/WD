class Robaczek:
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok
    
    def __del__(self):
        print("Pomscij mnie!")
    
    def idz_w_gore(self, ilekrokow):
        self.y = self.y + ilekrokow*self.krok

    def idz_w_dol(self, ilekrokow):
        self.y = self.y - ilekrokow*self.krok
    
    def idz_w_lewo(self, ilekrokow):
        self.x = self.x - ilekrokow*self.krok
    
    def idz_w_prawo(self, ilekrokow):
        self.x = self.x + ilekrokow*self.krok
    
    def pokaz_gdzie_jestes(self):
        print(self.x, self.y)
    
robak = Robaczek(0,0,2)
robak.idz_w_prawo(3)
robak.pokaz_gdzie_jestes()
