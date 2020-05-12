import pandas as pd
import numpy as np 


df = pd.read_csv('C:\\0Krzysztof\WD\zamowienia.csv', header=0, delimiter=';')
#print(df)
#3.1-------------------------
#print(df.Sprzedawca.unique())
#3.2-------------------------
#print(df.sort_values('Utarg', ascending=False).iloc[:5])
#3.3-------------------------
#print(df.groupby(['Sprzedawca']).agg({"idZamowienia":['count']}))
#3.4-------------------------
#print(df.groupby(['Kraj']).agg({"idZamowienia":['count']}))
#3.5-------------------------
#print((df[((df['Data zamowienia'].str.contains('2005'))&(df.Kraj=='Polska'))]).groupby(['Kraj']).agg({'idZamowienia':'count'}))
#3.6-------------------------
#print((df[(df['Data zamowienia'].str.contains('2004'))]).agg({'Utarg':'mean'}))
#3.7-------------------------
df[df["Data zamowienia"].str.contains("2004")].to_csv('zamówienia_2004.csv',index=False,sep=';')
df[df["Data zamowienia"].str.contains("2005")].to_csv('zamówienia_2005.csv',index=False,sep=';')





