from euler_method import euler
from lorenz import lorenz 

def rk2(dx, dy, dz, x0, y0, z0, h, sigma, rho, beta):
    k1_x = dx
    k1_y = dy
    k1_z = dz
    euler_x, euler_y, euler_z = euler(k1_x, k1_y, k1_z, x0, y0, z0, h)
    k2_x, k2_y, k2_z = lorenz(euler_x, euler_y, euler_z, sigma, rho, beta)
    x = x0 + (k1_x + k2_x) * h / 2
    y = y0 + (k1_y + k2_y) * h / 2
    z = z0 + (k1_z + k2_z) * h / 2

    return x, y, z
