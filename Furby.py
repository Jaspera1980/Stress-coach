
# coding: utf-8

# In[1]:


#libraries
import pyaudio
import speech_recognition as sr
import os
from gtts import gTTS

#
from time import ctime
import time


# In[2]:


#main pyaudio object
p = pyaudio.PyAudio()

#Get an overview of available input devices
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
print("Available input devices (Microphones):")
for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))


# In[3]:


#Get an overview of available output devices
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
print("Available output devices (Speakers):")
for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxOutputChannels')) > 0:
            print("Output Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))


# In[4]:


class furby():
    #Input devices settings
    THRESHOLD = 500
    CHUNK_SIZE = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    INPUT_DEVICE = 3
    OUTPUT_DEVICE = 8
    r = sr.Recognizer()
    
    #Function to record speech
    def recordAudio():
        with sr.Microphone(device_index=furby.INPUT_DEVICE, chunk_size=furby.CHUNK_SIZE, sample_rate=furby.RATE) as source:
            print("Say something!")
            audio = furby.r.listen(source)
        return audio
    
    #Function to ouput speech
    def speak(audioString):
        print(audioString)
        tts = gTTS(text=audioString, lang='en')
        tts.save("audio.mp3")
        #works only for linux
        #os.system("mpg321 audio.mp3")

    #Function to convert speech to text
    def speech_to_text():
        _data = ""
        try:
            # Uses the default API key
            # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            _data = furby.r.recognize_google(furby.recordAudio())
            print("You said: " + _data)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return _data
    


# In[5]:


def furby_vocabulary(data):
    try:
        if "how are you" in data:
            #furby.speak("I am fine")
            print("I am fine")
    
# 
#         if "what time is it" in data():
#             furby.speak(ctime())

#         if "where is" in data:
#             data = data.split(" ")
#             location = data[2]
#             furby.speak("Hold on Frank, I will show you where " + location + " is.")
#             os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
    except:
        pass


# In[6]:


def run_furby():
    time.sleep(2)
    while 1:
        furby_vocabulary(furby.speech_to_text())


# In[7]:


run_furby()

