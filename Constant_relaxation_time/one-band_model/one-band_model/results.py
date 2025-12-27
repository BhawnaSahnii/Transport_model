import numpy as np
import matplotlib.pyplot as plt
from transport import bandstructure, transport_coefficients
from scipy.constants import e, m_e

# Parameters
m_eff = 0.2 * m_e
mu = 0.05 * e
T_vals = np.linspace(300, 900, 100)

# -----------------------------
# Plot bandstructure
# -----------------------------

k, E = bandstructure(m_eff)

plt.figure()
plt.plot(k, E)
plt.xlabel("k (1/Å)")
plt.ylabel("Energy (eV)")
plt.title("Parabolic Band Structure")
plt.grid()
plt.show()

# -----------------------------
# Transport vs temperature
# -----------------------------

sigma_vals = []
S_vals = []
PF_vals = []

for T in T_vals:
    sigma, S, PF = transport_coefficients(T, mu, m_eff)
    sigma_vals.append(sigma)
    S_vals.append(S*1e6)  # µV/K
    PF_vals.append(PF * 1e3)  # mW m^-1 K^-2

plt.figure()
plt.plot(T_vals, sigma_vals)
plt.xlabel("Temperature (K)")
plt.ylabel("Conductivity (S/m)")
plt.show()

plt.figure()
plt.plot(T_vals, S_vals)
plt.xlabel("Temperature (K)")
plt.ylabel("Seebeck (µV/K)")
plt.show()

plt.figure()
plt.plot(T_vals, PF_vals)
plt.xlabel("Temperature (K)")
plt.ylabel("Power Factor (mW m$^{-1}$ K$^{-2}$)")
plt.show()
