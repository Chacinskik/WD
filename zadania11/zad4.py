import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

kolorki= ["r", "g", "b", "y", "m"]
fig = plt.figure( figsize =( 8 , 3 ))

for kolor_index in range(1, 6):
    ax = fig.add_subplot( 1 , 5 , kolor_index , projection = '3d' )
    ax = fig.gca(projection = "3d")
    _x = np.arange(4)
    _y = np.arange(5)
    _xx, _yy = np.meshgrid(_x, _y)
    x, y = _xx.ravel(), _yy.ravel()
    top = x + y
    bottom = np.zeros_like(top)
    width = depth = 1
    ax.bar3d(x, y, bottom, width, depth, top, shade = True, color=kolorki[kolor_index-1])
    if(kolor_index==3):
        ax.set_title("zad4")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
plt.show()