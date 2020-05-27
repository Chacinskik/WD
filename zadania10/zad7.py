import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 
import xlrd
import openpyxl


xlsx = pd.ExcelFile('C:\\0Krzysztof\WD\imiona.xlsx')
df = pd.read_excel(xlsx, 'Arkusz1')

wszystkie_lata = df.groupby(["Rok", "Plec"])["Liczba"].sum().reset_index()
wszystkie_lata_K = wszystkie_lata[wszystkie_lata["Plec"] == "K"].reset_index()
wszystkie_lata_M = wszystkie_lata[wszystkie_lata["Plec"] == "M"].reset_index()

plt.bar(wszystkie_lata_K["Rok"], wszystkie_lata_K["Liczba"], label="K")
plt.bar(wszystkie_lata_M["Rok"], wszystkie_lata_M["Liczba"], label="M", bottom=wszystkie_lata_K['Liczba'])
plt.ylabel('Ilosc narodzin')
plt.xlabel('Rok')
plt.title('zad7')
plt.legend()
plt.show()