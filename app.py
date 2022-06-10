
#from crypt import methods
import numpy as np
import pandas as pd
import pickle
import os
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods= ["GET","POST"])
def predict():
    # columns = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
    #    'Loan_Amount_Term', 'Credit_History', 'Property_Area', 'log_LoanAmount',
    #    'log_TotalIncome']

    user_input=np.zeros(10)
    user_input[0]=request.form['gender']
    user_input[1]=request.form['married']
    user_input[2]=request.form['dependents']
    user_input[3]=request.form['education']
    user_input[4]=request.form['self_employed']
    user_input[5]=np.log(float(request.form['loan_term']))
    user_input[6]=request.form['credit_history']
    user_input[7]=request.form['property_area']
    user_input[8]=np.log(float(request.form['loan_amt']))
    user_input[9]=np.log(float(request.form['applicant_income']))
    #user_input[10]=request.form['co_applicant_income']

 
    print(user_input)

    with open(r'D:\Python\Python Programming\My practice\06_04_AWS_Deployment\project\artifacts\model.pkl','rb') as file:
        model=pickle.load(file)
        prediction= model.predict([user_input])
        if prediction[0]==1:
            result= "Approved"
        else:
            result= "Not Approved"
        print(prediction, result)


    data= request.form
    print(data)
    return render_template('display.html', u_data=data,status_ln=result)

    # with open(r'D:\Python\Python Programming\My practice\06_04_AWS_Deployment\project\artifacts\model.pkl','rb') as file:
    #     model=pickle.load(file)
    #     prediction= model.predict(user_input)
    #     print(prediction)
#return render_template("prediction.html",result=prediction[0])
# @app.route('/data',methods =['GET','POST'])
# def data():
#     data1= request.form
#     print(data1)
#     return render_template('display.html', u_data=data1)
 
# ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
#        'Loan_Amount_Term', 'Credit_History', 'Property_Area', 'log_LoanAmount',
#        'log_TotalIncome']

if __name__== "__main__":
    app.run(host= "0.0.0.0",port=8080, debug=True) ##### AWS Deployment host = 0.0.0.0 port= 8080 debug= False
