#!/usr/bin/env python 3.1

import numpy as np
import matplotlib.pyplot as plt

numberOfObservations = 100


class Data:

    """Holder for two sets of (x,y) 2D coordinates sampled from two difference
    bivariate gaussian distributions"""

    def __init__(self, blueCoordinates, redCoordinates):
        self.blueCoordinates = blueCoordinates
        self.redCoordinates = redCoordinates
        _blue_xs, _blue_ys = zip(*self.blueCoordinates)
        _red_xs, _red_ys = zip(*self.redCoordinates)
        self._blue_xs = _blue_xs
        self._blue_ys = _blue_ys
        self._red_xs = _red_xs
        self._red_ys = _red_ys

    def red_coordinates(self):
        xs, ys = zip(*self.redCoordinates)
        return (xs, ys)

    def blue_coordinates(self):
        xs, ys = zip(*self.blueCoordinates)
        return (xs, ys)

    def max_y_coordinate(self):
        return max(max(self._blue_ys), max(self._red_ys))

    def max_x_coordinate(self):
        return max(max(self._blue_xs), max(self._red_xs))

    def min_y_coordinate(self):
        return min(min(self._blue_ys), min(self._red_ys))

    def min_x_coordinate(self):
        return min(min(self._blue_xs), min(self._red_xs))


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
    xy1s = generate_xs_and_ys(mean1, covariance, numberOfObservations)
    xy2s = generate_xs_and_ys(mean2, covariance, numberOfObservations)
    return Data(xy1s, xy2s)


def plot_generated_means(data):

    """plot the red and blue coordinates on the same graph"""

    x1s, y1s = data.blue_coordinates()
    x2s, y2s = data.red_coordinates()
    plt.plot(x1s, y1s, 'r.', x2s, y2s, 'b.')
    plt.axis('equal')
    plt.show()


def generate_points_to_analyse(data):

    """generates a set of evenly spaced coordinates to check"""

    min_x = data.min_x_coordinate()
    min_y = data.min_y_coordinate()
    x_interval = (data.max_x_coordinate() - min_x) / numberOfObservations
    y_interval = (data.max_y_coordinate() - min_y) / numberOfObservations
    for i in range(0, numberOfObservations):
        for j in range(0, numberOfObservations):
            yield(min_x + i * x_interval, min_y + j * y_interval)


def plot_points_to_test_and_actual_data(data, observations):

    obs_x, obs_y = list(zip(*list(observations)))
    x1s, y1s = data.blue_coordinates()
    x2s, y2s = data.red_coordinates()
    plt.plot(obs_x, obs_y, 'y.', x1s, y1s, 'r.', x2s, y2s, 'b.')
    plt.axis('equal')
    plt.show()


data = generate_blue_and_red_coordinates()
points = generate_points_to_analyse(data)
plot_points_to_test_and_actual_data(data, points)
