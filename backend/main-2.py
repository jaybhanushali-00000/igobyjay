from fastapi import FastAPI
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from numpy import array
import requests


app = FastAPI() 


origins = [
    "https://igobyjay-3ee1f.web.app",
    "https://igobyjay.pages.dev"
    "http://localhost:3000"
    ]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)



#reading credentials
df = pd.read_csv('auth_creds.csv')
print(df)
x = df['user_id']
y = df['password']
x = np.array(x)
x = x.reshape(-1,1)
y = np.array(y)
y = y.reshape(-1,1)


def authenticate(user_id,password):
    for i in range(len(x)):
        if(x[i]==user_id):
            break
    if(y[i]==password):
        return(1)
    else:
        return(0)
            
        
@app.get("/")
def home():
    return {
        "server running mast"
    }

@app.get("/auth/{user_id}_{password}")
def auth(user_id:str,password:str):
    b = authenticate(user_id,password)
    return{
        "value":b
    }
    

@app.get("/fibonacci/{num1}_{num2}_{num3}_{num4}")
def fibonacci(num1:int,num2:int,num3:int,num4:int):
    url = "http://172.18.0.86/"+"fibonacci/"+num1+"_"+num2+"_"+num3+"_"+num4
    response = requests.get(url)
    response_json = response.json()
    print(response_json["value"])
    return{
        "value": response_json["value"]
    }