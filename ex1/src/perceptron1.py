import numpy as np
from drawgif import draw
import random
lr = 1	#学习率

if __name__ == "__main__":
    data = []
    # X1类
    data.append(np.array([1,0,1], dtype=float))
    data.append(np.array([1,1,1], dtype=float))
    data.append(np.array([0,2,1], dtype=float))

    # X2类
    data.append(np.array([-2,-1,-1], dtype=float))
    data.append(np.array([-2,-2,-1], dtype=float))
    data.append(np.array([-1,-3,-1], dtype=float))

    #init 
    W = np.array([0,0,0], dtype=float)	
    #Wlist store the value of W in every round
    WList = []
    WList.append(W)
    round = 0
    status = False

    #begin
    while status is False:
        status = True	#用于验证算法是否已经收敛
        round = round + 1
        for i in range(len(data)):
            if np.dot(W, data[i]) <= 0:
                W = W + lr * data[i]
                status = False
            WList.append(W)
    print(WList)
    print(round)
    draw(data, WList, "result10")	#绘制动态图