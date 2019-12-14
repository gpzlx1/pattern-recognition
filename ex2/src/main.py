from generate import generate
from draw import draw
import numpy as np
import random

def distance(p1 ,p2):
    dist = np.sum(np.square(p1-p2))
    return dist

def c_mean(s, num_class : int):
    round = 1
    centers = []
    index = random.sample([i for i in range(len(s))], 3)
    for i in index:
        centers.append(s[i][0:2])

    while True:
        for point in s:
            coords = point[0:2]
            dist = []
            for center in centers:
                dist.append(distance(center, coords))
            point[2] = dist.index(min(dist))
       
        new_center = np.zeros((3,2))
        count = [0] * num_class
        for point in s:
            token = int(point[2])
            count[token] += 1
            new_center[token] += point[0:2]
            
        flag = True
        for i in range(num_class):
            new_center[i] = new_center[i] / count[i]
            if distance(new_center[i], centers[i]) > 1e-5:
                flag = False
                centers[i] = new_center[i]
        
        if flag:
            break

        round += 1
    
    return centers, s

    
        



if __name__ == "__main__":
    class1 = generate(0, 0, 1, 1, 5, 0)
    class2 = generate(5, 5, 1, 1, 100, 1)
    class3 = generate(-5, -5, 1, 1, 100, 2)
    s = np.vstack((class1, class2, class3))
    draw(s,"before.png")
    centers, s = c_mean(s.copy(), 3)
    draw(s,"after.png")


