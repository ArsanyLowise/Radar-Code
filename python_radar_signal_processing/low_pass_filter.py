import numpy as np
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt

def lowpass_filter(data, cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = lfilter(b, a, data)
    return y

if __name__ == "__main__":
    # Example data: A noisy sine wave
    fs = 500.0       # Sample frequency (Hz)
    t = np.arange(0, 1.0, 1.0/fs)
    freq = 5.0       # Frequency of the sine wave (Hz)
    x = np.sin(2 * np.pi * freq * t) + 0.5 * np.random.randn(t.size)

    cutoff = 10.0    # Desired cutoff frequency of the filter (Hz)
    order = 6        # Filter order

    y = lowpass_filter(x, cutoff, fs, order)

    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(t, x, label='Noisy signal')
    plt.plot(t, y, label='Filtered signal', linewidth=2)
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid()
    plt.show()
