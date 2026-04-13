from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = scaler.transform([features])
    prediction = model.predict(final_features)[0]

    result = "Customer WILL CHURN ❌" if prediction == 1 else "Customer will STAY ✅"

    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)