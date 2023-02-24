import numpy as np
import matplotlib.pyplot as plt

# Define constants
k = 9e9
# Coulomb's constant
q = 1e-9
# point charge

# Define grid of points
x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(x, y)

# Calculate electric field components
r = np.sqrt(X**2 + Y**2)
Ex = k*q*X/r**3
Ey = k*q*Y/r**3

# Visualize electric field vectors
plt.quiver(X, Y, Ex, Ey)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Electric Field Visualization')
plt.show()
