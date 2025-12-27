import numpy as np
from scipy.constants import hbar, k, e, m_e
from scipy.integrate import trapezoid

# -----------------------------
# Band structure functions
# -----------------------------

def band_energy(k, m_eff):
    return hbar**2 * k**2 / (2 * m_eff)

def velocity_squared(E, m_eff):
    return 2 * E / m_eff

def density_of_states(E, m_eff):
    prefactor = (1 / (2 * np.pi**2)) * (2 * m_eff / hbar**2)**(3/2)
    return prefactor * np.sqrt(E)

# -----------------------------
# Fermi functions
# -----------------------------

def fermi(E, mu, T):
    return 1 / (1 + np.exp((E - mu) / (k * T)))

def dfermi_dE(E, mu, T):
    f = fermi(E, mu, T)
    return -f * (1 - f) / (k * T)

# -----------------------------
# Scattering model (CRTA)
# -----------------------------

def scattering_time(E, tau0=1e-14, r=0):
    return tau0 * (E / e)**r

# -----------------------------
# Transport coefficients
# -----------------------------

def transport_coefficients(T, mu, m_eff, tau0=1e-14, r=0):
    E = np.linspace(1e-5*e, 1.0*e, 3000)

    v2 = velocity_squared(E, m_eff)
    g = density_of_states(E, m_eff)
    tau = scattering_time(E, tau0, r)
    df = -dfermi_dE(E, mu, T)

    integrand0 = v2 * tau * g * df
    integrand1 = (E - mu) * integrand0

    L0 = trapezoid(integrand0, E)
    L1 = trapezoid(integrand1, E)

    sigma = e**2 * L0
    S = -L1 / (e * T * L0)
    PF = sigma * S**2

    return sigma, S, PF

# -----------------------------
# Bandstructure (for plotting)
# -----------------------------

def bandstructure(m_eff, kmax=1e10, nk=1000):
    k = np.linspace(-kmax, kmax, nk)
    E = band_energy(k, m_eff) / e  # eV
    return k*1e-10, E  # 1/Å, eV