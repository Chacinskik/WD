import numpy as np 


a=np.arange(81).reshape(9,9)
print(a)
b=a.reshape((3,27))
print(b)
c=a.reshape((1,81))
print(c)