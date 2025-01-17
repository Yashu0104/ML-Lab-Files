#3d plot line combined
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


file_path = 'ML Lab - 1.xlsx'
data = pd.read_excel(file_path)


x = data['Attendence %']
y = data['Previous Marks'] 
z = data['Hours Studied'] 

# 3D Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label='3D Line Plot')
ax.set_xlabel('Attendence %')
ax.set_ylabel('Previous Marks')
ax.set_zlabel('Hours Studied')
ax.set_title('Test Plot')
plt.legend()
plt.show()
