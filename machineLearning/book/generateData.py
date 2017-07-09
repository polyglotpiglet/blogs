#!/usr/bin/env python 3.1

import numpy as np
import matplotlib.pyplot as plt

class Data:

    """Holder for two sets of (x,y) 2D coordinates sampled from two difference
    bivariate gaussian distributions"""

    def __init__(self, blueCoordinates, redCoordinates):
        self.blueCoordinates = blueCoordinates
        self.redCoordinates = redCoordinates

    def red_coordinates(self):
        xs, ys = zip(*self.redCoordinates)
        return (xs, ys)

    def blue_coordinates(self):
        xs, ys = zip(*self.blueCoordinates)
        return (xs, ys)

        

numberOfMeans = 100

# We sample the distribution <howMany := n> times to generate <howMany> 'mean'
# points, [(x_1, y_1), ... , (x_n, y_n)]
def generate_xs_and_ys(mean, covariance, howMany):
    x, y = np.random.multivariate_normal(mean, covariance, howMany).T
    return list(zip(x, y))

# We sample 2 distributions
def generate_means():
    mean1 = [1, 0]
    mean2 = [0, 1]
    covariance = [[1, 0], [0, 1]]
    xy1s = generate_xs_and_ys(mean1, covariance, numberOfMeans);
    xy2s = generate_xs_and_ys(mean2, covariance, numberOfMeans);
    return Data(xy1s, xy2s)

def plot_generated_means(data):
    """be a cat"""
    x1s, y1s = data.blue_coordinates()
    x2s, y2s = data.red_coordinates()
    plt.plot(x1s, y1s, 'r.', x2s, y2s, 'b.')
    plt.axis('equal')
    plt.show()

def analyse_data(data): 
    means1, means2 = generatedMeans
    print(sorted(means1))



plot_generated_means(generate_means())
