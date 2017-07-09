#!/usr/bin/env python 3.1

import numpy as np
import matplotlib.pyplot as plt

numberOfMeans = 100

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

    def max_y_coordinate(self):
        x1s, y1s = self.blue_coordinates()
        x2s, y2s = self.red_coordinates()
        return max(max(y1s), max(y2s))

    def max_x_coordinate(self):
        x1s, y1s = self.blue_coordinates()
        x2s, y2s = self.red_coordinates()
        return max(max(x1s), max(x2s))

    def min_y_coordinate(self):
        x1s, y1s = self.blue_coordinates()
        x2s, y2s = self.red_coordinates()
        return min(min(y1s), min(y2s))

    def min_x_coordinate(self):
        x1s, y1s = self.blue_coordinates()
        x2s, y2s = self.red_coordinates()
        return min(min(x1s), min(x2s))

def generate_xs_and_ys(mean, covariance, n):
    """We sample the distribution <n> times to generate <n> coordinates
    [(x_1, y_1), ... , (x_n, y_n)]"""
    x, y = np.random.multivariate_normal(mean, covariance, n).T
    return list(zip(x, y))

def generate_blue_and_red_coordinates():
    """sample two distributions to get the data"""
    mean1 = [1, 0]
    mean2 = [0, 1]
    covariance = [[1, 0], [0, 1]]
    xy1s = generate_xs_and_ys(mean1, covariance, numberOfMeans);
    xy2s = generate_xs_and_ys(mean2, covariance, numberOfMeans);
    return Data(xy1s, xy2s)

def plot_generated_means(data):
    """plot the red and blue coordinates on the same graph"""
    x1s, y1s = data.blue_coordinates()
    x2s, y2s = data.red_coordinates()
    plt.plot(x1s, y1s, 'r.', x2s, y2s, 'b.')
    plt.axis('equal')
    plt.show()

def analyse_data(data): 
    print(data.max_x_coordinate())
    print(data.min_x_coordinate())
    print(data.max_y_coordinate())
    print(data.min_y_coordinate())



analyse_data(generate_blue_and_red_coordinates())
