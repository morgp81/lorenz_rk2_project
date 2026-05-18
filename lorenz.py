import numpy as np
from numba import njit

@njit
def lorenz(x, y, z, sigma, rho, beta):
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z

    return dx_dt, dy_dt, dz_dt