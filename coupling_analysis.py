"""
Coupling matrix, cosine similarities, and condition number.
Section 4.3 of the paper.
"""
import numpy as np

ell_true  = np.pi
tau1_true = 0.8
tau2_true = 10/11

def zeta_model(t, ell, tau1, tau2):
    return np.exp(-ell * t**tau1) * np.cos(ell * t**tau2)

t = np.linspace(0.01, 1.0, 500)
dt = t[1] - t[0]

def sensitivity(param, h=1e-5):
    if param == 'ell':
        zp = zeta_model(t, ell_true + h, tau1_true, tau2_true)
        zm = zeta_model(t, ell_true - h, tau1_true, tau2_true)
    elif param == 'tau1':
        zp = zeta_model(t, ell_true, tau1_true + h, tau2_true)
        zm = zeta_model(t, ell_true, tau1_true - h, tau2_true)
    else:
        zp = zeta_model(t, ell_true, tau1_true, tau2_true + h)
        zm = zeta_model(t, ell_true, tau1_true, tau2_true - h)
    return (zp - zm) / (2 * h)

S_ell  = sensitivity('ell')  * ell_true
S_tau1 = sensitivity('tau1') * tau1_true
S_tau2 = sensitivity('tau2') * tau2_true

def L2_norm(S): return np.sqrt(np.sum(S**2) * dt)
def cosine(S1, S2): return np.sum(S1*S2)*dt / (L2_norm(S1)*L2_norm(S2))

print("Normalized L2 norms:")
print(f"  ||S_ell||  = {L2_norm(S_ell):.4f}")
print(f"  ||S_tau1|| = {L2_norm(S_tau1):.4f}")
print(f"  ||S_tau2|| = {L2_norm(S_tau2):.4f}")

print("\nPairwise coupling |cos theta|:")
c_ell_tau1  = abs(cosine(S_ell,  S_tau1))
c_ell_tau2  = abs(cosine(S_ell,  S_tau2))
c_tau1_tau2 = abs(cosine(S_tau1, S_tau2))
print(f"  |cos(ell, tau1)|  = {c_ell_tau1:.4f}")
print(f"  |cos(ell, tau2)|  = {c_ell_tau2:.4f}")
print(f"  |cos(tau1, tau2)| = {c_tau1_tau2:.4f}")

D = np.array([[1, c_ell_tau1, c_ell_tau2],
              [c_ell_tau1, 1, c_tau1_tau2],
              [c_ell_tau2, c_tau1_tau2, 1]])
eig = np.linalg.eigvalsh(D)
print("\nEigenvalues of D:", eig)
print(f"Condition number: {eig[-1]/eig[0]:.2f}")