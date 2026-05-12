from flask import Flask, render_template, request
from model import predict_disease

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Get user input safely
    fever = int(request.form.get('fever', 0))
    cough = int(request.form.get('cough', 0))
    headache = int(request.form.get('headache', 0))
    tiredness = int(request.form.get('tiredness', 0))
    cold = int(request.form.get('cold', 0))

    symptoms = [fever, cough, headache, tiredness, cold]

    # Predict disease
    result = predict_disease(symptoms)

    # Make result user-friendly
    if result == "Flu":
        message = "You may have Flu 🤒"
        advice = "Take rest, drink plenty of fluids, and consult a doctor if symptoms continue."
    elif result == "Cold":
        message = "You may have Common Cold 🤧"
        advice = "Stay warm, drink hot fluids, and take proper rest."
    elif result == "Migraine":
        message = "You may have Migraine 🤕"
        advice = "Avoid bright lights, take rest, and consult a doctor if needed."
    else:
        message = "Unable to determine the condition"
        advice = "Please consult a doctor for proper diagnosis."

    return render_template(
        'index.html',
        prediction=message,
        advice=advice
    )


if __name__ == "__main__":
    app.run(debug=True)