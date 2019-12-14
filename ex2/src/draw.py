import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import random

char = ["1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]

# s 点集合
# tag 在图上的表示
def get_random_color():
    color = "#"
    for i in range(6):
        color = color + str(random.sample(char,1)[0])
    return color

def draw( s : list, name : str):
    plt.clf()
    plt.xlim((-10,10))
    plt.ylim((-10,10))
    map = {}
    for point in s:
        if point[2] in map.keys():
            color = map[point[2]]
        else:
            color = get_random_color()
            map[point[2]] = color
        plt.scatter(point[0], point[1], marker = "+", color=color)
    plt.savefig(name)