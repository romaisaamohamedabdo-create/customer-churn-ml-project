"""
app.py — Flask Web App for Customer Churn Prediction
Run locally:  python app.py
Then open:    http://127.0.0.1:5000
"""

from flask import Flask, request, render_template, jsonify
import joblib
import numpy as np

# ── Load saved model artifacts ──
model          = joblib.load('model.pkl')
scaler         = joblib.load('scaler.pkl')
selected_features = joblib.load('features.pkl')

app = Flask(__name__)


@app.route('/')
def home():
    """Render the main prediction form."""
    return render_template('index.html', features=selected_features)


@app.route('/predict', methods=['POST'])
def predict():
    """Receive form data, run prediction, return result."""
    try:
        # Collect values from the HTML form in the correct feature order
        input_values = []
        for feature in selected_features:
            val = request.form.get(feature, 0)
            input_values.append(float(val))

        # Convert to numpy array and scale
        input_array = np.array(input_values).reshape(1, -1)
        input_scaled = scaler.transform(input_array)

        # Predict
        prediction = model.predict(input_scaled)[0]
        probability = model.predict_proba(input_scaled)[0][1]  # P(churn)

        # Prepare result message
        if prediction == 1:
            result = f"⚠️ HIGH RISK: This customer is likely to churn."
            risk_pct = f"{probability * 100:.1f}%"
            color = "danger"
        else:
            result = f"✅ LOW RISK: This customer is likely to stay."
            risk_pct = f"{probability * 100:.1f}%"
            color = "success"

        return render_template(
            'index.html',
            features=selected_features,
            prediction_text=result,
            risk_pct=risk_pct,
            color=color
        )

    except Exception as e:
        return render_template(
            'index.html',
            features=selected_features,
            prediction_text=f"Error: {str(e)}",
            color="warning"
        )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
