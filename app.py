import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle
from sklearn.preprocessing import StandardScaler
st.title("Medical Diagonistic app")
st.markdown('✍️ Does women have diabetes or not? 🧑‍💻')
# step1" Load the pickel model
model=open('rfc.pickle','rb')
clf=pickle.load(model)
# step2 get the user input from the front end
pregs=st.number_input('Pregnancies',0,20,step=1)
glu=st.number_input('Glucose',40,200,40)
bp=st.number_input('BloodPressure',20,140,20)
skin=st.number_input('SkinThickness',5,100,5)
insulin=st.number_input('Insulin',14.0,846.0,14.0)
bmi=st.slider('BMI',15,70,15)
dp=st.slider('DiabetesPedigreeFunction',0.05,2.50,0.05)
age=st.slider('Age',21,90,21)

# step3: converting user input to model input
data={
    'Pregnancies':pregs,
    'Glucose':glu,
    'BloodPressure':bp,
    'SkinThickness':skin,
    'Insulin':insulin,
    'BMI':bmi,
    'DiabetesPedigreeFunction':dp,
    'Age':age
}

input_data=pd.DataFrame([data])
# st.write(input_data)
# step 4 
prediction=clf.predict(input_data)[0]
# st.write(prediction)
if st.button("prediction"):
    if prediction==0:
        st.success('Women is healthy')
    else:
        st.error('Women has diabetes')
    
