import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import xlrd
import openpyxl


df= pd.read_excel(pd.ExcelFile("C:\\0Krzysztof\WD\imiona.xlsx"),"Arkusz1")
w=df.groupby(['Rok']).agg({'Liczba':['sum']})
w.plot(xticks=w.index.values)
plt.legend()
plt.show()





