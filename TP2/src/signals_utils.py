import numpy as np
from scipy.signal import lfilter, firwin

def generate_test_signals(N=1000, variance = 1.0):

    sigma =  np.sqrt(variance)

    # Signal d'entrée : bruit blanc
    x = np.random.normal(0, sigma, N)

    # Réponse impulsionnelle "inconnue"
    h = np.array([1.0, 0.3, -0.1, 0.2])

    # Signal désiré obtenu par filtrage
    d = lfilter(h, [1.0], x)

    return x, d, h

def generate_test_signals_2(N=1000, variance = 1.0, rho = 0.5):

    sigma =  np.sqrt(variance)

    # Signal d'entrée : bruit blanc
    v = np.random.normal(0, sigma, N)
    x = np.zeros(N)
    x[0] = v[0]
    for i in range(1, N):
        x[i] = v[i] + x[i-1] * rho

    # Réponse impulsionnelle "inconnue"
    h = np.array([1.0, 0.3, -0.1, 0.2])

    # Signal désiré obtenu par filtrage
    d = lfilter(h, [1.0], x)

    return x, d, h

def generate_test_LMS_signals(N=1000, variance_x = 1.0, noise_variance = 1.0, P = 10, frequency = 0.5):

    sigma_x =  np.sqrt(variance_x)
    sigma_noise = np.sqrt(noise_variance)

    # Signal d'entrée : bruit blanc
    x = np.random.normal(0, sigma_x, N)
    noise = np.random.normal(0, sigma_noise, N)
    # Réponse impulsionnelle "inconnue"
    h = firwin(P, cutoff=frequency, pass_zero="lowpass")


    # Signal désiré obtenu par filtrage
    d = lfilter(h, [1.0], x)
    d_final = d + noise

    return x, d_final, h


def generate_test_RLS_signals(N=1000, variance_x = 1.0, noise_variance =1.0, P=5, frequency=0.5, rho = 0.5):

    sigma =  np.sqrt(variance_x)
    sigma_noise = np.sqrt(noise_variance)
    # Signal d'entrée : bruit blanc
    noise = np.random.normal(0, sigma_noise, N)
    v = np.random.normal(0, sigma, N)
    x = np.zeros(N)
    x[0] = v[0]
    for i in range(1, N):
        x[i] = v[i] + x[i-1] * rho

    # Réponse impulsionnelle "inconnue"
    h = firwin(P, cutoff=frequency, pass_zero="lowpass")

    # Signal désiré obtenu par filtrage
    d = lfilter(h, [1.0], x)
    d_final = d + noise

    return x, d_final, h


