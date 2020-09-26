import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import pickle
import util

st.markdown(f"<h1 style='text-align: center; color: green;'><u>CAR PRICE PREDICTION APP</u></h1>This app will predicts the <b>Averate Selling Price</b> of Car! ", unsafe_allow_html=True)

st.info('Please select the required details at Sidebar to check the *** Selling Price *** of Car')

st.sidebar.header('User Input Features')

util.load_saved_artifacts()

year = st.sidebar.text_input('Year of Manufacture:',2015)

p_price = st.sidebar.text_input('What is the Shoroom Price ?(in Lacs):',5.0)
kms_driven = st.sidebar.text_input('How many Kilometers Drived ?:',5000)
owner = st.sidebar.selectbox('Owner has total Car:',(0,1,3))

fuel_type = st.sidebar.selectbox('What is fuel type ?',('Petrol','Diesel','CNG'))
if(fuel_type=='Petrol'):
    Fuel_Type_Petrol=1
    Fuel_Type_Diesel=0
else:
    Fuel_Type_Petrol=0
    Fuel_Type_Diesel=1

seller_type = st.sidebar.selectbox('Are you a Dealer or Individual ?',('Dealer','Individual'))
if(seller_type=='Individual'):
    Seller_Type_Individual=1
else:
    Seller_Type_Individual=0
    
transmission = st.sidebar.selectbox('Transmission type ?',('Manual','Automatic'))
if(transmission=='Mannual'):
    Transmission_Mannual=1
else:
    Transmission_Mannual=0
      
response = util.price_predict(p_price,kms_driven,owner,year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual)

st.write('')
st.write("As per your selection Car Shoroom Price is :**",p_price,"**(in Lacs), Kilometers Drived : **"
,kms_driven,"** KM, Owner has  : **",owner,"** car, Year of manufacture : **",year,"** , fuel type in Car : **",fuel_type
,"**, Selling by Dealer or Individual ? : **",seller_type,"** Transmission type : **",transmission,"**")

st.markdown(f"<h2 style='color: blue;'>So, Selling Price of Car will be <b>{response}</b> Lacs(INR) </h2>",unsafe_allow_html=True)

st.write('')
st.write('')
st.write('')
st.write("*By-   Shalendra Kumar*")
img = Image.open("shalendra.png")
st.image(img,width=120,caption='Thanks !!')

