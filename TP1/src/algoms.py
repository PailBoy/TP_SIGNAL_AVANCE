import numpy as np

def algoms(x,d, P, mu) :

    w=[0]*P
    N = len(d)
    for i in N :
        x_vec = []
        for j in P :
            if N < P :
                while P-j != N :
                    x_vec.append(0)
            else :
                x_vec.append(x[N-j])
        y



