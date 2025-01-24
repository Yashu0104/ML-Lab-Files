import numpy as np
import pandas as pd
from sympy import symbols, diff

np.random.seed(10)
samples=5
age = np.random.randint(20,80,samples)
bmi=np.random.uniform(18.5,24,samples)
bp=np.random.uniform(90,180,samples)
chol=np.random.uniform(150,300,samples)
coeff=np.array([0.5,-0.8,0.3,0.6])
intercept = 10
noise = np.random.normal(0,5,samples)

y = coeff[0]*age + coeff[1]*bmi + coeff[2]*bp + coeff[3]*chol + intercept + noise

data = pd.DataFrame({"AGE":age, "BMI":bmi, "BP":bp, "CHOL":chol, "Healthscore":y })
# print(data.head())
# print(y)
r=0
for i in range(0,samples):
   r=r+coeff[i] 