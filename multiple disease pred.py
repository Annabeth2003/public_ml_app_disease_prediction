# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 16:22:34 2023

@author: anjal
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('C:/Users/anjal/OneDrive/Desktop/books/glow/Projects/Multiple disease prediction ML/diabetes_model.sav','rb'))

heart_model = pickle.load(open('C:/Users/anjal/OneDrive/Desktop/books/glow/Projects/Multiple disease prediction ML/heart_model.sav','rb'))

parkinson_model = pickle.load(open('C:/Users/anjal/OneDrive/Desktop/books/glow/Projects/Multiple disease prediction ML/parkinsons_model.sav','rb'))

breastcancer_model = pickle.load(open('C:/Users/anjal/OneDrive/Desktop/books/glow/Projects/Multiple disease prediction ML/breastcancer_model.sav','rb'))

liver_model = pickle.load(open('C:/Users/anjal/OneDrive/Desktop/books/glow/Projects/Multiple disease prediction ML/liver_model.sav','rb'))

kidney_model = pickle.load(open('C:/Users/anjal/OneDrive/Desktop/books/glow/Projects/Multiple disease prediction ML/kidney_model.sav','rb'))


with st.sidebar:
    
    selected = option_menu('Disease Prediction System',
                         
                           ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           "Parkinson's Disease Prediction",
                           'Breast Cancer Prediction',
                           'Liver Disease Prediction',
                           'Chronic Kidney Disease Prediction'],
                           
                           icons = ['capsule-pill','capsule','heart','activity','bag-plus','bandaid'],
                           
                           default_index =0)
# Diabetes prediction page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)


# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        

# Parkinson's Prediction Page
if (selected == "Parkinson's Disease Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinson_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)

    
if(selected == 'Breast Cancer Prediction'):
    
    st.title('Breast Cancer Prediction using ML')
    
    col1, col2 = st.columns(2)
    
    with col1:
        mean_radius = st.text_input('Mean Radius')
        
    with col2:
        mean_texture = st.text_input('Mean Texture')
    
    with col1:
        mean_perimeter = st.text_input('Mean Perimeter')
    
    with col2:
        mean_area = st.text_input('Mean Area')
    
    with col1:
        mean_smoothness = st.text_input('Mean Smoothness')
    
    
    
    # code for Prediction
    breastc_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Breast Cancer Test Result'):
        breastc_prediction = breastcancer_model.predict([[mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness]])
        
        if (breastc_prediction[0] == 1):
          breastc_diagnosis = 'The person has breast cancer'
        else:
          breastc_diagnosis = 'The person does not have breast cancer'
        
    st.success(breastc_diagnosis)

    
if(selected == 'Liver Disease Prediction'):
    
    st.title('Liver Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Age = st.text_input('Age')
        
    with col2:
        TotalBilirubin = st.text_input('Total Bilirubin')
    
    with col3:
        DirectBilirubin = st.text_input('Direct Bilirubin')
    
    with col1:
        AlkalinePhosphotase = st.text_input('Alkaline Phosphotase')
    
    with col2:
        AlamineAminotransferase = st.text_input('Alamine Aminotransferase')
    
    with col3:
        AspartateAminotransferase = st.text_input('Aspartate Aminotransferase')
    
    with col1:
        TotalProtiens = st.text_input('Total Protiens')
    
    with col2:
        Albumin = st.text_input('Albumin')
        
    with col3:
        AlbuminandGlobulinRatio = st.text_input('Albumin and Globulin Ratio')
    
    
    # code for Prediction
    liver_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Liver Disease Test Result'):
        liver_prediction = liver_model.predict([[Age, TotalBilirubin, DirectBilirubin, AlkalinePhosphotase, AlamineAminotransferase, AspartateAminotransferase, TotalProtiens, Albumin, AlbuminandGlobulinRatio]])
        
        if (liver_prediction[0] == 1):
          liver_diagnosis = 'The person has liver disease'
        else:
          liver_diagnosis = 'The person does not have liver disease'
        
    st.success(liver_diagnosis)

    
if(selected == 'Chronic Kidney Disease Prediction'):
    
    st.title('Chronic Kidney Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Bp = st.text_input('Blood Pressure')
        
    with col2:
        Sg = st.text_input('SG count')
    
    with col3:
        Al = st.text_input('AL count')
    
    with col1:
        Su = st.text_input('SU count')
    
    with col2:
        Rbc = st.text_input('RBC count')
    
    with col3:
        Bu = st.text_input('BU count')
    
    with col1:
        Sc = st.text_input('SC count')
    
    with col2:
        Sod = st.text_input('SOD count')
        
    with col3:
        Pot = st.text_input('POT count')
      
    with col1:
        Hemo = st.text_input('Hemoglobin count')
    
    with col2:
        Wbcc = st.text_input('Wbcc count')
        
    with col3:
        Rbcc = st.text_input('Rbcc count')
    
    with col1:
        Htn = st.text_input('Htn count')
   
    
    
    # code for Prediction
    kidney_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Kidney Disease Test Result'):
        kidney_prediction = kidney_model.predict([[Bp, Sg, Al, Su, Rbc, Bu, Sc, Sod, Pot, Hemo, Wbcc, Rbcc, Htn]])
        
        if (kidney_prediction[0] == 1):
          kidney_diagnosis = 'The person has kidney disease'
        else:
          kidney_diagnosis = 'The person does not have kidney disease'
        
    st.success(kidney_diagnosis)