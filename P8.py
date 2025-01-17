import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load data from Excel
file_path = 'ML Lab - 1.xlsx'  # Replace with the path to your Excel file
data = pd.read_excel(file_path)

# Check the actual column names to identify any discrepancies
print("Columns before cleaning:", data.columns)

# Clean up column names (strip any extra spaces)
data.columns = data.columns.str.strip()

# Or rename columns explicitly if needed
data.rename(columns={
    'Attendance %': 'Attendance',  # Adjust as per the exact column names
    'Previous Marks': 'PreviousMarks',
    'Hours Studied': 'HoursStudied'
}, inplace=True)

# Check columns after renaming
print("Columns after cleaning:", data.columns)

# Add 'Result' column based on a condition (e.g., sum of features > 150)
data['Result'] = (data['Attendance'] + data['PreviousMarks'] + data['HoursStudied']) > 150
data['Result'] = data['Result'].astype(int)  # Convert to integers (0 or 1)

# Prepare the dataset
X = data[['Attendance', 'PreviousMarks', 'HoursStudied']].values  # Features
y = data['Result'].values  # Target (1 for Pass, 0 for Fail)

# Manual train-test split
split_index = int(0.8 * len(X))  # 80-20 split
X_train, X_test = X[:split_index], X[split_index:]
y_train, y_test = y[:split_index], y[split_index:]

# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict and calculate accuracy
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

# Define the plane equation from the model coefficients
coefficients = model.coef_[0]
intercept = model.intercept_[0]
w1, w2, w3 = coefficients[0], coefficients[1], coefficients[2]

# Create a mesh grid for the plane
x_range = np.linspace(data['Attendance'].min(), data['Attendance'].max(), 30)
y_range = np.linspace(data['PreviousMarks'].min(), data['PreviousMarks'].max(), 30)
X_mesh, Y_mesh = np.meshgrid(x_range, y_range)
Z_mesh = -(w1 * X_mesh + w2 * Y_mesh + intercept) / w3  # Solve for Z (HoursStudied)

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the points (blue for Pass, red for Fail)
for i in range(len(X_train)):
    color = 'blue' if y_train[i] == 1 else 'red'  # Pass students are blue, Fail students are red
    ax.scatter(X_train[i][0], X_train[i][1], X_train[i][2], c=color)

# Plot the decision plane
ax.plot_surface(X_mesh, Y_mesh, Z_mesh, color='green', alpha=0.5, edgecolor='none', label='Decision Boundary')

# Label axes
ax.set_xlabel('Attendance')
ax.set_ylabel('Previous Marks')
ax.set_zlabel('Hours Studied')
ax.set_title('3D Scatter Plot with Decision Boundary')

# Show legend and plot
plt.show()
