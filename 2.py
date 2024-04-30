import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

# Load and preprocess data
data = pd.read_csv('vibration_data.csv')

# Identify and convert datetime columns (replace 'datetime_column' with the actual column name)
datetime_columns = data.select_dtypes(include=[object]).columns  # This assumes date columns are object type
for col in datetime_columns:
    try:
        data[col] = pd.to_datetime(data[col])
        data[f'{col}_year'] = data[col].dt.year
        data[f'{col}_month'] = data[col].dt.month
        data[f'{col}_day'] = data[col].dt.day
        data[f'{col}_hour'] = data[col].dt.hour
        data.drop(col, axis=1, inplace=True)  # Drop the original datetime column
    except ValueError:
        continue  # Skip columns that cannot be converted to datetime

# Check the data types after modification
print(data.dtypes)

features = data.drop('status', axis=1)
labels = data['status']

# Split data
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Initialize and train the Random Forest model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Predict and evaluate the model
predictions = model.predict(X_test)
print(classification_report(y_test, predictions))
