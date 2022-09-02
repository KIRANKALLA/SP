import pickle
import streamlit as st
pickle_in=open('SalaryP.pkl','rb')
model=pickle.load(pickle_in)
e=st.number_input('Enter experience')
if st.button('PREDICT'):
  s=model.predict([[e]]).squeeze()
  s=int(s)
  st.success(f'Salary is {s}')
     
