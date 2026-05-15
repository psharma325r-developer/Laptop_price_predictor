import streamlit as st
import pandas as pd
import numpy as np
import pickle
# import the model
pipe=pickle.load(open('gb.pkl','rb'))
df=pickle.load(open('df.pkl','rb'))

st.title("Laptop Price Predictor")
#brand
company=st.selectbox('Brand',df['Company'].unique())
#type of laptop
type1=st.selectbox('Type',df['TypeName'].unique())

#Ram
ram=st.selectbox('Ram(In GB)',[2,4,6,8,12,16,24,32,64])

#Weight
weight=st.number_input('Weight of the laptop(In Kg)')
#Touchscreen
touchscreen=st.selectbox('Touchscreen',['No','Yes'])
#IPS
ips=st.selectbox('IPS',['No','Yes'])

#screensize
screen_size=st.number_input('Screen Size(In Inches)',min_value=0.1)
#resolution
resolution=st.selectbox('Screen Resolution',['1920*1080','1366*768','1600*900','3840*2160','3200*1800','2880*1800','2560*1600','2560*1440','2304*1440'])

#CPU
cpu=st.selectbox('cpu',df['Cpu_brand'].unique())

#HDD
hdd=st.selectbox('HDD(In GB)',[0,128,256,512,1024,2048])

#SSD
ssd=st.selectbox('SSD(In GB)',[0,8,128,256,512,1024])

#GPU
gpu=st.selectbox('gpu',df['GPU_Brand'].unique())

#os
os=st.selectbox('OS',df['OpSys'].unique())


if st.button('Predict_Price'):
#Query
    ppi=None
    if touchscreen=='Yes':
        touchscreen=1
    else:
        touchscreen=0
    if ips=='Yes':
        ips=1
    else:
        ips=0

    resolution = resolution.replace('*', 'x')
    X_res=int(resolution.split('x')[0])
    y_res=int(resolution.split('x')[1])
    ppi=((X_res**2)+(y_res**2))**0.5/screen_size


    # query=np.array([company,type1,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])
    query = pd.DataFrame({
        'Company':[company],
        'TypeName':[type1],
        'Ram':[ram],
        'Weight':[weight],
        'Touchscreen':[touchscreen],
        'IPS_panel':[ips],
        'PPI':[ppi],
        'Cpu_brand':[cpu],
        'HDD':[hdd],
        'SSD':[ssd],
        'GPU_Brand':[gpu],
        'OpSys':[os]
    })
    # query = query.reshape(1, 12)

    st.title("The predicted price of this configuration is "+str(int(np.exp(pipe.predict(query)[0]))))