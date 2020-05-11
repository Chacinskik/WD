import numpy as np 

x=np.arange(12)
print(x)
a=x.reshape(3,4)
print(a)
b=a.reshape(4,3)
print(b)
c=a.reshape(2,6)
print(c)
print("------------------------------------------")
print(a.ravel())
print(b.ravel())
print(c.ravel())
