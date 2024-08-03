import matplotlib.pyplot as plt
import numpy as np

# Define the parameters
A = 1  # Amplitude of the pulse
tau = 1  # Duration of the pulse

# Define the time axis
t = np.linspace(0, 2 * tau, 1000)

# Define the original pulse x(t)
x_t = np.piecewise(t, [t < 0, (t >= 0) & (t <= tau), t > tau], [0, A, 0])

# Define the impulse response h(t)
h_t = np.piecewise(t, [t < 0, (t >= 0) & (t <= tau), t > tau], [0, A, 0])

# Define the matched filter response y(t)
y_t = np.piecewise(t, [t < 0, (t >= 0) & (t <= tau), (t > tau) & (t <= 2 * tau), t > 2 * tau], [0, lambda t: A**2 * t, lambda t: A**2 * (2 * tau - t), 0])

# Plot the original pulse x(t)
plt.figure(figsize=(12, 6))
plt.subplot(3, 1, 1)
plt.plot(t, x_t, 'b--', label='x(t)')
plt.title('Original Pulse x(t)')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid(True)
plt.legend()

# Plot the impulse response h(t)
plt.subplot(3, 1, 2)
plt.plot(t, h_t, 'g--', label='h(t)')
plt.title('Impulse Response h(t)')
plt.xlabel('t')
plt.ylabel('h(t)')
plt.grid(True)
plt.legend()

# Plot the matched filter response y(t)
plt.subplot(3, 1, 3)
plt.plot(t, y_t, 'r--', label='y(t)')
plt.title('Matched Filter Response y(t)')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid(True)
plt.legend()

# Adjust layout and show the plots
plt.tight_layout()
plt.show()
