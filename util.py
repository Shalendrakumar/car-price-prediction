import pickle
import json
import numpy as np
from sklearn.preprocessing import StandardScaler

def load_saved_artifacts():
    global model
    global scaler_model
    print("loading saved column...start")
   
    with open('./model/random_forest_regression_model.pkl', 'rb') as f:
        model = pickle.load(f)
        
    with open('./model/StandardScaler_model.pkl', 'rb') as sf:
        scaler_model = pickle.load(sf)
    #scalerfile = './model/StandardScaler_model.pkl'
    #scaler_model = pickle.load(open(scalerfile, 'rb'))        
     
    print("loading saved column...done")

def price_predict(Present_Price,Kms_Driven,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual):
    Fuel_Type_Diesel=0
    Present_Price=float(Present_Price)
    Year = int(Year)
    Year=2020-Year
    Kms_Driven=int(Kms_Driven)
    Kms_Driven2=np.log(Kms_Driven)
    Owner=int(Owner)

    if(Fuel_Type_Petrol=='Petrol'):
        Fuel_Type_Petrol=1
        Fuel_Type_Diesel=0
    else:
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=1
       
    if(Seller_Type_Individual=='Individual'):
        Seller_Type_Individual=1
    else:
        Seller_Type_Individual=0
    
    if(Transmission_Mannual=='Mannual'):
        Transmission_Mannual=1
    else:
        Transmission_Mannual=0
        
      
    scalled_val=scaler_model.transform([[Present_Price,Kms_Driven2,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual]])    
    prediction=model.predict(scalled_val)
    output=round(prediction[0],2)
    if output<0:
        return ("Sorry you cannot sell this car")
    else:
        return (output)
        
    
if __name__ == '__main__':
    load_saved_artifacts()
    abc=price_predict(5.59,27000,3,2019,0,1,0,1)
    xyz=price_predict(9.85,6900,0,2017,0,1,0,1)
    print(abc)
    print(xyz)
    
