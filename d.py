import numpy as np
import matplotlib.pyplot as plt

# Define the period and fundamental frequency
T = 3
omega_0 = 2 * np.pi / T

# Compute a0
a0 = 2 / 3  # From earlier calculation

# Define a function to compute an and bn
def an_bn(n):
    # Compute an and bn based on the integral results for cosine and sine terms
    an = (2 / 3) * (np.sin(n * np.pi / 3) / (n * np.pi / 3))
    bn = (2 / 3) * ((1 - np.cos(n * np.pi / 3)) / (n * np.pi / 3))
    return an, bn

# Compute Fourier coefficients for n = 0 to 3
n_values = np.arange(4)
a_values = [a0]
b_values = [0]  # No sine term for n=0

for n in range(1, 4):
    an, bn = an_bn(n)
    a_values.append(an)
    b_values.append(bn)

# Compute magnitudes |Cn|
C_values = np.sqrt(np.array(a_values)**2 + np.array(b_values)**2)

# Plot the magnitude of Fourier coefficients |Cn|
plt.stem(n_values, C_values, basefmt=" ", use_line_collection=True)
plt.title("Magnitude of Fourier Coefficients |Cn| for n = 0 to 3")
plt.xlabel("n")
plt.ylabel("|Cn|")
plt.grid(True)
plt.show()

# Return the computed values
a_values, b_values, C_values
import numpy as np
import matplotlib.pyplot as plt

# Define the period and fundamental frequency
T = 3
omega_0 = 2 * np.pi / T

# Compute a0
a0 = 2 / 3  # From earlier calculation

# Define a function to compute an and bn
def an_bn(n):
    # Compute an and bn based on the integral results for cosine and sine terms
    an = (2 / 3) * (np.sin(n * np.pi / 3) / (n * np.pi / 3))
    bn = (2 / 3) * ((1 - np.cos(n * np.pi / 3)) / (n * np.pi / 3))
    return an, bn

# Compute Fourier coefficients for n = 0 to 3
n_values = np.arange(4)
a_values = [a0]
b_values = [0]  # No sine term for n=0

for n in range(1, 4):
    an, bn = an_bn(n)
    a_values.append(an)
    b_values.append(bn)

# Compute magnitudes |Cn|
C_values = np.sqrt(np.array(a_values)**2 + np.array(b_values)**2)

# Plot the magnitude of Fourier coefficients |Cn|
plt.stem(n_values, C_values, basefmt=" ", use_line_collection=True)
plt.title("Magnitude of Fourier Coefficients |Cn| for n = 0 to 3")
plt.xlabel("n")
plt.ylabel("|Cn|")
plt.grid(True)
plt.show()

# Return the computed values
a_values, b_values, C_values
