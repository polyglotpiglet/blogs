import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,5,100)
y = np.log(x) 

fig, ax = plt.subplots()
ax.plot(x, np.log(x))
ax.set_aspect('equal')
ax.grid(True, which='both')

ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

#plt.plot(x,y)
plt.show()
