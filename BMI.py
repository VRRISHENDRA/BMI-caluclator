import streamlit as st
st.title('BMI Calculator')
st.write('Please enter your details below:')
name = st.text_input('Name')
gender = st.radio('Gender', ('Male', 'Female', 'Other'))
age = st.number_input('Age', min_value=0, max_value=120)
address = st.text_area('Address')
hobbies = st.multiselect('Hobbies', ['Reading', 'Sports', 'Music', 'Cooking'])
weight = st.number_input('Weight (kg)', min_value=0.0, max_value=300.0, step=0.1)
height = st.number_input('Height (cm)', min_value=1.0, max_value=300.0, step=0.1)
if st.button('Calculate BMI'):
 height_m = height / 100
 bmi = round(weight / (height_m ** 2), 2)
 st.write('Your BMI is:', bmi)
 if bmi < 18.5:
 st.write('You are underweight.')
 elif bmi < 25:
 st.write('You have a normal weight.')
 elif bmi < 30:
 st.write('You are overweight.')
 else:
 st.write('You are obese.')
