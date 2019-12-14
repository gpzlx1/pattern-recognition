import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# s 点集合
# tag 在图上的表示
def draw( s : list, name : str):
    plt.clf()
    plt.xlim((-10,10))
    plt.ylim((-10,10))
    for point in s:
        if point[2] == 0:
            plt.scatter(point[0], point[1], marker = "+", color="r")
        if point[2] == 1:
            plt.scatter(point[0], point[1], marker = "+", color="g")
        if point[2] == 2:
            plt.scatter(point[0], point[1], marker = "+", color="b")    
    plt.savefig(name)