from lorenz import lorenz
from euler_method import euler
from rk_methods import explicit_rk2, explicit_rk4, implicit_rk2

sigma = 10
rho = 28
beta = 8/3

x = 1
y = 2
z = 3

dx_dt, dy_dt, dz_dt = lorenz(x, y, z, sigma, rho, beta)

print(dx_dt, dy_dt, dz_dt)

euler_x, euler_y, euler_z = euler(x, y, z, sigma, rho, beta, 0.01)

print(euler_x, euler_y, euler_z)

rk2_x, rk2_y, rk2_z = explicit_rk2(x, y, z, sigma, rho, beta, 0.01)

print(rk2_x, rk2_y, rk2_z)

rk2_x, rk2_y, rk2_z = implicit_rk2(x, y, z, sigma, rho, beta, 0.01)

print(rk2_x, rk2_y, rk2_z)

rk4_x, rk4_y, rk4_z = explicit_rk4(x, y, z, sigma, rho, beta, 0.01)

print(rk4_x, rk4_y, rk4_z)