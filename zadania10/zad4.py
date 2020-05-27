import matplotlib.pyplot as plt
import numpy as np 


x=np.arange(0,31,0.1)
s=np.sin(x)
a='sin(x)'
s2 = np.sin(x+3.14)
plt.axis([-1.5, 31.5, -1.25, 3.25])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Wykres {}, {}'.format(a, a))
plt.plot(x, s+2, label=a)
plt.plot(x,s2, label=a)
plt.legend(loc='center left')
plt.show()