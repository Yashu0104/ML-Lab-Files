import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(10)
samples = 10

age = np.random.randint(20, 80, samples)

coefficient = 0.5

intercept = 10

noise = np.random.normal(0, 5, samples)

healthscore = coefficient * age + intercept + noise

data = pd.DataFrame({
    "AGE": age,
    "Healthscore": healthscore
})

# print(data.head())

# plt.scatter(data["AGE"], data["Healthscore"])
# plt.xlabel("Age")
# plt.ylabel("Healthscore")
# plt.title("Relationship between Age and Healthscore")
# plt.show()