import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler# used to standardize the data
# from sklearn.model_selection import train_test_split # used to split data for train and test
# from sklearn import svm
# from sklearn.metrics import accuracy_score
import pickle
import streamlit as st

loaded_model = pickle.load(open('saved_diabetes.sav','rb'))
    # page title
st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
col1, col2 = st.columns(2)
    
with col1:
    Pregnancies = st.text_input('Number of Pregnancies')
        
with col2:
    Glucose = st.text_input('Glucose Level')
    
with col1:
    BloodPressure = st.text_input('Blood Pressure value')
    
with col2:
    SkinThickness = st.text_input('Skin Thickness value(avg ~30)')
    
with col1:
    Insulin = st.text_input('Insulin Level')
    
with col2:
    BMI = st.text_input('BMI value')
    
with col1:
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function (avg ~0.47)')
    
with col2:
    Age = st.text_input('Age of the Person')
    
    
# code for Prediction
diab_diagnosis = ''
    
# creating a button for Prediction
    
if st.button('Diabetes Test Result'):
    diab_prediction = loaded_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
    if (diab_prediction[0] == 1):
        diab_diagnosis = 'The person is diabetic'
    else:
      diab_diagnosis = 'The person is not diabetic'
        
st.success(diab_diagnosis)

