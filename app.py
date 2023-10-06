from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load the pre-trained machine learning model
model = joblib.load('water_quality_model.pkl')

@app.route('/')
def hello():
    return 'Welcome to the Water Quality Prediction API!'

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the request as JSON
        data = request.get_json()

        # Ensure that the request contains valid JSON data
        if not data:
            return jsonify({'error': 'Invalid JSON data'}), 400

        # Convert JSON data to a DataFrame for prediction
        input_data = pd.DataFrame(data, index=[0])

        # Make predictions using the loaded model
        predictions = model.predict(input_data)

        # Return the predictions as JSON
        return jsonify({'predictions': predictions.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
