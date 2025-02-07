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
            return "Master’s" if row['Age'] >= 30 else "Bachelor’s"
        elif row['Job Role'] == 'Engineer':
            return "Master’s" if row['Age'] > 25 else "Bachelor’s"
    return row['Education Level']

def fill_age(row):
    if pd.isna(row['Age']):
        if row['Education Level'] == "Bachelor’s":
            return 20
        elif row['Education Level'] == "Master’s":
            return 25
        elif row['Education Level'] == 'PhD':
            return 30
    return row['Age']

def fill_job(row):
    if pd.isna(row['Job Role']):
        if row['Age'] <= 25:
            return "Bachelor’s"
        elif row['Age'] <= 30:
            return "Master’s"
        elif row['Age'] > 30:
            return 'PhD'
    return row['Job Role']

data['Education Level'] = data.apply(fill_education, axis=1)
data['Age'] = data.apply(fill_age, axis=1)
data['Job Role'] = data.apply(fill_job, axis=1)

data.to_excel("cleaned_data.xlsx", index=False)
print(data[['Experience (Years)', 'Education Level', 'Age']])
