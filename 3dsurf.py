import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

# تنظیمات فونت و لاتک
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['mathtext.fontset'] = 'stix'  # فونت مخصوص فرمول‌های ریاضی
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14

# تعریف توابع (بدون تغییر)
def alpha_func(t, z):
    return (1/201) * np.exp(-(np.sin(np.pi*t/2)**2)/(1+np.sin(np.pi*t/2)**2)) * (0.25*z + 1)

def beta_func(t, z):
    return (np.exp(-np.log(t+14)**2) * np.abs(z)) / (1+np.abs(z)) + (1/(125+271*t)) * np.exp(-np.pi*t)

def gamma_func(t, z):
    return (np.cos(np.pi*t)/(173*(1+t**2))) * (z + (1/3)*np.exp(-t**2))

# ایجاد داده‌های شبکه
t = np.linspace(0, 1, 100)
z = np.linspace(-2, 2, 100)
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
    
    # 3. غیرفعال کردن tight_layout اگر خطا می‌دهد
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)  # تنظیم دستی حاشیه‌ها
    plt.show()

# ----------------------------------------------------------------------------------
# نکته کلیدی: استفاده از raw strings (r قبل از عنوان) برای فرمول‌های لاتک
# ----------------------------------------------------------------------------------
plot_function_with_contour(alpha_func,
                         surface_title=r"3D Surface of $\alpha(t,\zeta)$",  # استفاده از r
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


