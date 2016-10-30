import numpy as np
import matplotlib.pyplot as plt
import math

x1 = (0, 0.5, 0.7, 1.0, 1.5, 2.0, 2.2, 2.5, 2.6, 2.7, 3.0)
y1 = (4, 4.4, 5.0, 4.6, 3.7, 2.1, 2.0, 2.1, 3.0, 6.0, 10.5)

# plot my scatter points
plt.scatter(x1, y1, c='violet', alpha=0.5)

x2 = np.linspace(0,3,100)
y2 = 3.73200105121773 + 3.0893686896511547 * x2 - 5.027053275626108 * x2 * x2 / 9 - 64.13289983672958 * x2 * x2 * x2 / 27  +  66.60514592812433 * x2 * x2 * x2 * x2 / 81

plt.plot(x2,y2)


plt.axis([0, 3.0, 0, 11])

plt.show()
