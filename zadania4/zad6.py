class Slowa:
    def __init__(self, slowo1, slowo2):
        self.slowo1 = slowo1
        self.slowo2 = slowo2
    
    def czy_palindrom(self, slowo1):
        slowo1temp = list(slowo1)
        if (slowo1temp[::]==slowo1temp[::-1]):
            return True
        return False
    
    def czy_metagramy(self, slowo1, slowo2):
        counter = 0
        if (len(slowo1)!=len(slowo2)):
            return False
        for i in range(len(slowo1)):
            if (slowo1[i]!=slowo2[i]):
                counter +=1
            if (counter>1):
                return False
        return True
    
    def czy_anagramy(self, slowo1, slowo2):
        if (len(slowo1)!=len(slowo2)):
            return False
        slowo1set = set(slowo1)
        slowo2set = set(slowo2)
        if (slowo1set==slowo2set):
            return True
        return False
    
    def wyswietl_wyrazy(self, slowo1):
        print(slowo1)

wyraz = Slowa('racecar', 'drugie')
print(wyraz.czy_palindrom('racecar'))
print(wyraz.czy_metagramy('mata', 'tata'))
print(wyraz.czy_anagramy('mata', 'tama'))


