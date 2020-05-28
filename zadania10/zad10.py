import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.subplot(121)
x=np.arange(1, 21)
plt.stem(1/x, use_line_collection=True, label='f(x)=1/x')
plt.axis([1, 20, 0, 1])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title("zad1")
plt.legend()

plt.subplot(122)
x=np.arange(0,31,0.5)
s=np.sin(x)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.plot(x, s, drawstyle='steps-post', label='steps-post')
plt.plot(x, s, label='sin(x)')
plt.legend(loc='upper right')
plt.show()