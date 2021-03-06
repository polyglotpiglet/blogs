import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,1,100)
y = - 1 * np.log(x)

fig, ax = plt.subplots()
ax.plot(x, y)
#ax.set_aspect('equal')
ax.grid(True, which='both')

ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

#plt.plot(x,y)
plt.show()
