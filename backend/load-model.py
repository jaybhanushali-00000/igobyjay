from tensorflow.keras.models import load_model
import numpy as np

model = load_model('model.h5')
model.summary()
x_test = np.array([11,12,13,14,15])
prediction = model.predict(x_test)
rounded_results = [int(np.round(num)) for num in prediction]
print(x_test)
print(rounded_results)