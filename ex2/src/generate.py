import random
import numpy as np
 
def generate(x : int, y : int, num : int, class_num : int):
    dim = 2
    s = np.random.randn(num, dim) #生成标准正态分布
    return np.insert(s, 2, values=class_num, axis=1) + [x, y, 0]
