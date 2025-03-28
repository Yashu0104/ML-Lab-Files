import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("play_tennis_100.csv")

# Convert categorical features to numeric
df['Outlook'] = df['Outlook'].map({'Sunny': 0, 'Rainy': 1, 'Overcast': 2})
df['Temperature'] = df['Temperature'].map({'Cool': 0, 'Mild': 1, 'Hot': 2})
df['Humidity'] = df['Humidity'].map({'Normal': 0, 'High': 1})
df['Windy'] = df['Windy'].map({False: 0, True: 1})  # Assuming Windy is boolean

# Features and target
X = df[['Outlook', 'Temperature', 'Humidity', 'Windy']]
y = df['PlayTennis']

# Train decision tree
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

# Plot the tree
plt.figure(figsize=(12, 8))
tree.plot_tree(dtree, feature_names=X.columns, class_names=dtree.classes_, filled=True)
plt.show()
