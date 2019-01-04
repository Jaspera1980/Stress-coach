from Furby import furby
import time
import Heart_beat_getter
#import os


#Input 
def vocabulary(data):
    try:
        if "how are you" in data:
            furby.speak("I am fine")
            print("I am fine")
            
        if "heart rate" in data:
            bpm = Heart_beat_getter.heart_rate()
            furby.speak("Your heart rate is %s" %bpm)
    
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


# In[15]:


def run_furby():
    time.sleep(2)
    while 1:
        vocabulary(furby.speech_to_text())
        
run_furby()


