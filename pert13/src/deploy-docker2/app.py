from flask import Flask, request, render_template
from joblib import load

app = Flask(__name__)

model = load('model.joblib')

@app.route('/')
def index():
    return render_template('index.html', ipk=0)

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    ind, mat, ing = [float(x) for x in request.form.values()]

    data = [ind, mat, ing]

    prediction = model.predict([data])
    output = round(prediction[0][0], 2)

    return render_template('index.html', ipk=output, ind=ind, mat=mat, ing=ing)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    #app.run(debug=True)
