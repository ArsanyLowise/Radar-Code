import numpy as np
import matplotlib.pyplot as plt

def simulate_radar_signal(length, noise_level):
    signal = np.sin(np.linspace(0, 2 * np.pi, length))
    noise = np.random.normal(0, noise_level, length)
    return signal + noise

def snr(signal, noise):
    signal_power = np.mean(signal**2)
    noise_power = np.mean(noise**2)
    return 10 * np.log10(signal_power / noise_power)

# Parameters
length = 1000
noise_level = 0.5

# Simulate radar signal
radar_signal = simulate_radar_signal(length, noise_level)
original_signal = np.sin(np.linspace(0, 2 * np.pi, length))
noise = radar_signal - original_signal

# Calculate SNR
signal_to_noise_ratio = snr(original_signal, noise)
print(f"SNR: {signal_to_noise_ratio:.2f} dB")

# Plot the results
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(original_signal, label='Original Signal')
plt.plot(radar_signal, label='Radar Signal with Noise', alpha=0.7)
plt.title('Radar Signal vs Original Signal')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(noise, label='Noise')
plt.title('Noise')
plt.legend()

plt.tight_layout()
plt.show()
