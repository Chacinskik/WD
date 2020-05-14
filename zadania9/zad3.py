import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import xlrd
import openpyxl


df= pd.read_excel(pd.ExcelFile("C:\\0Krzysztof\WD\imiona.xlsx"),"Arkusz1")
d=df.where(df.Rok >= 2013).groupby('Plec').agg({'Liczba':['sum']})
wykres = d.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6))
plt.title('zad3')
plt.show()
