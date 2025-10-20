import numpy as np

def algoms_RLS(x, d, P, lambda_=0.99, delta=1000.0):

    x = np.asarray(x, dtype=float)
    d = np.asarray(d, dtype=float)
    N = len(x)


    w = np.zeros(P, dtype=float)
    Pmat = (1.0 / delta) * np.eye(P, dtype=float)
    y = np.zeros(N, dtype=float)
    e = np.zeros(N, dtype=float)
    W = [w.copy()]

    for n in range(P - 1, N):
        x_vec = np.array([x[n - p] for p in range(P)], dtype=float)

        yn = 0
        for p in range(P):
            yn += w[p] * x_vec[p]

        y[n] = yn
        e[n] = d[n] - y[n]

        # gain de Kalman
        Px = Pmat @ x_vec
        denom = lambda_ + float(x_vec @ Px)
        k = Px / denom

        # mise à jour des poids
        w = w + k * e[n]

        # mise à jour de Pmat
        Pmat = (Pmat - np.outer(k, x_vec) @ Pmat) / lambda_

        # logger trajectoires
        W.append(w.copy())
    return W, y, e