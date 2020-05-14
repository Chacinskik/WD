import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import xlrd
import openpyxl


df= pd.read_excel(pd.ExcelFile("C:\\0Krzysztof\WD\imiona.xlsx"),"Arkusz1")
d = df.groupby(['Plec']).agg({'Liczba':['sum']})
print(d)
wykres=d.plot.bar()
wykres.set_ylabel('Mln')
wykres.legend()
plt.title('zad2')
plt.show()
