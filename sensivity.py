import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams


rcParams['font.family'] = 'serif'
rcParams['font.size'] = 12

plt.style.use('seaborn-v0_8-darkgrid')

# functiona and parameter
t_vals = np.linspace(0, 2, 500)
tau1_vals = [0.7, 0.8, 0.9]
tau2_vals = [0.7, 0.8, 0.9]
ell_vals = [np.pi/2, np.pi, 2*np.pi]

def zeta_solution(t, tau1, tau2, ell):
    return np.exp(-ell * t**tau1) * np.cos(ell * t**tau2)


custom_colors = ['black', 'red', 'blue']

# fig
def create_sensitivity_plot(x, y_list, param_name, param_vals, colors=custom_colors):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    for y, val, color in zip(y_list, param_vals, colors):
        ax.plot(x, y, lw=2.5, color=color, 
               label=fr'${param_name}={val:.2f}$')
    
    ax.set_xlabel('Time (t)', fontsize=14)
    ax.set_ylabel(r' $\zeta(t)$', fontsize=14)
    ax.set_title(fr'Sensitivity Analysis: Variation in ${param_name}$', 
                fontsize=16, pad=20)
    ax.legend(fontsize=12, framealpha=0.9)
    ax.grid(True, alpha=0.3)
    ax.axhline(0, color='gray', linestyle='--', alpha=0.5)
    
    return fig

# sens τ1
zeta_tau1 = [zeta_solution(t_vals, tau1, 4/5, np.pi) for tau1 in tau1_vals]
fig1 = create_sensitivity_plot(t_vals, zeta_tau1, r'\tau_1', tau1_vals)

# sens τ2
zeta_tau2 = [zeta_solution(t_vals, 4/5, tau2, np.pi) for tau2 in tau2_vals]
fig2 = create_sensitivity_plot(t_vals, zeta_tau2, r'\tau_2', tau2_vals)

# sens ℓ
zeta_ell = [zeta_solution(t_vals, 4/5, 10/11, ell) for ell in ell_vals]
fig3 = create_sensitivity_plot(t_vals, zeta_ell, r'\ell', ell_vals)

plt.tight_layout()
plt.show()
