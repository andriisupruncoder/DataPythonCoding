from sklearn.metrics import recall_score

# True labels
y_true = [1, 0, 1, 1]

# Predicted labels
y_pred = [1, 1, 1, 0]

# Calculate recall score
recall_score(y_true, y_pred)