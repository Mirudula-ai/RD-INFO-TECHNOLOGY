from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
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
