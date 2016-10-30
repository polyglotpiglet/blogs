import numpy as np
import matplotlib.pyplot as plt

x = (1, 1.1, 0.8, 0.2, 1.2, 0.9, 1.1, 1.2, 0.4, 0.7, 0.8, 0.6)
y = (0.8, 1.0, 0.7, 0.4, 1.1, 1.1, 1.3, 1.0, 0.5, 0.8, 0.6, 0.75)

# plot my scatter points
plt.scatter(x, y, c='violet', alpha=0.5)

# straight line through origin
plt.plot([0, 1.5], [1.5, 0])

plt.axis([0, 1.5, 0, 1.5])

plt.show()
