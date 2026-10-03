"""
Sensitivity derivatives and Figure 13 generation.
Section 4.3 of the paper.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 12

ell_true  = np.pi
tau1_true = 0.8
tau2_true = 10/11

def zeta_model(t, ell, tau1, tau2):
    return np.exp(-ell * t**tau1) * np.cos(ell * t**tau2)

t = np.linspace(0.01, 1.0, 500)

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

S_ell, S_tau1, S_tau2 = sensitivity('ell'), sensitivity('tau1'), sensitivity('tau2')
St_ell, St_tau1, St_tau2 = S_ell*ell_true, S_tau1*tau1_true, S_tau2*tau2_true

# Figure 13
fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))
colors = ['#d62728', '#2ca02c', '#1f77b4']
labels = [r'$\ell$', r'$\tau_1$', r'$\tau_2$']

for ax, data, title, ylab in [
    (axes[0], [S_ell, S_tau1, S_tau2], '(a) Raw sensitivity functions', r'$S_p(t)$'),
    (axes[1], [St_ell, St_tau1, St_tau2], '(b) Normalized sensitivity functions', r'$\tilde{S}_p(t)$')
]:
    for d, c, l in zip(data, colors, labels):
        ax.plot(t, d, color=c, lw=2.2, label=l)
    ax.axhline(0, color='gray', lw=0.8, ls='--', alpha=0.5)
    ax.set_xlabel(r'$t$'); ax.set_ylabel(ylab)
    ax.set_title(title); ax.legend(framealpha=0.9); ax.grid(alpha=0.3)

plt.tight_layout()
plt.savefig('fig13.png', dpi=300, bbox_inches='tight')
plt.show()