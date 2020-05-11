import numpy as np 


a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([[0,0,0,0],[0,0,0,1], [0,1,0,1],[1,1,1,1]])
print(a)
print(b)
print(a.min(axis=0))
print(a.min(axis=1))
print(b.min(axis=0))
print(b.min(axis=1))