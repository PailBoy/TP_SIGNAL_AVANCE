import numpy as np
from scipy.signal import lfilter


def algoms(x,d, P, mu) :

    w=[0]*P
    N = len(x)
    y=[]
    erreur = [0]*N
    for n in range(N):
        x_vec = []
        for p in range(P):
            x_vec.append(x[n-p])
        sum = 0
        for p in range(P):
            sum+= w[p]*x_vec[p]
        y.append(sum)
        erreur[n] = d[n]-y[n]
        for p in range(P):
            w[p]=mu* erreur[n] * x_vec[p]

    return w, y, erreur


def algolms(x, d, P, mu):
    N = len(x)
    w = [0.0] * P
    y = [0.0] * N
    e = [0.0] * N

    for n in range(N):
        # construire x_vec = [x[n], x[n-1], ..., x[n-P+1]] avec zero-padding
        x_vec = []
        for p in range(P):
            idx = n - p
            x_vec.append(x[idx] if idx >= 0 else 0.0)

        # sortie
        y_n = 0.0
        for p in range(P):
            y_n += w[p] * x_vec[p]
        y[n] = y_n

        # erreur
        e[n] = d[n] - y[n]

        # mise à jour des poids (LMS)
        for p in range(P):
            w[p] = w[p] + 2.0 * mu * e[n] * x_vec[p]

    return w, y, e



