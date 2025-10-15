def algoms(x,d, P, mu) :

    w=[0]*P
    N = len(x)
    y=[0]*N
    w_tot = []
    erreur = [0]*N
    w_tot.append(w.copy())
    for n in range(P-1, N):
        x_vec = []
        for p in range(P):
            x_vec.append(x[n-p] if n-p>=0 else 0)
        yn = 0
        for p in range(P):
            yn+= w[p]*x_vec[p]
        y[n] = yn
        erreur[n] = d[n]-y[n]
        for p in range(P):
            w[p]=w[p] + mu* erreur[n] * x_vec[p]
        w_tot.append(w.copy())
    return w_tot, y, erreur






