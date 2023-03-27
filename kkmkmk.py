import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import entropy
from nolds import dfa, hurst_rs

# Generowanie szeregu czasowego
N = 100
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
rolling_window_entropy = rolling_window.apply(lambda x: entropy(time_series, base=2))
rolling_window_hurst = rolling_window.apply(lambda x: hurst_rs(time_series))
rolling_window_dfa = rolling_window.apply(lambda x: dfa(time_series))

x_ticks = [25*i for i in range(int(N/25)+1)]

plt.style.use('ggplot')
fig, axs = plt.subplots(2, 2, figsize=(240, 120))
fig.suptitle('Porównanie danych przed i po normalizacji oraz standaryzacji', fontsize=20)

# Plot dla danych oryginalnych
axs[0, 0].plot(t, time_series, label='Szereg czasowy', color = 'blue', alpha=0.8)
axs[0, 0].plot(t, rolling_window_mean, linewidth=1, color = 'tab:orange', label = 'Srednia')
axs[0, 0].plot(t,rolling_window_min , linewidth=1, label = 'Minimum')
axs[0, 0].plot(t, rolling_window_max, linewidth=1, label = 'Maksimum')
axs[0, 0].plot(t,rolling_window_median, linewidth=1, label = 'Mediana')
axs[0, 0].plot(t, rolling_window_kurtosis, linewidth=1, label = 'Kurtoza')
axs[0, 0].plot(t, rolling_window_entropy, linewidth=1, label = 'Entropia')
axs[0, 0].plot(t, rolling_window_hurst, linewidth=1, label = 'Wykładnik Hursta')
axs[0, 0].plot(t, rolling_window_dfa, linewidth=1, label = 'Wymiar fraktalny')
axs[0, 0].fill_between(t, rolling_window_mean - rolling_window_std_deviation, rolling_window_mean + rolling_window_std_deviation, color='tab:orange', alpha = 0.6, label = 'Odchylenie standardowe')
axs[0, 0].legend()
axs[0, 0].set_xlim(0, N)
axs[0, 0].set_title("Wykres przed normalizacją/standaryzacją")

normalized_data = (data - data.min()) / (data.max() - data.min())
rolling_window_normalized = normalized_data[0].rolling(window=h, min_periods=1)
rolling_window_normalized_mean = rolling_window_normalized.mean()
rolling_window_normalized_std_deviation = rolling_window_normalized.std()
rolling_window_normalized_min = rolling_window_normalized.min()
rolling_window_normalized_max = rolling_window_normalized.max()
rolling_window_normalized_median = rolling_window_normalized.median()
rolling_window_normalized_kurtosis = rolling_window_normalized.kurt()
rolling_window_normalized_entropy = rolling_window_normalized.apply(lambda x: entropy(normalized_data[0], base=2))
rolling_window_hurst_normalized = rolling_window_normalized.apply(lambda x: hurst_rs(normalized_data[0]))
rolling_window_dfa_normalized = rolling_window_normalized.apply(lambda x: dfa(normalized_data[0]))

axs[0, 1].plot(t, normalized_data[0], label='Szereg czasowy', color = 'blue', alpha=0.8)
axs[0, 1].plot(t, rolling_window_normalized_mean, linewidth=1, color = 'tab:orange', label = 'Srednia')
axs[0, 1].plot(t, rolling_window_normalized_min, linewidth=1, label = 'Minimum')
axs[0, 1].plot(t, rolling_window_normalized_max, linewidth=1, label = 'Maksimum')
axs[0, 1].plot(t, rolling_window_normalized_median, linewidth=1, label = 'Mediana')
axs[0, 1].plot(t, rolling_window_normalized_kurtosis, linewidth=1, label = 'Kurtoza')
axs[0, 1].plot(t, rolling_window_normalized_entropy, linewidth=1, label = 'Entropia')
axs[0, 1].plot(t, rolling_window_hurst_normalized, linewidth=1, label = 'Wykładnik Hursta')
axs[0, 1].plot(t, rolling_window_dfa_normalized, linewidth=1, label = 'Wymiar fraktalny')
axs[0, 1].fill_between(t, rolling_window_normalized_mean - rolling_window_normalized_std_deviation, rolling_window_normalized_mean + rolling_window_normalized_std_deviation, color='tab:orange', alpha = 0.6, label = 'Odchylenie standardowe')
axs[0, 1].legend()
axs[0, 1].set_xlim(0, N)
axs[0, 1].set_title("Wykres po normalizacji")

