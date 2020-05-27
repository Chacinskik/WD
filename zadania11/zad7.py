import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.gca(projection = "3d")
n = 5

for c, m, zlow, zhigh in [( "r" , "o" , -5 , 5 )]:
    xs = randrange(n, 23 , 32 )
    ys = randrange(n, 0 , 0 )
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c =c, marker =m, label="Jablka")

ax = fig.gca(projection = "3d")
t = np.linspace( 0 , 2 * np.pi, 10 )
z = t
x = np.sin(t)
y = np.sin(t)*0.1
ax.plot(x+30, y, z, label = "Waz", color="g", linewidth=4)
ax.legend()
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()