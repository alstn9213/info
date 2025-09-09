import numpy as np 
import matplotlib.pyplot as plt

D1 = np.array([[1.0,1.2,3,4,5,6], [1.5,3,2.3,5.3,3.8,5.5]])
D2 = np.array([[-0.6,1.0,1.2,3,4,5,6],[2.9,1.5,3,2.3,5.3,3.8,5.5]])

fig, (ax1,ax2) = plt.subplots(1,2,sharex=True,sharey=True)
fig.set_size_inches((15,6))

ax1.plot(D1[0], D1[1], 'ko', markersize=10)
ax1.set_xlim([-1,7])
ax1.set_ylim([1,6])
ax1.set_title('D1', fontsize=18)

ax2.plot(D2[0], D2[1], 'ko', markersize=10)
ax2.set_xlim([-1,7])
ax2.set_ylim([1,6])
ax2.set_title('D2', fontsize=18)

plt.show()