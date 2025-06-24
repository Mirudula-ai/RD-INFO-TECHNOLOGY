from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
<<<<<<< HEAD
model = joblib.load("diabetes_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/premeal")
def premeal():
    return render_template("premeal_form.html")

@app.route("/postmeal")
def postmeal():
    return render_template("postmeal_form.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        values = [float(request.form.get(field)) for field in [
            "pregnancies", "glucose", "bloodpressure", "skinthickness",
            "insulin", "bmi", "dpf", "age"
        ]]
        prediction = model.predict([np.array(values)])
        result = "Diabetic" if prediction[0] == 1 else "Not Diabetic"
        return render_template("result.html", result=result)
    except Exception as e:
        return render_template("error.html", error=str(e))

if __name__ == "__main__":
    app.run(debug=True)
=======
model = joblib.load('diabetes_model.pkl')

@app.route('/')
<<<<<<< HEAD
def index():
    return render_template('index.html')

@app.route('/premeal')
def premeal():
    return render_template('premeal_form.html')

@app.route('/postmeal')
def postmeal():
    return render_template('postmeal_form.html')
=======
def home():
    return render_template('form.html')
>>>>>>> e3f99357a60b8229cd3166b4c3a70118ab3fd085

@app.route('/predict', methods=['POST'])
def predict():
    data = [
        float(request.form['pregnancies']),
        float(request.form['glucose']),
        float(request.form['bp']),
        float(request.form['skin']),
        float(request.form['insulin']),
        float(request.form['bmi']),
        float(request.form['dpf']),
        float(request.form['age'])
    ]
    prediction = model.predict([np.array(data)])
    result = 'Diabetic' if prediction[0] == 1 else 'Not Diabetic'
    color = '#ff4d4d' if result == 'Diabetic' else '#5cd65c'
<<<<<<< HEAD
        return f"""
    <body style='background: linear-gradient(to right, #74ebd5, #ACB6E5); display: flex; align-items: center; justify-content: center; height: 100vh;'>
        <div style='background-color: white; padding: 40px; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.3); text-align: center;'>
            <h2 style='color: {color};'>Prediction: {result}</h2>
            <a href='/' style='display: inline-block; margin-top: 20px; padding: 10px 20px; background-color: #4CAF50; color: white; text-decoration: none; border-radius: 5px;'>Back</a>
        </div>
    </body>
    """


if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
=======

    return f'''
    <body style="background: linear-gradient(to right, #74ebd5, #ACB6E5); font-family: Arial; display: flex; align-items: center; justify-content: center; height: 100vh;">
        <div style="background-color: white; padding: 40px; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.3); text-align: center;">
            <h2 style="color: {color};">Prediction: {result}</h2>
            <a href="/" style="display: inline-block; margin-top: 20px; padding: 10px 20px; background-color: #4CAF50; color: white; text-decoration: none; border-radius: 5px;">Back to Form</a>
        </div>
    </body>
    '''
    
import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
>>>>>>> e3f99357a60b8229cd3166b4c3a70118ab3fd085
>>>>>>> c5edf7ec071f4b8303d7e1e094805c44a440ef82
