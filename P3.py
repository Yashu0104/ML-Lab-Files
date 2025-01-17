#Sample
import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)  # Parameter 1
y = np.sin(x)                # Parameter 2
z = np.cos(x)                # Parameter 3

# 3D Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label='3D Line Plot')
ax.set_xlabel('X (Parameter 1)')
ax.set_ylabel('Y (Parameter 2)')
ax.set_zlabel('Z (Parameter 3)')
ax.set_title('3D Plot with 3 Parameters')
plt.legend()
plt.show()
