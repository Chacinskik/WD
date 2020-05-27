import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 
import xlrd
import openpyxl


iris = pd.read_csv('C:\\0Krzysztof\WD\iris.data', names=["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species"])
x=iris['SepalLengthCm']
y=iris['SepalWidthCm']
data={
    'x':x,
    'y':y,
    'c':np.random.randint(0,50,150),
    's':abs(x.subtract(y))
}
plt.xlabel('SepalLengthCm')
plt.ylabel('SepalWidthCm')
plt.scatter('x', 'y', c='c', s='s', data=data)
plt.show()