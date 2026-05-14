import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
from main import x, y, z
from rk_methods import explicit_rk2, explicit_rk4, implicit_rk2
import numpy as np

#--------------------
#Stable Values
#--------------------

sigma = 10
rho = 14
beta = 8/3

x = 1
y = 2
z = 3

t_final = 50
number_of_steps = int(t_final / 0.01)

x_values = []
y_values = []
z_values = []

for i in range(number_of_steps):
    x, y, z = explicit_rk4(x, y, z, sigma, rho, beta, 0.01)
    x_values.append(x)
    y_values.append(y)
    z_values.append(z)

np.array(x_values)
np.array(y_values)
np.array(z_values)

fig = plt.figure(figsize=(12, 6))
fig.suptitle("Stable Values")
stableE = fig.add_subplot(121, projection='3d')

# Plot the trajectory
stableE.plot(x_values, y_values, z_values, color='blue', label='Lorenz Attractor')

# Formatting
stableE.set_title("Lorenz Attractor Visualization Explicit RK2")
stableE.set_xlabel("X Axis")
stableE.set_ylabel("Y Axis")
stableE.set_zlabel("Z Axis")

x_values = []
y_values = []
z_values = []

for i in range(number_of_steps):
    x, y, z = implicit_rk2(x, y, z, sigma, rho, beta, 0.01)
    x_values.append(x)
    y_values.append(y)
    z_values.append(z)

np.array(x_values)
np.array(y_values)
np.array(z_values)

stableI = fig.add_subplot(122, projection='3d')

# Plot the trajectory
stableI.plot(x_values, y_values, z_values, color='green', label='Lorenz Attractor')

# Formatting
stableI.set_title("Lorenz Attractor Visualization Implicit RK2")
stableI.set_xlabel("X Axis")
stableI.set_ylabel("Y Axis")
stableI.set_zlabel("Z Axis")

plt.savefig("lorenz_plot_stable.png")

#--------------------
#Chaos Values
#--------------------

sigma = 10
rho = 28
beta = 8/3

x = 1
y = 2
z = 3

t_final = 50
number_of_steps = int(t_final / 0.01)

x_values = []
y_values = []
z_values = []

for i in range(number_of_steps):
    x, y, z = explicit_rk4(x, y, z, sigma, rho, beta, 0.01)
    x_values.append(x)
    y_values.append(y)
    z_values.append(z)

np.array(x_values)
np.array(y_values)
np.array(z_values)

fig2 = plt.figure(figsize=(12, 6))
fig2.suptitle("Chaos Values")
chaosE = fig2.add_subplot(121, projection='3d')

# Plot the trajectory
chaosE.plot(x_values, y_values, z_values, color='blue', label='Lorenz Attractor')

# Formatting
chaosE.set_title("Lorenz Attractor Visualization Explicit RK2")
chaosE.set_xlabel("X Axis")
chaosE.set_ylabel("Y Axis")
chaosE.set_zlabel("Z Axis")

x_values = []
y_values = []
z_values = []

for i in range(number_of_steps):
    x, y, z = implicit_rk2(x, y, z, sigma, rho, beta, 0.01)
    x_values.append(x)
    y_values.append(y)
    z_values.append(z)

np.array(x_values)
np.array(y_values)
np.array(z_values)

chaosI = fig2.add_subplot(122, projection='3d')

# Plot the trajectory
chaosI.plot(x_values, y_values, z_values, color='green', label='Lorenz Attractor')

# Formatting
chaosI.set_title("Lorenz Attractor Visualization Implicit RK2")
chaosI.set_xlabel("X Axis")
chaosI.set_ylabel("Y Axis")
chaosI.set_zlabel("Z Axis")

plt.savefig("lorenz_plot_chaos.png")
plt.show()