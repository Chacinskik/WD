import matplotlib.pyplot as plt
import numpy as np 


x=np.arange(1, 21)
plt.plot(1/x, 'g>:', label='f(x)=1/x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title("zad2")
plt.legend()
plt.show()