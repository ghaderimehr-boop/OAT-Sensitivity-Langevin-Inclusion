import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma
from matplotlib import rcParams


rcParams['font.family'] = 'serif'
rcParams['font.size'] = 12
plt.style.use('seaborn-v0_8-darkgrid')


custom_colors = ['black', 'red', 'blue']

# frac Caputo
def caputo_derivative(f, t, alpha, eps=1e-8):
    n = len(t)
    if n < 2:
        return np.zeros_like(f)
    
    h = t[1] - t[0]
    if h <= 0:
        return np.zeros_like(f)
    
    coeff = h**(-alpha)/gamma(2-alpha)
    sigma = np.array([(k+1)**(1-alpha) - k**(1-alpha) for k in range(n)])
    
    derivative = np.zeros(n)
    
    for i in range(1, n):
        diff = np.diff(f[:i+1])
        derivative[i] = coeff * np.sum(sigma[:i][::-1] * diff)
    
    return derivative

# function for fig
def create_sensitivity_plot(x, y_list, param_name, param_vals, colors=custom_colors):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    y_min = min([np.min(y[1:]) for y in y_list])
    y_max = max([np.max(y[1:]) for y in y_list])
    margin = 0.1 * (y_max - y_min)
    
    for y, val, color in zip(y_list, param_vals, colors):
        ax.plot(x[1:], y[1:], lw=2.5, color=color, 
               label=fr'${param_name}={val:.2f}$')
        ax.plot(x[0], y[0], 'o', color=color, markersize=4, alpha=0.5)
    
    ax.set_xlabel('t', fontsize=14)
    ax.set_ylabel(r' $\zeta(t)$', fontsize=14)
    ax.set_title(fr'Sensitivity Analysis: Variation in ${param_name}$', 
                fontsize=16, pad=20)
    ax.legend(fontsize=12, framealpha=0.9)
    ax.grid(True, alpha=0.3)
    ax.axhline(0, color='gray', linestyle='--', alpha=0.5)
    
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([y_min - margin, y_max + margin])
    
    return fig

# Sens Anal
def analyze_parameter(parameter_name, parameter_values, fixed_params):
    t = np.linspace(1e-6, 1, 500)  
    zeta = np.ones(len(t)) * 0.5
    
    zeta_vals = []
    for param_val in parameter_values:
        
        if parameter_name == r'\tau_1':
            tau1 = param_val
            tau2 = fixed_params['tau2']
            l = fixed_params['l']
        elif parameter_name == r'\tau_2':
            tau2 = param_val
            tau1 = fixed_params['tau1']
            l = fixed_params['l']
        elif parameter_name == r'\ell':
            l = param_val
            tau1 = fixed_params['tau1']
            tau2 = fixed_params['tau2']
        
        term = (zeta - alpha(t, zeta))/beta(t, zeta)
        D_term = caputo_derivative(term, t, tau2)
        DD_term = caputo_derivative(D_term + l*term - gamma_func(t, zeta), t, tau1)
        zeta_vals.append(DD_term)
    
    return create_sensitivity_plot(t, zeta_vals, parameter_name, parameter_values)

# functions
def alpha(t, z):
    return (1/100) * np.exp(-t/2) * np.sin(z)

def beta(t, z):
    return 1 + (np.arctan(z)/np.pi)

def gamma_func(t, z):
    return (1 + np.cos(2*np.pi*t/5)) * z / (10*(1 + z**2))

# Sens perform
if __name__ == "__main__":
    #  τ₁
    fig1 = analyze_parameter(r'\tau_1', [0.27, 0.6, 0.93],
                           {'tau2': 10/11, 'l': np.pi/2})
    fig1.savefig('sensitivity_tau1.png', dpi=600, bbox_inches='tight')  
    plt.close(fig1)      #  τ₂
    fig2 = analyze_parameter(r'\tau_2', [0.12, 0.41, 0.69],
                           {'tau1': 4/5, 'l': np.pi/2})
    fig2.savefig('sensitivity_tau2.png', dpi=600, bbox_inches='tight')  
    plt.close(fig2) 
    #  ℓ
    fig3 = analyze_parameter(r'\ell', [np.pi/2, 2*np.pi, 4*np.pi],
                           {'tau1': 4/5, 'tau2': 10/11})
    fig3.savefig('sensitivity_ell.png', dpi=600, bbox_inches='tight')  
    plt.close(fig3) 
    plt.show()
