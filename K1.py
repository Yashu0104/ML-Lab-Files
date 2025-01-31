import pandas as pd
file_path = 'Missing Values.xlsx'
data = pd.read_excel(file_path)
# frame = pd.DataFrame(data)
a = data['Experience (Years)']
b = data['Education Level']
c = data['Age']
d = data['Job Role']
e = data['City']
f = data['Working Hours/Week']
g = data['Salary ($)']

r = a.dropna().values
# print(r)
mean = sum(r)/len(r)
# print(mean)
variance = sum((i - mean) ** 2 for i in r) / (len(r) - 1)
# print(variance)
standdev= variance**0.5
# print(standdev)
sd = round(standdev,0)
# print(sd)
a.fillna(sd, inplace=True)
print(a)
# if pd.isna(row[''])