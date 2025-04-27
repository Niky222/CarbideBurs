import numpy as np
from scipy.optimize import curve_fit


R = np. array (153.66, 49.75, 107.16, 99.83, 48.87, 50.45, 85.20, 87.84, 76.70, 74.84, 73.15, 79.99])
V = np.array ([130, 160, 130, 160, 130, 160, 130, 160, 144.2, 144.2, 144.2, 144.2])
f = np.array ([0.03, 0.03, 0.03, 0.07, 0.07, 0.03, 0.03, 0.07, 0.07, 0.046, 0.046, 0.046, 0.046])
y = np.array([7, 7, 7, 7, 13, 13, 13, 13, 9.5, 9.5, 9.5, 9.5])


initial_guess = [1, 1, 1, 1]


params, covariance = curve_fit(lambda V, C, k, l, m: C * (V ** k) * (f ** l) * (y ** m), V, R, p0=initial_guess)


c, k, l, m = params
print (f'C:{C}')
print (f'k:{k}')
print (f'l:{l}')
print (f'm:{m}'）
