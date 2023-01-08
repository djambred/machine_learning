from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import joblib
app = Flask(__name__)


@app.route('/',methods=['GET'])
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET'])
@cross_origin()
def index():
    if request.method == 'POST':
        # if(request.form["x"] is None or request.form["y"] is None):
        #     flash("fill inputs")
        try:
            x=int(request.form['x'])
            y =int(request.form['y'])
            filename = 'mlr.sav'
            loaded_model = joblib.load(open(filename, 'rb'))
            prediction=loaded_model.predict([[x,y]])
            print('prediction is', prediction)
            return render_template('results.html',prediction=round(10*prediction[0]))
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    else:
        return render_template('index.html')




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
    #app.run(debug=True)