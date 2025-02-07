import pandas as pd

file_path = 'Missing Values.xlsx'
data = pd.read_excel(file_path)

a = data['Experience (Years)']
b = data['Education Level']
c = data['Age']
d = data['Job Role']
e = data['City']
f = data['Working Hours/Week']
g = data['Salary ($)']

r = a.dropna().values 
mean = sum(r) / len(r)  
variance = sum((i - mean) ** 2 for i in r) / (len(r) - 1) 
standdev = variance ** 0.5  
sd = round(standdev, 0)  

data['Experience (Years)'].fillna(sd, inplace=True)

def fill_education(row):
    if pd.isna(row['Education Level']): 
        if row['Job Role'] == 'Scientist':
            return 'PhD'
        elif row['Job Role'] == 'Manager':
            return 'Masters' if row['Age'] >= 30 else 'Bachelors'
        elif row['Job Role'] == 'Engineer':
            return 'Masters' if row['Age'] > 25 else 'Bachelors'
    return row['Education Level']  

data['Education Level'] = data.apply(fill_education, axis=1)
# data.to_excel("cleaned_data.xlsx", index=False)
print(data[['Experience (Years)', 'Education Level']])

def fill_education(row):
    if pd.isna(row['Education Level']): 
        if row['Job Role'] == 'Scientist':
            return 'PhD'
        elif row['Job Role'] == 'Manager':
            return 'Masters' if row['Age'] >= 30 else 'Bachelors'
        elif row['Job Role'] == 'Engineer':
            return 'Masters' if row['Age'] > 25 else 'Bachelors'
    return row['Education Level']  