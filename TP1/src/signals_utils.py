import numpy as np
from scipy.signal import lfilter

def generate_test_signals(N=1000, variance = 1.0):

    sigma =  np.sqrt(variance)

    # Signal d'entrée : bruit blanc
    x = np.random.normal(0, sigma, N)

    # Réponse impulsionnelle "inconnue"
    h = np.array([1.0, 0.3, -0.1, 0.2])

    # Signal désiré obtenu par filtrage
    d = lfilter(h, [1.0], x)

    return x, d, h