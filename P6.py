#3d scatter plot
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

file_path = 'ML Lab - 1.xlsx'
data = pd.read_excel(file_path)

x = data['Attendence %']
y = data['Previous Marks'] 
z = data['Hours Studied'] 

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(x, y, z, c=z, cmap='viridis', s=50, alpha=0.8, edgecolor='k')

# # Add color bar
# cbar = fig.colorbar(scatter, ax=ax)
# cbar.set_label('Z (Parameter 3)')

# Label axes
ax.set_xlabel('Attendence %')
ax.set_ylabel('Previous Marks')
ax.set_zlabel('Hours Studied')
ax.set_title('3D Scatter Plot')

# Show plot
plt.show()
