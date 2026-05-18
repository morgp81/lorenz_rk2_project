from numba import njit
from lorenz import lorenz

@njit
def euler(x0, y0, z0, sigma, rho, beta, h):
    k1_x, k1_y, k1_z = lorenz(x0, y0, z0, sigma, rho, beta)
    x = x0 + k1_x * h
    y = y0 + k1_y * h
    z = z0 + k1_z * h

    return x, y, z
