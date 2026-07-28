import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib

print("Machine Learning Started...")

# Read CSV
data = pd.read_csv("data/students.csv")

# Input Features
X = data[["CGPA", "Attendance"]]

# Output
y = data["Performance"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Model
model = DecisionTreeClassifier()

# Train Model
model.fit(X_train, y_train)

# Save Model
joblib.dump(model, "models/performance_model.pkl")

print("✅ Model Trained Successfully!")
print("Model Saved Successfully!")