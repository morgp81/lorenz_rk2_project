import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
import numpy as np
from numba import njit
from rk_methods import explicit_rk2, implicit_rk2


@njit
def run_explicit_rk2(x0, y0, z0, sigma, rho, beta, dt, number_of_steps):
    x_values = np.empty(number_of_steps)
    y_values = np.empty(number_of_steps)
    z_values = np.empty(number_of_steps)

    x = x0
    y = y0
    z = z0

    for i in range(number_of_steps):
        x, y, z = explicit_rk2(x, y, z, sigma, rho, beta, dt)

        x_values[i] = x
        y_values[i] = y
        z_values[i] = z

    return x_values, y_values, z_values


@njit
def run_implicit_rk2(x0, y0, z0, sigma, rho, beta, dt, number_of_steps):
    x_values = np.empty(number_of_steps)
    y_values = np.empty(number_of_steps)
    z_values = np.empty(number_of_steps)

    x = x0
    y = y0
    z = z0

    for i in range(number_of_steps):
        x, y, z = implicit_rk2(x, y, z, sigma, rho, beta, dt)

        x_values[i] = x
        y_values[i] = y
        z_values[i] = z

    return x_values, y_values, z_values


def make_plot(sigma, rho, beta, title, filename):
    x0 = 1.0
    y0 = 2.0
    z0 = 3.0

    dt = 0.01
    t_final = 50
    number_of_steps = int(t_final / dt)

    x_exp, y_exp, z_exp = run_explicit_rk2(
        x0, y0, z0, sigma, rho, beta, dt, number_of_steps
    )

    x_imp, y_imp, z_imp = run_implicit_rk2(
        x0, y0, z0, sigma, rho, beta, dt, number_of_steps
    )

    fig = plt.figure(figsize=(12, 6))
    fig.suptitle(title)

    stableE = fig.add_subplot(121, projection="3d")
    stableE.plot(x_exp, y_exp, z_exp, color="blue", label="Lorenz Attractor")
    stableE.set_title("Lorenz Attractor Visualization Explicit RK2")
    stableE.set_xlabel("X Axis")
    stableE.set_ylabel("Y Axis")
    stableE.set_zlabel("Z Axis")

    stableI = fig.add_subplot(122, projection="3d")
    stableI.plot(x_imp, y_imp, z_imp, color="green", label="Lorenz Attractor")
    stableI.set_title("Lorenz Attractor Visualization Implicit RK2")
    stableI.set_xlabel("X Axis")
    stableI.set_ylabel("Y Axis")
    stableI.set_zlabel("Z Axis")

    plt.savefig(filename)


make_plot(
    sigma=10.0,
    rho=14.0,
    beta=8.0 / 3.0,
    title="Stable Values",
    filename="lorenz_plot_stable.png"
)

make_plot(
    sigma=10.0,
    rho=28.0,
    beta=8.0 / 3.0,
    title="Chaos Values",
    filename="lorenz_plot_chaos.png"
)

plt.show()