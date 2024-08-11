import pickle
import streamlit as st
import numpy as np

model = pickle.load(open("dia.pkl",'rb'))


li=[]


with st.form("my_form"):
    gender              = st.selectbox("Gender",("Male","Female"),help="Select Gender")
    age                 = st.number_input("Age")
    hypertension        = st.selectbox("hypertension",("Yes","No"))
    heart_disease       = st.selectbox("heart_disease",("Yes","No"))
    smoking_history     = st.selectbox("smoking_history",("current","ever","former","not current","No Info"))
    bmi                 = st.number_input("bmi")
    HbA1c_level         = st.number_input("HbA1c_level")
    blood_glucose_level = st.number_input("blood_glucose_level")
    submitted              = st.form_submit_button(label="Submit")


if(gender == "Male"):
    li.append(1)
else:
    li.append(0)

li.append(age)

if(hypertension == "Yes"):
    li.append(1)
else:
    li.append(0)

if(heart_disease == "Yes"):
    li.append(1)
else:
    li.append(0)

if(smoking_history == "current"):
    li.append(2)
elif(smoking_history== "ever" ):
    li.append(3)
elif(smoking_history == "former" ):
    li.append(4)
elif(smoking_history == "not current" ):
    li.append(5)
elif(smoking_history == "never" ):
    li.append(6)
else:
    li.append(1)

li.append(bmi)
li.append(HbA1c_level)
li.append(blood_glucose_level)

predictor = np.array([li])
result1 = model.predict(predictor)
if submitted:
    if(result1 == 1):
        st.write("Sucess")
    else:
        st.write("No")