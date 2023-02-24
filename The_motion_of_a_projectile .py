import numpy as np
import matplotlib.pyplot as plt

# Define initial conditions
v0 = 30
# initial velocity (m/s)
theta = 45
# angle of launch (degrees)
g = 9.81
# acceleration due to gravity (m/s^2)
t_max = 5
# maximum time of flight (s)

# Define equations of motion
def x(t):
    return v0*np.cos(np.deg2rad(theta))*t

def y(t):
    return v0*np.sin(np.deg2rad(theta))*t - 0.5*g*t**2

# Implement Euler method
dt = 0.01 # time step (s)
t = np.arange(0, t_max, dt)
x_vals = np.zeros_like(t)
y_vals = np.zeros_like(t)

for i in range(len(t)):
    x_vals[i] = x(t[i])
    y_vals[i] = y(t[i])

# Visualize results
plt.plot(x_vals, y_vals)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Projectile Motion Simulation')
plt.show()
