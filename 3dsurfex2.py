import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

# تنظیمات فونت و لاتک
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14

# تعریف توابع جدید مطابق معادلات شما
def alpha_func(t, z):
    return (1/100) * np.exp(-t/2) * np.sin(z)

def beta_func(t, z):
    return 1 + (np.arctan(z)/np.pi)

def gamma_func(t, z):
    return (1 + np.cos(2*np.pi*t/5)) * z / (10*(1 + z**2))

# ایجاد داده‌های شبکه
t = np.linspace(0, 1, 100)
z = np.linspace(-5, 5, 100)
T, Z = np.meshgrid(t, z)

def plot_function_with_contour(func, surface_title, contour_title, cmap, zlabel=None):
    fig = plt.figure(figsize=(16, 6))
    values = func(T, Z)
    
    # 1. نمودار 3D
    ax1 = fig.add_subplot(121, projection='3d')
    surf = ax1.plot_surface(T, Z, values, cmap=cmap, linewidth=0, antialiased=True, alpha=0.8)
    ax1.set_title(surface_title, pad=15)
    ax1.set_xlabel('$t$')
    ax1.set_ylabel(r'$\zeta$')
    ax1.set_zlabel(zlabel if zlabel else r'Value')
    fig.colorbar(surf, ax=ax1, shrink=0.5, aspect=10)
    
    # 2. نمودار کانتور
    ax2 = fig.add_subplot(122)
    contour = ax2.contourf(T, Z, values, 20, cmap=cmap)
    ax2.set_title(contour_title, pad=15)
    ax2.set_xlabel('$t$')
    ax2.set_ylabel(r'$\zeta$')
    fig.colorbar(contour, ax=ax2, shrink=0.5, aspect=10)
    
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.show()

# رسم نمودارها با توابع جدید
plot_function_with_contour(alpha_func,
                         surface_title=r"3D Surface of $\alpha(t,\zeta)$",
                         contour_title=r"Contour Levels of $\alpha(t,\zeta)$",
                         cmap=cm.coolwarm,
                         zlabel=r"$\alpha(t,\zeta)$")

plot_function_with_contour(beta_func,
                         surface_title=r"3D Surface of $\beta(t,\zeta)$",
                         contour_title=r"Contour Levels of $\beta(t,\zeta)$",
                         cmap=cm.viridis,
                         zlabel=r"$\beta(t,\zeta)$")

plot_function_with_contour(gamma_func,
                         surface_title=r"3D Surface of $\gamma(t,\zeta)$",
                         contour_title=r"Contour Levels of $\gamma(t,\zeta)$",
                         cmap=cm.plasma,
                         zlabel=r"$\gamma(t,\zeta)$")
