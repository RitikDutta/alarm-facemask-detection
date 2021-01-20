import cv2
import time
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import os
beep = lambda x: os.system("echo -n '\a';sleep 0.2;" * x)
import cv2
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import os
from os import system
beep = lambda x: os.system("echo -n '\a';sleep 0.2;" * x)


# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5')

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
import pygame

import time

pygame.init()

pygame.mixer.music.load("speech.wav")

# pygame.mixer.music.play()
# Replace this with the path to your image
#Load the saved model
video = cv2.VideoCapture(0)
count, t, smallcount = 0,0,0  
while True:
        _, frame = video.read()

        #Convert the captured frame into RGB
        im = Image.fromarray(frame, 'RGB')

        #Resizing into 128x128 because we trained the model with this image size.
        im = im.resize((224,224))
        img_array = np.array(im)

        #Our keras model used a 4D tensor, (images x height x width x channel)
        #So changing dimension 128x128x3 into 1x128x128x3 
        img_array = np.expand_dims(img_array, axis=0)

#image = Image.open('test_photo.jpg')

#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
        size = (224, 224)
#         image = ImageOps.fit(image, size, Image.ANTIALIAS)

#turn the image into a numpy array
#         image_array = np.asarray(image)

# display the resized image
#         image.show()

# Normalize the image
        normalized_image_array = (img_array.astype(np.float32) / 127.0) - 1

# Load the image into the array
        data[0] = normalized_image_array

# run the inference
        prediction = model.predict(data)
        print(prediction)
#         count = 0
#         t = 0
#         for i in range(20):
        if prediction[0][0]<prediction[0][1]:
            count+=1
#             print("Count = ", count)
        else:
#             smallcount=0
#             for j in range(5):
            if prediction[0][0]>prediction[0][1]:
                smallcount+=1
#                 print("Small Count = ",smallcount)
#                 print(prediction[0][0])
            else:
                smallcount=0
                print("Small Count 2 = ",smallcount)
            if smallcount == 5:
                t=1
#                 print("t = ",t)
                
            if t ==1:
                count=0
                smallcount=0
        if count == 20:
            pygame.mixer.music.play()
            count=0
            time.sleep(5)

#             print("No Mask")
        cv2.imshow("Capturing", frame)
        key=cv2.waitKey(1)
        if key == ord('q'):
            break
video.release()
cv2.destroyAllWindows()