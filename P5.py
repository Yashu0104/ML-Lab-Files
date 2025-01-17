#scatter plot
import matplotlib.pyplot as plt
import pandas as pd

file_path = 'ML Lab - 1.xlsx'
data = pd.read_excel(file_path)

x = data['Attendence %']
y = data['Previous Marks'] 
z = data['Hours Studied'] 


# Scatter plot with size representing the third parameter
plt.scatter(x, y, c=z, cmap='viridis', s=50, edgecolor='k', alpha=0.7)
plt.colorbar(label='Z (Parameter 3)')  # Add color bar for the third parameter
plt.xlabel('Attendence %')
plt.ylabel('Previous Marks')
plt.title('Scatter Plot with 3 Parameters')
plt.show()
