import sys
import numpy as np
import matplotlib.pyplot as plt

# input file where results are stored line by line
resultFile = sys.argv[1]

f = open(resultFile)
lines = f.read().split("\n")
removeLast = lines[:len(lines) - 2]

# list of resutls as floats
results = map(lambda l: float(l), removeLast)

plt.plot(results)
plt.show()


