import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt


df=pd.read_csv("C:\\0Krzysztof\WD\zamowienia.csv", header=0, delimiter=';')
d=df.groupby('Sprzedawca').agg({'idZamowienia':['count']})
wykres = d.plot.bar()
wykres.set_xlabel('Sprzedawca')
wykres.set_ylabel('Ilosc zamowien')
wykres.legend()
plt.title('Sprzedaze')
plt.show()

