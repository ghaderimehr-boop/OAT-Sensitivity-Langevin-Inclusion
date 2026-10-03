"""
Parameter identification with noisy synthetic observations.
Section 4.3 of the paper.
"""
import numpy as np
from scipy.optimize import least_squares

ell_true  = np.pi
tau1_true = 0.8
tau2_true = 10/11

def zeta_model(t, ell, tau1, tau2):
    return np.exp(-ell * t**tau1) * np.cos(ell * t**tau2)

t = np.linspace(0.01, 1.0, 200)
zeta_true = zeta_model(t, ell_true, tau1_true, tau2_true)

def residual(params, zeta_obs):
    return zeta_model(t, *params) - zeta_obs

errors = []
for seed in range(20):
    rng = np.random.default_rng(seed=seed)
    zeta_obs = zeta_true + 0.02 * rng.standard_normal(len(t))
    x0 = [ell_true*1.10, tau1_true*0.95, tau2_true*1.05]
    bounds = ([0.1,0.1,0.1],[10,0.99,0.99])
    res = least_squares(residual, x0, args=(zeta_obs,), bounds=bounds)
    e = res.x
    errors.append([100*abs(e[0]-ell_true)/ell_true,
                   100*abs(e[1]-tau1_true)/tau1_true,
                   100*abs(e[2]-tau2_true)/tau2_true])

errors = np.array(errors)
print("Mean relative errors (%):")
print(f"  ell  = {errors[:,0].mean():.2f}")
print(f"  tau1 = {errors[:,1].mean():.2f}")
print(f"  tau2 = {errors[:,2].mean():.2f}")
print("\nStandard deviations (%):")
print(f"  ell  = {errors[:,0].std():.2f}")
print(f"  tau1 = {errors[:,1].std():.2f}")
print(f"  tau2 = {errors[:,2].std():.2f}")