import io
import os
import tensorflow as tsf
import numpy as npy

AGENT_V0 = "v1.h5"
path = os.path.join(os.getcwd(),"agents",AGENT_V0)
 
model = tsf.keras.models.load_model(path)
print(model.summary())

def predictor(img):
    img = npy.reshape(img,(1,28,28,3))
    print(img.shape)
   //creating model prediction
    y_prediction = model.predict(img)
    return npy.argmax(y_prediction[0])
   
    
