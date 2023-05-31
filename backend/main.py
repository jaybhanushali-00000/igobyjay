#import argparse
import numpy as np
from numpy import array
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


#from numpy import loadtxt
from tensorflow.keras.models import load_model


#fastapi_app
app = FastAPI()


# #adding argument parser
# aar_par = argparse.ArgumentParser()

# #adding arguments 
# aar_par.add_argument('num1',type=float,help="number 1")
# aar_par.add_argument('num2',type=float,help="number 2")
# aar_par.add_argument('num3',type=float,help="number 3")
# aar_par.add_argument('num4',type=float,help='number 4')

# #reading arguments
# args_output = vars(aar_par.parse_args())

# #saving in array
# x_input = np.zeros(len(args_output))
# for i in range(len(args_output)):
#     x_input[i] = args_output["num"+str(i+1)]

def computing(a,b,c,d):
    #importing model
    model_1 = load_model('model_fibonacci.h5')
    
    # demonstrate prediction
    x_input = np.zeros(4)
    x_input = ([a,b,c,d])
    x_input = np.array(x_input)    
    x_input = x_input.reshape((1,4))
    results = model_1.predict(x_input)

    rounded_results = [int((num)) for num in results]
    return(rounded_results)


origins = [
    "http://localhost:3000",
    "localhost:3000"
    "https://igobyjay.pages.dev"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/')
async def home():
     return {
       "message":"Hello World"
     }

@app.get('/fibonacci/{num1}_{num2}_{num3}_{num4}')
async def fibo(num1:float,num2:float,num3:float,num4:float):
     return {
       "value":(computing(num1,num2,num3,num4))
     }


