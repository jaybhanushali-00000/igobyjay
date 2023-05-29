import pandas as pd
import numpy as np
from numpy import array
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow import keras


#a splitter function which splits sequence into input of n ( prev terms ) and output ( next term )
def sequence_splitter(sequence,n_steps):
    x,y = list(),list()
    for i in range(len(sequence)):
        end_ix = i + n_steps
        if end_ix > len(sequence)-1:
            break
        seq_x , seq_y = sequence[i:end_ix] , sequence[end_ix] 
        x.append(seq_x)
        y.append(seq_y)
    return array(x) , array(y)       



#reding data
df = pd.read_csv('gistfile1.csv')
ys = df['Fibonacci out']
# ys = np.array(ys)
# xs = np.zeros(len(ys))

# for i in range(1,len(xs)+1):
#     xs[i-1] = i

# for i in range(0,len(ys)):
#     ys[i] = float(ys[i])


#manipulating data into required format
xs , ys = sequence_splitter(ys , 4)


#adding ml model archiecture 
model = Sequential()
model.add(Dense(units=10 , activation ='relu',input_dim=4 ))
model.add(Dense(units=64,activation='relu'))
model.add(Dense(units=1))

#training dataset
model.compile(loss='mse',optimizer='adam')
model.fit(xs,ys,epochs=100)


# demonstrate prediction
x_input = array([2,3,5,8])
x_input = x_input.reshape((1,4))
results = model.predict(x_input)

#rounded_results = [int(np.round(num)) for num in results]
print(results)


#saving dataset
model.save("model_1.h5")
print("model saved to disk")

