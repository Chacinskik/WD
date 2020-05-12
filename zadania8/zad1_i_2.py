import pandas as pd
import numpy as np 
import xlrd
import openpyxl


xlsx = pd.ExcelFile('C:\\0Krzysztof\WD\imiona.xlsx')
df = pd.read_excel(xlsx, 'Arkusz1')
#2.1--------------------------
#print(df.where(df.Liczba > 1000).dropna())
#2.2--------------------------
#print(df.where(df.Imie == 'krzysztof'.upper()).dropna())
#2.3--------------------------
#print(df.agg({'Liczba':['sum']}).dropna())
#2.4--------------------------
#print(df.where(df.Rok<=2005).groupby(['Rok']).agg({'Liczba':['sum']}).dropna())
#2.5--------------------------
#print(df.groupby(['Plec']).agg({'Liczba':['sum']}).dropna())
#2.6--------------------------
#brak efektywnego pomyslu :c
#2.7--------------------------
k=df[df['Plec']=='K']
kmax=df[df['Plec']=='K'].max()
print(k[(k['Liczba']==kmax['Liczba'])])
m=df[df['Plec']=='M']
mmax=df[df['Plec']=='M'].max()
print(m[(m['Liczba']==mmax['Liczba'])])
