import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.metrics import confusion_matrix

df = pd.read_csv("outputs/evaluation_sample.csv")
# true labels and predictions (example placeholders)
y_true = df["manual_sentiment"]
y_pred = df["sentiment"]

cm = confusion_matrix(y_true, y_pred, labels=["negative","positive"])

plt.figure(figsize=(6,5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Negative","Positive"],
    yticklabels=["Negative","Positive"]
)

plt.title("Confusion Matrix for Sentiment Classification")

plt.xlabel("Predicted Label")

plt.ylabel("Actual Label")

plt.tight_layout()

plt.savefig("outputs/figures/confusion_matrix.png", dpi=300)

plt.show()