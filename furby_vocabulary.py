from Furby import furby
import time
import Heart_beat_getter
import scenarios
#import os


#Input 
def vocabulary(data):
    try:
        if "furby" in data:
            furby.speak("Hey wat kan ik voor je doen?")
            answer = furby.speech_to_text()
            if 'stress' in answer:
                scenarios.scenario2()
            if 'oefening'in answer:
                scenarios.scenario2()
            
            #print("I am fine")
    
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

        


