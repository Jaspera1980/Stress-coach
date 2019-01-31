from Furby import furby
import time
import Heart_beat_getter as bpm
import scenarios
from datetime import datetime
from time import sleep

#Input
def vocabulary(data):
    try:
        if ("furby" in data) and ("laat" in data) or ("tijd" in data):
            furby.speak("het is %s" %datetime.now().strftime("%H:%M"))
        if ("furby" in data) and ('stress' in data) or ('gestrest' in data) or ('oefening'in data):
            scenarios.activate_scenario_1()
        if ("furby" in data) and ("regen" in data) or ("regent" in data):
            furby.speak("het regent niet op dit moment")
        if ("furby" in data) and ("weer" in data):
            furby.speak("het is bewolkt met hier en daar kans op een bui")
        if ("furby" in data) and ("wat kan je" in data) or ("mogelijkheden" in data) or ("help" in data):
            furby_functionality(0.5)
        if ("furby" in data) and ("hartslag" in data) or ("meet" in data):
            furby.speak("ik ga je hartslag meten, een moment geduld")
            heart_rate = bpm.heart_rate()
            if heart_rate > 0:
                furby.speak("je hartslag is %s slagen per minuut" %heart_rate)
            else:
                furby.speak("ik kan je hartslag niet goed meten, controleer of de smartwatch goed om je pols zit")
        if ("furby" in data) and ("analyseer" in data) or ("stem" in data):
            furby.speak("ik ga je stemgeluid analyseren, een moment geduld")
            sleep(10)
            furby.speak("volgens de analyse ben je licht gestresst") 
        
    except:
        pass

def furby_functionality(pause):
    furby.speak("ik kan het volgende")
    sleep(pause)
    furby.speak("Ik kan je hartslag meten.")
    furby.speak("Als je wilt dat ik je hartslag meet kun je zeggen: hey furby meet mijn hartslag")
    sleep(pause)
    furby.speak("Ik kan je stemgeluid analyseren op stress.")
    furby.speak("Als je wilt dat ik je stem analyseer kun je zeggen: hey furby analyseer mijn stem")
    sleep(pause)
    furby.speak("Als je gestrest bent kun je mij vragen om je te helpen")
    furby.speak("Als je dat wilt kun je zeggen: hey furby ik ben gestrest")
    sleep(pause)
    furby.speak("je kunt ook het weer, de tijd en nog veel meer aan mij vragen want ik leer constant bij") 