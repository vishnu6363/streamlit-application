# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 21:50:13 2022

@author: VISHNU
"""

from flask import Flask,request
import numpy as np
import pandas as pd
import pickle
import flasgger
from flasgger import Swagger

app=Flask(__name__)
Swagger(app)

pickle_in=open('clsifier.pkl','rb')
clasifier=pickle.load(pickle_in) 

@app.route('/')
def welcome():
    return "welecome All"

@app.route('/predict',methods=["Get"])
def predict_note_authentication():
    
    """ let's Autheticate The Bank Note
    This is using docsting for specifications.
    ---
    parameters:
        - name: variance
          in: query
          type: number
          required: true
        - name: skewness
          in: query
          type: number
          required: true
        - name: curtosis
          in: query
          type: number
          required: true
        - name: entropy
          in: query
          type: number
          required: true
    responses:
        200:
            description: The output values
            
    """      
          
    variance=request.args.get('variance')
    skewness=request.args.get('skewness')
    curtosis=request.args.get('curtosis')
    entropy=request.args.get('entropy')
    prediction=clasifier.predict([[variance,skewness,curtosis,entropy]])
    return "The predicted value is "+str(prediction) 

@app.route('/predict_file',methods=["POST"])
def note_file():
    """ let's Autheticate The Bank Note
    This is using docsting for specifications.
    ---
    parameters:
        - name: file
          in: formData
          type: file
          required: true
    response:
        200:
            description:the output values
    """
    df_test=pd.read_csv(request.files.get('file'))
    print(df_test.head())
    prediction=clasifier.predict(df_test)
    print(prediction)
    
    return str(list(prediction))
    
if(__name__=='__main__'):
    app.run(host='0.0.0.0',port=800) 












