
# coding: utf-8

# In[6]:


from gtts import gTTS
import os


# In[7]:


tts = gTTS('Goodmorning Ottie, merry christmas! How are you feeling today?')
tts.save('test.mp3')
os.system("mpg321 test.mp3")

