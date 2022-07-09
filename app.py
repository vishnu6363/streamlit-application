# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 17:50:28 2022

@author: VISHNU
"""

import pickle
import streamlit as st
import numpy as np
import pandas as pd
#from flask import jsonify
import json
import streamlit_option_menu


from streamlit_option_menu import option_menu
#loding the saved model
house_price=pickle.load(open('D:\\project\\learn and build\\bnglr house price\\house_price.pkl','rb'))
car_price=pickle.load(open('D:\project\learn and build\carprice\carpricemodel.pkl','rb'))
heart=pickle.load(open('D:\project\learn and build\heart\heart.pkl','rb'))
bank_note=pickle.load(open('D:\\banknoteauthentication\\banknote.pkl','rb'))

#silde bar for navigation

with st.sidebar:
    
    selection = option_menu('learn and build project 3',
                            ['heart deseases prediction',
                             'banglore house price',
                             'bank note authentication',
                             
                            'car price prediction'],
                            default_index=0)
if selection == 'heart deseases prediction':
    #page title
    st.title('Heart Deseases Prediction')
    
    age =st.number_input("Enter your age",min_value=21,max_value=80)
    trest=st.text_input("Enter the  resting blood pressurs")
    chol=st.text_input('Enter the cholestrol Level')
    thalach=st.text_input("The person's maximum heart rate achieved")
    oldpeak=st.number_input("Enter the old peak range",min_value=0,max_value=6)
    sex=st.selectbox("Enter the Gender",('Male','Female'))
    
    if sex== "Male":
        s1=0
        s2=1
    else:
        s1=1
        s2=0
    cp=st.selectbox("Enter the Chest Pain Type",("typical angina","atypical angina","non-anginal pain","asymptomatic"))
    if cp=="typical angina":
        cp0=0
        cp1=0
        cp2=0
        cp3=0
    elif cp=="non-anginal pain":
        cp0=0
        cp1=0
        cp2=1
        cp3=0
    elif cp=="atypical angina":
        cp0=0
        cp1=1
        cp2=0
        cp3=0  
    else: 
        cp0=0
        cp1=0
        cp2=0
        cp3=1
    fb=st.number_input("Enter fasting blood sugar")
    if fb>120:
        fbs0=1
        fbs1=0
    else:
        fbs1=1
        fbs0=0
    resteg=st.selectbox("Enter resting electrocardiographic results",("normal",
                                                                      "having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)",
                                                                      "showing probable or definite left ventricular hypertrophy by Estes' criteria"))
    if resteg=="showing probable or definite left ventricular hypertrophy by Estes' criteria":
        res0=0
        res1=0
        res2=1
    elif resteg=="normal":
        res0=1
        res1=0
        res2=0
    else:
        res0=0
        res1=1
        res2=0
    exang=st.selectbox("exercise induced angina",("Yes","No"))
    if exang=="Yes":
        ex0=1
        ex1=0
    else:
        ex0=0
        ex1=1
    slpoe=st.selectbox("the slope of the peak exercise ST segment",("upsloping","flat","downsloping"))
    if slpoe=="downsloping":
        slp0=0
        slp1=0
        slp2=1
    elif slpoe=="flat":
        slp0=0
        slp1=1
        slp2=0
    else:
        slp0=1
        slp1=0
        slp2=0
    ca=st.selectbox("Enter number of major vessels (0-4) colored by flourosopy",(0,1,2,3,4))
    if ca==0:
        ca0=1
        ca1=0
        ca2=0
        ca3=0
        ca4=0
    elif ca==1:
         ca0=0
         ca1=1
         ca2=0
         ca3=0
         ca4=0
    elif ca==2:
         ca0=0
         ca1=0
         ca2=1
         ca3=0
         ca4=0
    elif ca==3:
         ca0=0
         ca1=0
         ca2=0
         ca3=1 
         ca4=0
    else: 
        ca0=0
        ca1=0
        ca2=0
        ca3=0 
        ca4=1
    thal=st.selectbox("Enter the thalassemia value",( "3 = normal",
                                                     " 6 = fixed defect",
                                                     " 7 = reversable defect",
                                                     "thalsev: not used ,thalpul: not used"))
    if thal=="3 = normal":
        thal0=1
        thal1=0
        thal2=0
        thal3=0
   
    elif thal=="6 = fixed defect":
            thal0=0
            thal1=1
            thal2=0
            thal3=0  
    elif thal==" 7 = reversable defect":
         thal0=0
         thal1=0
         thal2=1
         thal3=0 
    else:
         thal0=0
         thal1=0
         thal2=0
         thal3=1
         
         
    result=''
    if st.button('Press Here'):
        desies=heart.predict([[age,trest,chol,thalach,oldpeak,s1,s2,cp0,cp1,cp2,cp3,fbs0,fbs1,res0,res1,res2,ex0,ex1,slp0,slp1,slp2,ca0,ca1,ca2,ca3,ca4,thal0,thal1,thal2,thal3]]) 
        if desies==1:
          result="The Person having Heart Disease"    
        else:
           result="The Person Not having Heart Disease"
    st.success(result)       
        
    
    
    
    
    
    
    
    
    
    
    
                
    
'''-------------------------------------------------------------------''' 
if selection == 'banglore house price':
    st.title('Banglore House Price Prediction')
    
    
    
    __locations=None
    __data_columns=None
    __model=None 
    with open("D:\\project\\learn and build\\bnglr house price\\columns.json") as f:
          __data_columns=json.load(f)['data_columns']
          __location=__data_columns[3:]
                   
    
    
    
    def house_prices(location,sqt,bhk,bath):
        try:
            loc_index=__data_columns.index(location.lower())
        except:
            loc_index = -1
            
            
        
       # loc_index = np.where(X.columns==location)[0][0]
        x = np.zeros(243)
        x[0] = sqt
        x[1] = bath
        x[2] = bhk
    
        if loc_index >=0:
          x[loc_index] = 1
          
        return round(house_price.predict([x])[0],3)
     
    
    
    data=pd.read_csv('D:\\project\\learn and build\\bnglr house price\\Bengaluru_House_Data.csv') 
    loc=data['location'].unique()
    
    
    location=st.selectbox('Enter the location',loc)    
    sqt=st.text_input("Enter the squrefeet")
    bath=st.text_input("Enter the number of Bathroom")
    bhk=st.text_input("Enter the number of BHK")
    result=''
    
    if st.button('House Price in laks'):
        
        result= house_prices(location,sqt,bhk,bath)
    st.success("The Final Price in INR {} \-".format(result))
   
       











    
if(selection == 'bank note authentication'):
    
    #title
    st.title('Bank Note Authentication')
    
    
    variance=st.text_input('Enter the Variance ')
    skweness=st.text_input('Enter the Skewness ')
    curtosis=st.text_input('Enter the Curtosis ')
    entropy=st.text_input('Enter the Entropy ')
    
    Note=''
    
    if st.button('Enter'):
    
       note=bank_note.predict([[variance,skweness,curtosis,entropy]])
       
       if note[0]==1:
           Note='The Note is Original'
       else:
           Note='The Note is Fake'
    
    st.success(Note)
    
    
    







    
if selection == 'car price prediction':
    st.title('Car Price Prediction')
    
    Year = st.number_input('Car model Year',min_value=1990,max_value=2022)
    present_price=st.text_input('What is the Showroom Price?(in laks)')
    km=st.text_input('How many km Drived?')
    owner=st.selectbox('How many owners previously had the car', (0,1,2))
    fule=st.selectbox('What is the Fuke type',('Petrol','desiel','CNG'))
    if fule=='desiel':
        p=0
        d=1
    else:
        p=1
        d=0
    seller=st.selectbox('Are you Dealer or Individual',('Dealer','Individual'))
    if seller=='Dealer':
        s=0
    else:
         s=1
    transmission=st.selectbox('Transmission Manaul',('Manual car','Automatic cra'))
    if transmission=='Manual car':
        transmissions=1
    else:
        transmissions=0
        
    year=2020-Year 
    car_prediction=''
   # c=''
    

    if st.button('predict price'):
        car_prediction=car_price.predict([[present_price,km,owner,year,d,p,s,transmissions]])
       # c=st.write([present_price,km,owner,Year,d,p,s,transmissions])
   #car_prediction=price
    st.success(car_prediction)
        
    
    
    
    
    
        
    
        

