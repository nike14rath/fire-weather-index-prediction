from flask import Flask
import pickle
from sklearn.preprocessing import StandardScaler

from flask import jsonify, render_template, request
import pandas as pd
import numpy as np


# let's load the model here 

with open('Models/ridge.pkl', 'rb') as f:
    ridge_model = pickle.load(f)

with open('Models/scaler.pkl', 'rb') as f:
    scaler_model = pickle.load(f)


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')



@app.route("/predictions", methods = ['POST', 'GET'])
def pedict_data():
    if request.method == "POST":
        month = int(request.form.get('month'))
        Temperature=float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        month_sin = np.sin(2 * np.pi * month / 12)
        month_cos = np.cos(2 * np.pi * month / 12)

        scaled_input = scaler_model.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region, month_sin, month_cos]])
        result = ridge_model.predict(scaled_input)


        return render_template('home.html', result = result[0])
    
    else:
        return render_template('home.html')





if __name__=="__main__":
    app.run(host="0.0.0.0")