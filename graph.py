import numpy as np
import matplotlib.pyplot as plt

# Define the harmonics
n = np.array([0, 1, 2, 3])
T = 4  # Period of the signal
w0 = 2 * np.pi / T  # Fundamental angular frequency

# Fourier coefficients calculation
a0 = 1/2  # DC component a0

# Coefficients for n > 0 (only odd n have non-zero coefficients)
def b_n(n):
    return (4 / (n * np.pi)) * np.sin(n * np.pi / 2)

b = np.array([a0, b_n(1), 0, b_n(3)])  # Define Fourier coefficients for n = 0, 1, 2, 3

# Magnitude of Fourier components
magnitude = np.abs(b)

# Phase of Fourier components
phase = np.angle(b)

# Plotting magnitude and phase
fig, axs = plt.subplots(2, 1, figsize=(8, 6))

# Magnitude plot
axs[0].stem(n, magnitude, 'b', markerfmt='bo', basefmt=" ", use_line_collection=True)
axs[0].set_title('Magnitude of Fourier Components for n = 0 to n = 3')
axs[0].set_xlabel('Harmonic number n')
axs[0].set_ylabel('Magnitude')
axs[0].grid(True)

# Phase plot
axs[1].stem(n, phase, 'r', markerfmt='ro', basefmt=" ", use_line_collection=True)
axs[1].set_title('Phase of Fourier Components for n = 0 to n = 3')
axs[1].set_xlabel('Harmonic number n')
axs[1].set_ylabel('Phase (radians)')
axs[1].grid(True)

# Show plot
plt.tight_layout()
plt.show()
