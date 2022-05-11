import io
import os
import tensorflow as tf
import numpy as np

AGENT_V1 = "v1.h5"
path = os.path.join(os.getcwd(),"agents",AGENT_V1)
 
model = tf.keras.models.load_model(path)
print(model.summary())

def predictor(image):
    image = np.reshape(image,(1,28,28,3))
    print(image.shape)
    y_pred = model.predict(image)
    return np.argmax(y_pred[0])
   
    
