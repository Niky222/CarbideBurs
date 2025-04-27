import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Define the function for calculating Fta
def calculate_Fta(V, fz, y):
  return 1977.87 * V ** -0.128093 * fz ** 0.702486 * y ** -0.228604


# Setting variable ranges
V = np. Linspace (157, 204, 100)
fz = np. linspace(0.03, 0.05, 100)
у = 10


# Create mesh
V_grid, fz_grid = np. meshgrid (V, fz)
Fc_grid = calculate_Fta(V_grid, fz_grid, y)


# Plotting
fig = plt. figure()
ax = fig. add_subplot (111, projection='3d')
ax. plot_surface(V_grid, fz_grid, Fc_grid, cmap='viridis')


# Add labels
ax. set_xlabel( Cutting speed (V)') ax.set_ylabel('Feed per tooth(fz)')
ax.set_zlabel Cutting force(Fta)')
ax. set_title( Response surface')


# Show surface
plt.show()
