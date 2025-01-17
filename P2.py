import numpy as np
import pandas as pd

# Load data from Excel file
file_path = 'ML Lab - 1.xlsx'  # Replace with your actual file path
data = pd.read_excel(file_path)

# Extract columns
attendance = data['Attendance %'].values
previous_marks = data['previous_marks'].values
actual_marks = data['actual_marks'].values  # Assuming you have actual marks as well in the dataset

# Normalize the data (optional)
attendance = attendance / 100
previous_marks = previous_marks / 100
actual_marks = actual_marks / 100

# Initialize parameters
w1, w2, b = 0.0, 0.0, 0.0
alpha = 0.01  # Learning rate
epochs = 1000
m = len(actual_marks)

# Gradient Descent
for epoch in range(epochs):
    predictions = w1 * attendance + w2 * previous_marks + b
    cost = (1 / (2 * m)) * np.sum((predictions - actual_marks) ** 2)
    
    # Gradients
    dw1 = (1 / m) * np.sum((predictions - actual_marks) * attendance)
    dw2 = (1 / m) * np.sum((predictions - actual_marks) * previous_marks)
    db = (1 / m) * np.sum(predictions - actual_marks)
    
    # Update parameters
    w1 -= alpha * dw1
    w2 -= alpha * dw2
    b -= alpha * db
    
    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Cost: {cost}")

print(f"Trained parameters: w1={w1}, w2={w2}, b={b}")
