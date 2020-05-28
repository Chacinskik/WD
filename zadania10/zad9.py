import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('C:\\0Krzysztof\WD\zamowienia.csv', header=0, sep=";")
sprzedawcy_suma = df.groupby("Sprzedawca")["Utarg"].sum().reset_index(name="Suma zamowien")
sprzedawcy = sprzedawcy_suma["Sprzedawca"]
sumy_zamowien = sprzedawcy_suma["Suma zamowien"]

wedges, texts, autotexts = plt.pie(sumy_zamowien, explode=(0, 0.1, 0, 0, 0, 0, 0.15, 0.2, 0) ,labels=sprzedawcy,
autopct='%1.1f%%', textprops=dict(color="black"), shadow=True)

plt.setp(autotexts, size=14, weight="bold")
plt.title("zad9")
plt.legend(title='Sprzedawcy')
plt.show()