# Standaryzacja danych
standardized_data = (data - data.mean()) / data.std()
rolling_window_standardized = standardized_data[0].rolling(window=h, min_periods=1)
rolling_window_standardized_mean = rolling_window_standardized.mean()
rolling_window_standardized_std_deviation = rolling_window_standardized.std()
rolling_window_standardized_min = rolling_window_standardized.min()
rolling_window_standardized_max = rolling_window_standardized.max()
rolling_window_standardized_median = rolling_window_standardized.median()
rolling_window_standardized_kurtosis = rolling_window_standardized.kurt()
rolling_window_standardized_entropy = rolling_window_standardized.apply(lambda x: entropy(standardized_data[0], base=2))
rolling_window_standardized_hurst = rolling_window_normalized.apply(lambda x: hurst_rs(standardized_data[0]))
rolling_window_standardized_dfa = rolling_window_normalized.apply(lambda x: dfa(standardized_data[0]))
# Wizualizacja danych po standaryzacji
axs[1, 0].plot(t, standardized_data[0], label='Szereg czasowy', color = 'blue', alpha=0.8)
axs[1, 0].plot(t, rolling_window_standardized_mean, linewidth=1, color = 'tab:orange', label = 'Srednia')
axs[1, 0].plot(t,rolling_window_standardized_min , linewidth=1, label = 'Minimum')
axs[1, 0].plot(t, rolling_window_standardized_max, linewidth=1, label = 'Maksimum')
axs[1, 0].plot(t, rolling_window_standardized_median, linewidth=1, label = 'Mediana')
axs[1, 0].plot(t, rolling_window_standardized_kurtosis, linewidth=1, label = 'Kurtoza')
axs[1, 0].plot(t, rolling_window_standardized_entropy, linewidth=1, label = 'Entropia')
axs[1, 0].plot(t, rolling_window_standardized_hurst, linewidth=1, label = 'Wykładnik Hursta')
axs[1, 0].plot(t, rolling_window_standardized_dfa, linewidth=1, label = 'Wymiar fraktalny')
axs[1, 0].fill_between(t, rolling_window_standardized_mean - rolling_window_standardized_std_deviation, rolling_window_standardized_mean + rolling_window_standardized_std_deviation, color='tab:orange', alpha = 0.6, label = 'Odchylenie standardowe')
axs[1, 0].legend()
axs[1, 0].set_xlim(0, N)
axs[1, 0].set_title("Standaryzacja")
plt.show()

def generate_graph(axs,index, t, data,standardized_data,normalized_data,label):
    axs[index, 0].plot(t, data, linewidth=1, color='tab:orange', label=label)
    axs[index, 0].legend()
    axs[index, 0].set_xlim(0, N)
    axs[index, 0].set_title(label)

    axs[index, 1].plot(t, standardized_data, linewidth=1, color='tab:orange', label=label)
    axs[index, 1].legend()
    axs[index, 1].set_xlim(0, N)
    axs[index, 1].set_title(label)

    axs[index,2].plot(t, normalized_data, linewidth=1, color='tab:orange', label=label)
    axs[index, 2].legend()
    axs[index, 2].set_xlim(0, N)
    axs[index, 2].set_title(label)

ilosc_cech = 9
fig, axs = plt.subplots(ilosc_cech, 3, figsize=(24, 12))
generate_graph(axs,0,t, rolling_window_mean, rolling_window_standardized_mean, rolling_window_normalized_mean, "Średnia")
generate_graph(axs,1,t, rolling_window_min, rolling_window_standardized_min, rolling_window_normalized_min, "Minimum")
generate_graph(axs,2,t, rolling_window_max, rolling_window_standardized_max, rolling_window_normalized_max, "Maksimum")
generate_graph(axs,3,t, rolling_window_median, rolling_window_standardized_median, rolling_window_normalized_median, "Mediana")
generate_graph(axs,4,t, rolling_window_kurtosis, rolling_window_standardized_kurtosis, rolling_window_normalized_kurtosis, "Kurtoza")
generate_graph(axs,5,t, rolling_window_entropy, rolling_window_standardized_entropy, rolling_window_normalized_entropy, "Entropia")
generate_graph(axs,6,t, rolling_window_hurst, rolling_window_standardized_hurst, rolling_window_hurst_normalized, "Wykładnik Hursta")
generate_graph(axs,7,t, rolling_window_dfa, rolling_window_standardized_dfa, rolling_window_dfa_normalized, "Wymiar fraktalny")
generate_graph(axs,8,t, rolling_window_std_deviation, rolling_window_standardized_std_deviation, rolling_window_normalized_std_deviation, "Odchylenie standardowe")
plt.show()