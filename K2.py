import pandas as pd

# Load the Excel file
file_path = 'Missing Values.xlsx'
data = pd.read_excel(file_path)

# Extract relevant columns
a = data['Experience (Years)']
b = data['Education Level']
c = data['Age']
d = data['Job Role']
e = data['City']
f = data['Working Hours/Week']
g = data['Salary ($)']

# Manually calculate the standard deviation for Experience (Years)
r = a.dropna().values  # Remove NaN values
mean = sum(r) / len(r)  # Mean calculation
variance = sum((i - mean) ** 2 for i in r) / (len(r) - 1)  # Variance calculation
standdev = variance ** 0.5  # Standard deviation
sd = round(standdev, 0)  # Round to nearest integer

# Fill NaN values in "Experience (Years)" with the calculated standard deviation
data['Experience (Years)'].fillna(sd, inplace=True)

# Function to fill missing Education Level based on Job Role & Age
def fill_education(row):
    if pd.isna(row['Education Level']):  # Check if Education Level is NaN
        if row['Job Role'] == 'Scientist':
            return 'PhD'
        elif row['Job Role'] == 'Manager':
            return 'Masters' if row['Age'] >= 30 else 'Bachelors'
        elif row['Job Role'] == 'Engineer':
            return 'Masters' if row['Age'] > 25 else 'Bachelors'
    return row['Education Level']  # Keep existing value if not NaN

# Apply the function to update Education Level
data['Education Level'] = data.apply(fill_education, axis=1)

# Save the cleaned DataFrame
data.to_excel("cleaned_data.xlsx", index=False)

# Print the updated columns
print(data[['Experience (Years)', 'Education Level']])
