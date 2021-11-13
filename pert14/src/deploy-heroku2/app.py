import numpy as np
from flask import Flask, request, render_template, redirect, url_for
import pickle
import os

app = Flask(__name__)


@app.route('/')
def home():
    return redirect(url_for('welcome'))


@app.route('/index')
def welcome():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/predict',methods=['GET', 'POST'])
def predict():
    if request.method=='POST':
        result = request.form

        pkl_file = open('cat', 'rb')
        index_dict = pickle.load(pkl_file)
        new_vector = np.zeros(len(index_dict))

        try:
            new_vector[index_dict['age']] = result['age']
        except:
            pass
        try:
            new_vector[index_dict['sex_' + str(result['sex'])]] = 1
        except:
            pass
        try:
            new_vector[index_dict['bmi']] = result['bmi']
        except:
            pass
        try:
            new_vector[index_dict['children']] = result['children']
        except:
            pass
        try:
            new_vector[index_dict['smoker_' + str(result['smoker'])]] = 1
        except:
            pass
        try:
            new_vector[index_dict['region_' + str(result['region'])]] = 1
        except:
            pass

        model = pickle.load(open('random_forst_model_1.pkl', 'rb'))
        prediction = model.predict(new_vector.reshape(1, -1))

    return render_template('index.html', pred='Expected bill will be ${:.2f}'.format(prediction[0]))


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port=5000, debug=True)
    #app.run(debug=True)