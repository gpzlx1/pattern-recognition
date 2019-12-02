import numpy as np
from drawgif import draw

if __name__ == "__main__":
    data = []
    # X1类
    data.append(np.array([0,0,1], dtype=float))
    data.append(np.array([1,1,1], dtype=float))

    # X2类
    data.append(np.array([0,-1,-1], dtype=float))
    data.append(np.array([-1,0,-1], dtype=float))


    #init 
    W = np.array([1,0,-1], dtype=float)
    #Wlist store the value of W in every round
    WList = []
    WList.append(W)
    round = 0
    status = False

    #begin
    while status is False:
        if round > 20:
            break
        status = True
        round = round + 1
        for i in range(len(data)):
            if np.dot(W, data[i]) <= 0:
                W = W + 0.5 * data[i]
                status = False
            WList.append(W)

    print(round)
    draw(data, WList, "result2")

