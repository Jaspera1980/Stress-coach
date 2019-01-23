from Furby import furby
import time
import Heart_beat_getter
import scenarios
from datetime import datetime

#Input
def vocabulary(data):
    try:
        if "furby" in data:
            furby.speak("Wat kan ik voor je doen?")
            answer = furby.speech_to_text()
            if ('stress' in answer) or ('gestrest' in answer)or ('oefening'in answer):
                scenarios.activate_scenario_1()
            if ("laat" in answer) or ("tijd" in answer):
                furby.speak("het is %s uur en %s minuten" %(datetime.now().strftime("%H"), datetime.now().strftime("%M")))
            if ("regen" in answer) or ("regent" in answer):
                furby.speak("het regent niet op dit moment")
            if "weer" in answer:
                furby.speak("het is bewolkt met hier en daar kans op een bui")
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
