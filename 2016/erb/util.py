from math import sqrt

__author__ = 'erb'


def distance_to(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
