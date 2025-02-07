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

def fill_age(row):
    if pd.isna(row['Age']):
        if row['Education Level'] == 'Bachelors':
            return 20
        elif row['Education Level'] == 'Masters':
            return 25
        elif row['Education Level'] == 'PhD':
            return 30
    return row['Age']

def fill_job(row):
    if pd.isna(row['Job Role']):
        if row['Age'] <= 25:
            return 'Bachelors'
        elif row['Age'] <= 30:
            return 'Masters'
        elif row['Age'] > 30:
            return 'PhD'
    return row['Job Role']

def fill_salary(row):
    if pd.isna(row['Salary ($)']):
        if row['Job Role'] == 'Scientist':
            return 100000
        elif row['Job Role'] == 'Manager':
            return 80000
        elif row['Job Role'] == 'Engineer':
            return 60000
    return row['Salary ($)']

def fill_working_hrs(row):
    if pd.isna(row['Working Hours/Week']):
        if row['Salary ($)'] > 100000:
            return 50
        elif 80000 < row['Salary ($)'] <= 100000:
            return 45
        elif row['Salary ($)'] <= 80000:
            return 40
    return row['Working Hours/Week']

most_common_city = data['City'].mode()[0]
data['City'].fillna(most_common_city, inplace=True)

data['Education Level'] = data.apply(fill_education, axis=1)
data['Age'] = data.apply(fill_age, axis=1)
data['Job Role'] = data.apply(fill_job, axis=1)
data['Salary ($)'] = data.apply(fill_salary, axis=1)
data['Working Hours/Week'] = data.apply(fill_working_hrs, axis=1)

data.to_excel("cleaned_data01.xlsx", index=False)
print(data[['Experience (Years)', 'Education Level', 'Age', 'City', 'Working Hours/Week', 'Salary ($)']])
