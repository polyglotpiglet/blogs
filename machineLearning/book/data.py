#!/usr/bin/env python 3.1
import numpy as np
import matplotlib.pyplot as plt

numberOfMeans = 10

# We sample the distribution <howMany := n> times to generate <howMany> 'mean'
# points, [(x_1, y_1), ... , (x_n, y_n)]
def generateXsAndYs(mean, covariance, howMany):
  x, y = np.random.multivariate_normal(mean, covariance, howMany).T
  return list(zip(x, y))

# We sample 2 distributions
def generateMeans():
  mean1 = [1, 0]
  mean2 = [0, 1]
  covariance = [[1, 0], [0, 1]]
  xy1s = generateXsAndYs(mean1, covariance, numberOfMeans);
  xy2s = generateXsAndYs(mean2, covariance, numberOfMeans);
  return (xy1s, xy2s)

def plotGeneratedMeans(generatedMeans):
  means1, means2 = generatedMeans
  x1s, y1s = zip(*means1)
  x2s, y2s = zip(*means2) 
  plt.plot(x1s, y1s, 'r.', x2s, y2s, 'b.')
  plt.axis('equal')
  plt.show()

"""Takes in a list of <numberOfMeans := n> tuples [(x_0, y_0), ... (x_n, y_n)]
 Then generates 100 observations by choosing one of these n means at random
 (let's call it the ith mean, ie (x_i, y_i)) (with uniform probability) and 
 sample the distribution N((x_i, y_i)T, I/5) where I is the identity matrix."""
def generateObservationsFromMean(generatedMean):
  covariance = [[0.2, 0], [0, 0.2]]
  for i in range(0, 100):
    rand = np.random.randint(0, numberOfMeans)
    mu_x, mu_y = generatedMean[rand]
    x, y = np.random.multivariate_normal([mu_x, mu_y], covariance, 1).T
    yield (x[0], y[0])

def generateObservations():
  mean1, mean2 = generateMeans()
  blueObservations = list(generateObservationsFromMean(mean1))
  redObservations = list(generateObservationsFromMean(mean2))
  x1s, y1s = zip(*blueObservations)
  x2s, y2s = zip(*redObservations)
  return (x1s, y1s, x2s, y2s) # TODO make this a class

def plotObservations(observations): 
  x1s = observations[0]
  y1s = observations[1]
  x2s = observations[2]
  y2s = observations[3]
  plt.plot(x1s, y1s, 'b.', x2s, y2s, 'r.')
  plt.axis('equal')
  plt.show()




obz = generateObservations()
plotObservations(obz)
