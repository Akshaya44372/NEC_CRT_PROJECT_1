import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("dataset.csv")

# Remove missing values
data = data.dropna()

# Convert names to lowercase
data["name"] = data["name"].str.lower()

# Features and labels
X = data["name"]
y = data["gender"]

# Better feature extraction
vectorizer = TfidfVectorizer(
    analyzer='char',
    ngram_range=(2, 5)
)

X_vectorized = vectorizer.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Better model
model = LinearSVC()

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

# Save files
joblib.dump(model, "gender_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model saved successfully.")