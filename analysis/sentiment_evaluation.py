import pandas as pd
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("outputs/evaluation_sample.csv")

y_true = df["manual_sentiment"]
y_pred = df["sentiment"]

accuracy = accuracy_score(y_true, y_pred)

print("Accuracy:", accuracy)

print("\nClassification Report:\n")
print(classification_report(y_true, y_pred))