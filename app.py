from flask import Flask, render_template, request
import joblib
import pickle

app = Flask(__name__, template_folder='templates')
model = pickle.load(open("model.pkl","rb"))
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    age = request.form.get('age')
    income = request.form.get('income')
    score = request.form.get('score')
    
    prediction = model.predict([[age, income, score]])

    
    gender = 'Female' if prediction == 1 else 'Male'

    return render_template('result.html', gender=gender)

if __name__ == '__main__':
    app.run(debug=True)
