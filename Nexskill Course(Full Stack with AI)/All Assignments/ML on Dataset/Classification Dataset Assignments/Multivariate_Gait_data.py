import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

df = pd.read_csv("All Assignments/ML on Dataset/Classification Dataset Assignments/Multivariate Gait Data.csv")
print()
print("Graph of data")
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x = "condition", hue="condition", palette="Set2", legend=False)
plt.title("Total data count for each condition")
plt.xlabel("condition 1, 2, 3")
plt.ylabel("Data count")
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

y = df["condition"]
X = df[['subject', 'replication', 'leg', 'joint', 'time', 'angle']]

X_train, X_test, y_text, y_train = train_test_split( X, y, random_state=42, train_size=0.2)
print("AI model learning..... ")


