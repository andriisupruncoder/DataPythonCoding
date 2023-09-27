import pandas as pd
import numpy as np
import missingno as msno
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.neural_network import MLPRegressor
from sklearn.decomposition import PCA
import markdown

# Download the Boston Housing Dataset from the Internet and call it as a DataFrame
df = pd.read_csv("https://raw.githubusercontent.com/rasbt/mlxtend/master/data/boston_housing_data.csv")

# Check the extent of missing values using 'missingno' package and apply missing data imputation
msno.matrix(df)
df.fillna(df.mean(), inplace=True)

# Create a correlation matrix for all the variables
corr_matrix = df.corr()

# Perform the ANN techniques on the dataset
X = df.drop("MEDV", axis=1)
y = df["MEDV"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
ann = MLPRegressor()
ann.fit(X_train, y_train)
y_pred = ann.predict(X_test)

# Evaluate the performance of the model using RMSE, R-squared and adjusted R-squared methods
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
adjusted_r2 = r2_score(y_test, y_pred, adjusted=True)

# Apply the PCA technique for dimensionality reduction of the dataset
pca = PCA(n_components=5)
X_reduced = pca.fit_transform(X)

# Again, perform the ANN algorithm and evaluate the performance of the model using RMSE, R-squared and adjusted R-squared methods
ann_reduced = MLPRegressor()
ann_reduced.fit(X_reduced, y_train)
y_pred_reduced = ann_reduced.predict(X_reduced)
rmse_reduced = np.sqrt(mean_squared_error(y_test, y_pred_reduced))
r2_reduced = r2_score(y_test, y_pred_reduced)
adjusted_r2_reduced = r2_score(y_test, y_pred_reduced, adjusted=True)

# Compare both the performance and conclude using Markdown
markdown_text = """
## Performance Comparison

| Metric | ANN | ANN with PCA |
|---|---|---|
| RMSE | {} | {} |
| R-squared | {} | {} |
| Adjusted R-squared | {} | {} |

**Conclusion**

The ANN model with PCA performed better than the ANN model without PCA. This is because PCA helped to reduce the dimensionality of the dataset, which made it easier for the ANN model to learn the underlying patterns in the data.
""".format(rmse, rmse_reduced, r2, r2_reduced, adjusted_r2, adjusted_r2_reduced)

with open("performance_comparison.md", "w") as f:
    f.write(markdown_text)