import random
import numpy as np
 
def generate(x : int, y : int, v_x : int, v_y : int, num : int, class_index : int):
    dim = 2
    s = np.random.randn(num, dim) #生成标准正态分布
    s = s * [v_x, v_y]
    return np.insert(s, 2, values=class_index, axis=1) + [x, y, 0]
