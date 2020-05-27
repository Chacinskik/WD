import matplotlib.pyplot as plt
import numpy as np 


x=np.arange(1, 21)
plt.plot(1/x, label='f(x)=1/x')
plt.axis([1, 20, 0, 1])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title("zad1")
plt.legend()
plt.show()