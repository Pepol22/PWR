import numpy as np
from scipy.stats import kurtosis, entropy
from nolds import dfa, hurst_rs

N = 500
np.random.seed(0)
time_series = np.random.rand(N)

print(f'Średnia: {np.mean(time_series)}')
print(f'Odchylenie standardowe: {np.std(time_series)}')
print(f'Wartość maksymalna: {np.max(time_series)}')
print(f'Wartość minimalna: {np.min(time_series)}')
print(f'Mediana: {np.median(time_series)}')
print(f'Kurtoza: {kurtosis(time_series)}')
print(f'Entropia: {entropy(time_series, base=2)}')  # base = 2 to log o podstawie 2
print(f'Wymiar fraktalny: {dfa(time_series)}')
print(f'Wykladnik Hursta {hurst_rs(time_series)}')

