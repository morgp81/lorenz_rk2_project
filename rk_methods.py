from euler_method import euler
from lorenz import lorenz 

def explicit_rk2(x0, y0, z0, sigma, rho, beta, h):
    k1_x, k1_y, k1_z = lorenz(x0, y0, z0, sigma, rho, beta)
    euler_x, euler_y, euler_z = euler(x0, y0, z0, sigma, rho, beta, h)
    k2_x, k2_y, k2_z = lorenz(euler_x, euler_y, euler_z, sigma, rho, beta)
    x = x0 + (k1_x + k2_x) * h / 2
    y = y0 + (k1_y + k2_y) * h / 2
    z = z0 + (k1_z + k2_z) * h / 2

    return x, y, z

def implicit_rk2(x0, y0, z0, sigma, rho, beta, h):
    x,y,z = euler(x0, y0, z0, sigma, rho, beta, h)
    for i in range(10):
        mid_x = (x0 + x) / 2
        mid_y = (y0 + y) / 2
        mid_z = (z0 + z) / 2
        lorenz_mid_x, lorenz_mid_y, lorenz_mid_z = lorenz(mid_x, mid_y, mid_z, sigma, rho, beta)
        new_x = x0 + lorenz_mid_x * h
        new_y = y0 + lorenz_mid_y * h
        new_z = z0 + lorenz_mid_z * h
        if abs(new_x - x) < 1e-6 and abs(new_y - y) < 1e-6 and abs(new_z - z) < 1e-6:
            x,y,z = new_x, new_y, new_z
            break
        else:
            x,y,z = new_x, new_y, new_z

    return x, y, z

def explicit_rk4(x0, y0, z0, sigma, rho, beta, h):
    k1_x, k1_y, k1_z = lorenz(x0, y0, z0, sigma, rho, beta)
    euler_x1 = x0 + k1_x * h / 2
    euler_y1 = y0 + k1_y * h / 2
    euler_z1 = z0 + k1_z * h / 2
    k2_x, k2_y, k2_z = lorenz(euler_x1, euler_y1, euler_z1, sigma, rho, beta)
    euler_x2 = x0 + k2_x * h / 2
    euler_y2 = y0 + k2_y * h / 2
    euler_z2 = z0 + k2_z * h / 2
    k3_x, k3_y, k3_z = lorenz(euler_x2, euler_y2, euler_z2, sigma, rho, beta)
    euler_x3 = x0 + k3_x * h
    euler_y3 = y0 + k3_y * h
    euler_z3 = z0 + k3_z * h
    k4_x, k4_y, k4_z = lorenz(euler_x3, euler_y3, euler_z3, sigma, rho, beta)
    x = x0 + (k1_x + 2*k2_x + 2*k3_x + k4_x) * h / 6
    y = y0 + (k1_y + 2*k2_y + 2*k3_y + k4_y) * h / 6
    z = z0 + (k1_z + 2*k2_z + 2*k3_z + k4_z) * h / 6

    return x, y, z