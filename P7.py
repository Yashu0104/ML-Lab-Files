import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

file_path = 'ML Lab - 1.xlsx'
data = pd.read_excel(file_path)

x = data['Attendence %']
y = data['Previous Marks'] 
z = data['Hours Studied'] 

# Define the plane equation: z = ax + by + c
a, b, c = 1, -1, 5  # Example coefficients for the plane equation

# Create a mesh grid for the plane
x_range = np.linspace(min(x), max(x), 30)
y_range = np.linspace(min(y), max(y), 30)
X, Y = np.meshgrid(x_range, y_range)
Z = a * X + b * Y + c  # Calculate Z values for the plane

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot for the points
scatter = ax.scatter(x, y, z, c=z, cmap='viridis', s=50, alpha=0.8, edgecolor='k', label='Data Points')

# Plot the plane
ax.plot_surface(X, Y, Z, alpha=0.5, color='blue', edgecolor='none', label='Plane')

# Add color bar
cbar = fig.colorbar(scatter, ax=ax)
cbar.set_label('Hours Studied')

# Label axes
ax.set_xlabel('Attendence %')
ax.set_ylabel('Previous Marks')
ax.set_zlabel('Hours Studied')
ax.set_title('3D Scatter Plot with Plane')

# Show legend and plot
plt.legend()
plt.show()
