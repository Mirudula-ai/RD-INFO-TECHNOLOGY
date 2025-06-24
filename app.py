from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load('diabetes_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/premeal')
def premeal():
    return render_template('premeal_form.html')

@app.route('/postmeal')
def postmeal():
    return render_template('postmeal_form.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        inputs = [
            float(request.form['pregnancies']),
            float(request.form['glucose']),
            float(request.form['bp']),
            float(request.form['skin']),
            float(request.form['insulin']),
            float(request.form['bmi']),
            float(request.form['dpf']),
            float(request.form['age'])
        ]
        prediction = model.predict([inputs])
        result = "Diabetic" if prediction[0] == 1 else "Not Diabetic"
        return render_template('index.html', result=result)
    except Exception as e:
        return render_template('index.html', result=f"Error: {str(e)}")

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
