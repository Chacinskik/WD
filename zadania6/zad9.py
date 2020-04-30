import numpy as np 


fib=[]
minifib=[]
a=0
b=1
for x in range(5):
    for y in range(5):
        temp=b
        b+=a
        a=temp
        minifib.append(a)
    fib.append(minifib)
    minifib=[]
c= np.array(fib)
print(c)