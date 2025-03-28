from pkgutil import get_data
from networkx import tree_data # type: ignore
import pandas as pd
import numpy as np
from collections import Counter
import pprint

# Load the dataset
df = pd.read_csv("play_tennis_100.csv")  # Adjust path if needed

# Function to calculate entropy
def entropy(data):
    label_column = data.iloc[:, -1]
    label_counts = Counter(label_column)
    total = len(label_column)
    
    ent = 0
    for count in label_counts.values():
        prob = count / total
        ent -= prob * np.log2(prob)
    return ent

# Function to calculate information gain
def info_gain(data, feature):
    total_entropy = entropy(data)
    values = data[feature].unique()
    weighted_entropy = 0

    for val in values:
        subset = data[data[feature] == val]
        weight = len(subset) / len(data)
        weighted_entropy += weight * entropy(subset)

    return total_entropy - weighted_entropy

# ID3 algorithm to build the decision tree
def build_tree(data, features):
    labels = data.iloc[:, -1]
    
    # Base cases
    if len(set(labels)) == 1:
        return labels.iloc[0]  # Only one class remains
    
    if not features:
        return labels.mode()[0]  # Return majority class
    
    # Choose the best feature
    gains = {feature: info_gain(data, feature) for feature in features}
    best_feature = max(gains, key=gains.get)

    tree = {best_feature: {}}
    remaining_features = [f for f in features if f != best_feature]

    for value in data[best_feature].unique():
        subset = data[data[best_feature] == value]
        subtree = build_tree(subset, remaining_features)
        tree[best_feature][value] = subtree

    return tree

# Build and display the tree
features = df.columns[:-1].tolist()  # All columns except target
decision_tree = build_tree(df, features)

# Pretty print the decision tree
pprint.pprint(decision_tree)

# Predict function
def predict(tree, sample):
    if not isinstance(tree, dict):
        return tree
    
    feature = next(iter(tree))
    value = sample.get(feature)
    subtree = tree[feature].get(value)

    if subtree is None:
        return "Unknown"  # Handle unseen values

    return predict(subtree, sample)

# Train the tree
features = tree_data.columns[:-1].tolist()  # Exclude target column
decision_tree = build_tree(tree_data, features)

# Display the tree
print("\nDecision Tree:")
pprint.pprint(decision_tree)

# Test the model
correct = 0
for _, row in get_data.iterrows():
    sample = row.to_dict()
    actual = sample[df.columns[-1]]
    predicted = predict(decision_tree, sample)
    if predicted == actual:
        correct += 1

accuracy = correct / len(get_data)
print(f"\nAccuracy on test data: {accuracy * 100:.2f}%")
