import sys
import numpy as np
import matplotlib.pyplot as plt

theta1 = 0.24522210175513323
theta2 = 1.0684296895629888
theta3 = -1.7556623273903793
theta4 = 2.4372319164446665
theta5 = -1.0215605651849788

x1 = (1,1.1,0.8,0.2,1.2,0.9,1.1, 1.2,0.4, 0.7, 0.6)
y1 = (0.8, 1.0, 0.7, 0.4, 1.1, 1.1, 1.3, 1.0, 0.5, 0.8, 0.75)

# plot my scatter points
plt.scatter(x1, y1, c='violet', alpha=0.5)

x2 = np.linspace(0,3,100)
y2 = theta1 + theta2 * x2 + theta3 * np.power(x2,2) + theta4 * np.power(x2, 3) + theta5 * np.power(x2,4) 

#plt.plot(x2,y2)

plt.axis([0, 1.2, 0, 1.5])

plt.show()

