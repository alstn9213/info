import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

plt.figure(figsize=(7,7))

ax = plt.axes(projection='3d')
ax.xaxis.set_tick_params(labelsize=15)
ax.yaxis.set_tick_params(labelsize=15)
ax.zaxis.set_tick_params(labelsize=15)
ax.set_xlabel('$x$', fontsize=20)
ax.set_ylabel('$y$', fontsize=20)
ax.set_zlabel('$z$', fontsize=20)

# eq(3,3)
t = np.linspace(0,2,101)
x = np.sin(6*t)
y = 1/4 * t
z = t**2 / 2

ax.plot3D(x,y,z,c='k')
ax.plot([x[0]], [y[0]], [z[0]], 'o', markersize=10, color='k', label="t = {:.2f}".format(t[50]))

ax.plot([x[-1]], [y[-1]], [z[-1]], '*', markersize=10, color='k',label="t = {:.2f}".format(t[-1]))

ax.legend(fontsize=15, loc="upper left")

plt.show()