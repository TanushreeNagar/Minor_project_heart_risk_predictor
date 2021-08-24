from flask import Flask,render_template,request
import numpy as np
import joblib

model=joblib.load('regression-model-heart-risk.sav')
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')
  

@app.route('/getresults',methods=['POST'])  

def getresults():
     
    form_data=request.form
    #print(form_data)
    name=form_data['name']
    gender=float(form_data['gender'])
    Age=float(form_data['Age'])
    tc=float(form_data['tc'])
    hdl=float(form_data['hdl'])
    smoke=float(form_data['smoke'])
    bpn=float(form_data['bpn'])
    diab=float(form_data['diab'])
    
    test_data=np.array([gender,Age,tc,hdl,smoke,bpn,diab]).reshape(1,7)
    
    #model.predict(test_data)
    
    prediction=model.predict(test_data)[0]
    prediction=max(prediction,0)
    result_dict={"name":name,"risk":round(prediction,2)}

    return render_template('results.html',results=result_dict)
app.run(debug=True)