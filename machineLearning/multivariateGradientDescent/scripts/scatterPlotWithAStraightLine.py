import numpy as np
import matplotlib.pyplot as plt

x = (0, 0.5, 0.7, 1.0, 1.5, 2.0, 2.2, 2.5, 2.6, 2.7, 3.0)
y = (4, 4.4, 5.0, 4.6, 3.7, 2.1, 2.0, 2.1, 3.0, 6.0, 10.5)

# plot my scatter points
plt.scatter(x, y, c='violet', alpha=0.5)

plt.plot([0, 3.5495164410057947], [3, 3.5495164410057947 + 3 * 0.44680851063830135])

plt.axis([0, 3.0, 0, 11])

plt.show()
