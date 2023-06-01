
import flask
import pickle
import numpy
from flask import Flask, request, jsonify

model = pickle.load(open("C:/Users/vknsr/Downloads/final.pkl",'rb'))
app = Flask(__name__)


@app.route('/')
def home():
    return "Hello world"


@app.route('/loan_status', methods=['POST'])
def loan_status():
    age = request.form.get('person_age')
    income = request.form.get('person_income')
    home_ownership = request.form.get('person_home_ownership')
    emp_length = request.form.get('person_emp_length')
    loan_intent = request.form.get('loan_intent')
    loan_amount = request.form.get('loan_amnt')
    input_query =numpy.array([['age', 'income', 'home_ownership', 'emp_length', 'loan_intent', 'loan_amount']])
    result = model.predict(input_query)[0]
    return jsonify({'loan_status', str(result)})


if __name__ == '__main__':
    app.run(debug=True)