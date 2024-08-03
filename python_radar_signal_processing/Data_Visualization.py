# Using Matplotlib, write a script to plot the amplitude spectrum of a radar signal:
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

signal = np.array([0, 1, 0, -1])
n = len(signal)
freq = np.fft.fftfreq(n)
amplitude = np.abs(fft(signal))

plt.plot(freq, amplitude)
plt.title('Amplitude Spectrum')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.show()

# How would you visualize complex data (e.g., 3D plots, heatmaps)?
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

ax.plot_surface(X, Y, Z)
plt.show()

# Visualize using Heatmap

import seaborn as sns

data = np.random.rand(10, 12)
sns.heatmap(data)
plt.show()
