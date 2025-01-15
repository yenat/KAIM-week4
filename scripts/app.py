from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Load the model when a request is made
        model = joblib.load('/home/enat/KAIM-week4/notebooks/model_12-01-2025-11-27-43-961795.pkl')
        
        data = request.get_json()
        input_data = pd.DataFrame([data])
        prediction = model.predict(input_data)
        
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
