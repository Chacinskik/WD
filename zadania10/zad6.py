import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 
import xlrd
import openpyxl


xlsx = pd.ExcelFile('C:\\0Krzysztof\WD\imiona.xlsx')
df = pd.read_excel(xlsx, 'Arkusz1')

plt.subplot(131)
liczba_plec = df.groupby("Plec")["Liczba"].sum()
liczba_k = liczba_plec[0]
liczba_m = liczba_plec[1]
etykiety1=['M', 'K']
wartosci1=[liczba_m, liczba_k]
plt.ylabel('Ilosc narodzin')
plt.title('zad6.1')
plt.bar(etykiety1, wartosci1, color='r')

plt.subplot(132)
wszystkie_lata = df.groupby(["Rok", "Plec"])["Liczba"].sum().reset_index()
wszystkie_lata_K = wszystkie_lata[wszystkie_lata["Plec"] == "K"].reset_index()
wszystkie_lata_M = wszystkie_lata[wszystkie_lata["Plec"] == "M"].reset_index()
plt.ylabel('Ilosc narodzin')
plt.xlabel('Rok')
plt.plot(wszystkie_lata_M["Rok"], wszystkie_lata_M["Liczba"], label="M")
plt.plot(wszystkie_lata_K["Rok"], wszystkie_lata_K["Liczba"], label="K")
plt.legend(loc="lower right")
plt.title("zad6.2")

plt.subplot(133)
suma_w_kazdym_roku=df.groupby('Rok')['Liczba'].sum().reset_index()
etykiety2=suma_w_kazdym_roku['Rok']
wartosci2=suma_w_kazdym_roku['Liczba']
plt.ylabel('Ilość narodzin')
plt.xlabel('Rok')
plt.title('zad6.3')
plt.bar(etykiety2, wartosci2, label='Suma narodzin', color='g')

plt.show()