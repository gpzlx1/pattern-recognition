import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

def draw(data : list, WList : np.array, filename):
    plt.clf()
    fig, ax = plt.subplots()
    ims = []
    plt.xlim((-1,5))
    plt.ylim((-1,5))

    for point in data:
        if point[2] > 0:
            ax.scatter(point[0], point[1], marker = "+", color="r")
        else:
            ax.scatter(-point[0], -point[1], marker = "*", color="b")
        
    x = np.linspace(-1, 5, 100)
    y = np.linspace(-1, 5, 100)
    x, y = np.meshgrid(x, y)
    #draw W
    f = WList[0][0] * x + WList[0][1] * y  + WList[0][2]
    W = ax.contour(x, y, f, 0)

    def update(i):
        ax.cla()
        for point in data:
            if point[2] > 0:
                ax.scatter(point[0], point[1], marker = "+", color="r")
            else:
                ax.scatter(-point[0], -point[1], marker = "*", color="b")
        x = np.linspace(-1, 5, 100)
        y = np.linspace(-1, 5, 100)
        x, y = np.meshgrid(x, y)
        f = WList[i][0] * x + WList[i][1] * y  + WList[i][2]
        ax.contour(x, y, f, 0)
        return W, ax

    anim = animation.FuncAnimation(fig, update, frames=np.arange(len(WList)), interval=200)
    anim.save("./ex1/pict/" + filename + ".gif", writer="pillow")