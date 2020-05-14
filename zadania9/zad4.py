import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt


iris = pd.read_csv('C:\\0Krzysztof\WD\iris.data', names=["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species"])

iris_setosa = iris[iris["Species"]=="Iris-setosa"]
iris_versicolor = iris[iris["Species"]=="Iris-versicolor"]
iris_virginica = iris[iris["Species"]=="Iris-virginica"]

x3 = iris_virginica["SepalLengthCm"]
y3 = iris_virginica["PetalLengthCm"]
plt.scatter(x3, y3, color="r", label="Iris virginica")

x = iris_setosa["SepalLengthCm"]
y = iris_setosa["PetalLengthCm"]
plt.scatter(x, y, color="g", label="Iris setosa")

x2 = iris_versicolor["SepalLengthCm"]
y2 = iris_versicolor["PetalLengthCm"]
plt.scatter(x2, y2, color="b", label="Iris versicolor")

plt.xlabel("Sepal length (cm)")
plt.ylabel("Petal length (cm)")
plt.title("Iris dataset: petal length and sepal length")
plt.legend(loc="lower right")
plt.plot()
plt.show()