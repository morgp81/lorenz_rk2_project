from euler_method import euler
from lorenz import lorenz 

def rk2(x0, y0, z0, sigma, rho, beta, h):
    k1_x, k1_y, k1_z = lorenz(x0, y0, z0, sigma, rho, beta)
    euler_x, euler_y, euler_z = euler(x0, y0, z0, sigma, rho, beta, h)
    k2_x, k2_y, k2_z = lorenz(euler_x, euler_y, euler_z, sigma, rho, beta)
    x = x0 + (k1_x + k2_x) * h / 2
    y = y0 + (k1_y + k2_y) * h / 2
    z = z0 + (k1_z + k2_z) * h / 2

    return x, y, z
