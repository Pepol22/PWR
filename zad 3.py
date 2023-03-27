import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import entropy
from nolds import dfa, hurst_rs

# Generowanie szeregu czasowego
N = 500
h = 25  # szerokość okna
np.random.seed(0)
time_series = np.random.rand(N)
t = np.arange(N)

# Tworzenie ramki danych, i obliczanie danych statystycznych na oknie przesuwnym o zadanym h
data = pd.DataFrame(time_series)
rolling_window = data[0].rolling(window=h, min_periods=1)
rolling_window_mean = rolling_window.mean()
rolling_window_std_deviation = rolling_window.std()
rolling_window_min = rolling_window.min()
rolling_window_max = rolling_window.max()
rolling_window_median = rolling_window.median()
rolling_window_kurtosis = rolling_window.kurt()
rolling_window_entropy = rolling_window.apply(lambda x: entropy(x, base=2))
rolling_window_hurst_exponent = rolling_window.apply(lambda x: hurst_rs(x))
rolling_window = data[0].rolling(window=h, min_periods=5)
rolling_window_fractal_dimension = rolling_window.apply(lambda x: dfa(x))

x_ticks = [25*i for i in range(int(N/25)+1)]

plt.style.use('ggplot')
plt.title("Srednia i odchylenie standardowe na tle danych dla h=" + str(h))
plt.plot(t, time_series, label='Szereg czasowy', color = 'blue', alpha=0.8)
plt.plot(t, rolling_window_mean, linewidth=3, color = 'tab:orange', label = 'Srednia')
plt.fill_between(t,  rolling_window_mean - rolling_window_std_deviation, rolling_window_mean + rolling_window_std_deviation, color='tab:orange', alpha = 0.6, label = 'Odchylenie standardowe')
plt.legend()
plt.xticks(x_ticks)
plt.xlim(0, N)



plt.style.use('ggplot')
fig1, ax1 = plt.subplots(nrows=4, ncols=1, figsize=(10, 3))
fig1.suptitle('Ilustracja zmian pozostalych danych statystycznych z zadania pierwszego na oknie przesuwnym dla h=' + str(h))

ax1[0].set_title('Wartosc maksymalna')
ax1[0].plot(t, rolling_window_max, color='red', linewidth=3)
ax1[0].set_xlim(0, N)

ax1[1].set_title('Wartosc minimalna')
ax1[1].plot(t, rolling_window_min, color='blue', linewidth=3)
ax1[1].set_xlim(0, N)

ax1[2].set_title('Mediana')
ax1[2].plot(t, rolling_window_median, color='green', linewidth=3)
ax1[2].set_xlim(0, N)

ax1[3].set_title('Kurtoza')
ax1[3].plot(t, rolling_window_kurtosis, color='orange', linewidth=3)
ax1[3].set_xlim(0, N)



plt.style.use('ggplot')
fig2, ax2 = plt.subplots(nrows=3, ncols=1, figsize=(10, 3))
fig2.suptitle('Ilustracja zmian pozostalych danych statystycznych z zadania drugiego na oknie przesuwnym dla h=' + str(h))

ax2[0].set_title('Entropia')
ax2[0].plot(t, rolling_window_entropy, color='red', linewidth=3)
ax2[0].set_xlim(0, N)

ax2[1].set_title('Wymiar fraktalny')
ax2[1].plot(t, rolling_window_fractal_dimension, color='blue', linewidth=3)
ax2[1].set_xlim(0, N)

ax2[2].set_title('Wykladnik Hursta')
ax2[2].plot(t, rolling_window_hurst_exponent, color='green', linewidth=3)
ax2[2].set_xlim(0, N)

plt.show()
