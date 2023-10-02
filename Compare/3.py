dataset = pd.read_excel("Regression AE Attendances Gavin McCann (2).xlsx")

# Convert the dependent variable from string to integer
label_encoder = LabelEncoder()
dataset['CORE_HRG'] = label_encoder.fit_transform(dataset['CORE_HRG'])

# Define the columns to be encoded
cols_to_encode = ['SEX', 'POSTCODE_SECTOR_USUAL_ADDR', 'ATTENDANCE_SITE_CODE', 'Arrival Mode Description']

# Encode the categorical columns using LabelEncoder
for col in cols_to_encode:
    le = LabelEncoder()
    dataset[col] = le.fit_transform(dataset[col])

dataset.drop('Arrival Mode', axis=1, inplace=True)

# Preprocess the independent variables
X = dataset.iloc[:, 1:]
y = dataset.iloc[:, 0]

# Encode the categorical variables using one-hot encoding
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [1, 2])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a multinomial logistic regression model
lr = LogisticRegression(multi_class='multinomial', solver='lbfgs')

# Fit the model on the training data
lr.fit(X_train, y_train)
print(lr.classes_)