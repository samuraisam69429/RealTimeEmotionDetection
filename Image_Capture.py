#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('pip install opencv-python')


# In[4]:


import cv2 #opencv
import os
import time
import uuid


# In[5]:


IMAGES_PATH = 'C:\samarth\Seminar\implementation\Tensorflow\workspace\images\collectedimages'


# In[6]:


labels = ['Happy', 'Sad', 'Suprise', 'Anger','Neutral']
number_imgs = 15


# In[7]:


for label in labels:
    get_ipython().system("mkdir {'C:\\samarth\\Seminar\\implementation\\Tensorflow\\workspace\\images\\collectedimages\\\\'+label}")
    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        imgname = os.path. join(IMAGES_PATH, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()


# In[ ]:




