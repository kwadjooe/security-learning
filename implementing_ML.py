# import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# load the dataset
data = pd.read_csv("network_traffic.csv")

# split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data.drop('label', axis=1), data['label'], test_size=0.2, random_state=42)

# train a random forest classifier
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# make predictions on the testing set
y_pred = clf.predict(X_test)

# evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
confusion_mat = confusion_matrix(y_test, y_pred)

print("Accuracy:", accuracy)
print("Confusion matrix:", confusion_mat)
