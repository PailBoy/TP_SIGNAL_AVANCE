import numpy as np
from scipy.signal import lfilter

def generate_test_signals(N=1000, variance = 1.0):
    """
    Génère les signaux x[n] (bruit blanc) et d[n] = h*x[n],
    où h est la réponse impulsionnelle inconnue [1, 0.3, -0.1, 0.2].

    Paramètres
    ----------
    N : int
        Longueur du signal à générer
    seed : int
        Graine aléatoire pour la reproductibilité

    Renvoie
    -------
    x : ndarray
        Signal d'entrée (bruit blanc)
    d : ndarray
        Signal de sortie obtenu par filtrage
    h : ndarray
        Réponse impulsionnelle utilisée (filtre inconnu)
    """
    sigma =  np.sqrt(variance)

    # Signal d'entrée : bruit blanc
    x = np.random.normal(0, sigma, N)

    # Réponse impulsionnelle "inconnue"
    h = np.array([1.0, 0.3, -0.1, 0.2])

    # Signal désiré obtenu par filtrage
    d = lfilter(h, [1.0], x)

    return x, d, h