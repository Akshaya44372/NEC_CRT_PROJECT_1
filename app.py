from flask import Flask, render_template, request
import joblib

# Load model and vectorizer
model = joblib.load("gender_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None

    if request.method == "POST":

        name = request.form["name"]

        # Convert to lowercase
        name = name.lower()

        # Vector transform
        vector = vectorizer.transform([name])

        # Predict
        result = model.predict(vector)[0]

        prediction = result

    return render_template(
        "index.html",
        prediction=prediction
    )

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )