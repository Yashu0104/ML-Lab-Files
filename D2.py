import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("play_tennis_100.csv")

# Encode categorical variables
df['Outlook'] = df['Outlook'].map({'Sunny': 0, 'Rainy': 1, 'Overcast': 2})
df['Temperature'] = df['Temperature'].map({'Cool': 0, 'Mild': 1, 'Hot': 2})
df['Humidity'] = df['Humidity'].map({'Normal': 0, 'High': 1})
df['Windy'] = df['Windy'].map({False: 0, True: 1})

# Features and target
features = ['Outlook', 'Temperature', 'Humidity', 'Windy']
X = df[features]
y = df['PlayTennis']

# Split the dataset (70% train, 30% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=100
)

# Train the decision tree
dtree = DecisionTreeClassifier()
dtree.fit(X_train, y_train)

# Predict on test data
y_pred = dtree.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Visualize the tree
plt.figure(figsize=(12, 5))
tree.plot_tree(
    dtree,
    feature_names=features,
    class_names=dtree.classes_,
    filled=True
)
plt.show()
