from Furby import furby
import time
from time import sleep
import Heart_beat_getter as bpm
import numpy as np
import os
from random import choice
import furby_vocabulary

#Scenario 1 script
scen1_dict = {0: "Hoi! Voel je je misschien een beetje opgejaagd?",
              1: "Ik denk dat het goed is om even iets anders te gaan doen. Ik kan je helpen met een ademhalingsoefening. Wil je dat?",
              2: "Gelukkig! Geef me een seintje wanneer je me wel nodig hebt. ",
              3: "Oké! Hier komt een ademhalingsoefening. ",
              4: "Dat was de oefening. Wat vond je ervan? ",
              5: "Oké, veel succes! Geef  me een seintje wanneer je me weer nodig hebt.", 
              6: "Oké! Wil je dan misschien iets anders doen? ",
              7: "Oké, geef me een seintje wanneer je me wel nodig hebt.",
              8: "Ik kan je helpen met een yoga-oefening, wil je dat? ",
              9: "Oké, laat me weten welke oefening je mij in de toekomst zou willen laten voorstellen.",
              10: "Oké, hier komt een Yoga-oefening.",
              11: "Ik begrijp het antwoord niet, je kunt Ja of Nee als antwoordt geven",
              12: "De oefening wordt afgebroken",
              13: "Ik zal nu de oefening starten",
              14: "Oké, ik probeer daar in de toekomst rekening mee te houden"}

#Function of ja of nee antwoordt
def ja_of_nee():
    for count in range(3):
        answer = furby.speech_to_text()
        if "ja" in answer:
            print('antwoord is ja')
            return "ja"
        if "nee" in answer:
            print('antwoord is nee')
            return "nee"
        if count == 2:
            furby.speak(scen1_dict[12])
        else:
            furby.speak(scen1_dict[11])
            
def feedback():
    furby.speak(scen1_dict[4])
    feedback = furby.speech_to_text()
    furby.speak(scen1_dict[5])
    #sleep(30)
    heart_rate = bpm.heart_rate()
    print(heart_rate)
    return feedback, heart_rate


def scenario1():
    #ask first yes no no question
    furby.speak(scen1_dict[0])
    answer = ja_of_nee()
    if answer is 'ja':
        #ask if user want to do an exercise
        furby.speak(scen1_dict[1])
        answer2 = ja_of_nee()
        if answer2 is 'ja':
            #play exercise file
            furby.speak(scen1_dict[13])
            sleep(5)
            #os.system("mpg321 /home/pi/Downloads/Test/Audio_files/3min-ademruimte.mp3")
            #print("mpg321 3min-ademruimte.mp3")
            #ask feedback on the exercise
            _feedback = feedback()
            #log answer + heart rate in database
        if answer2 is 'nee':
            #Ask if user wants to do an other exercise
            furby.speak(scen1_dict[6])
            answer4 = ja_of_nee()
            if answer4 is 'ja':
                #Suggest a other exercise
                furby.speak(scen1_dict[8])
                answer5 = ja_of_nee()
                if answer5 is 'ja':
                    #the user reacts possitive play the exericse
                    furby.speak(scen1_dict[10])
                    sleep(5)
                    print('yoga oefening wordt afgespeeld') 
                    #os.system("mpg321 /home/pi/Downloads/Test/Audio_files/suggestieve_ontspanningsoefening.mp3")
                    #ask feedback on the exercise
                    _feedback = feedback()
                    #log answer + heart rate in database
                if answer5 is 'nee':
                    #ask which exercises the user prefers in the future
                    furby.speak(scen1_dict[9])
                    answer7 = furby.speech_to_text()
                    furby.speak(scen1_dict[14])
                    #log answer to database
            if answer4 is 'nee':
                furby.speak(scen1_dict[7])
    if answer is 'nee':
        furby.speak(scen1_dict[2])


#Variables
bpm_threshold = 60

#Scenarios where randomly can be choosen from
intervention = [scenario1]

#Function to determine is scenario should be run or not
def run_intervention():
    #set initial heart rate to zero
    heart_rate = bpm.heart_rate()
    if heart_rate > bpm_threshold:
        choice(intervention)()
    else:
        print('hartslag is %s, een intervention is niet nodig' %heart_rate)

#Set timeout duration
min_duration = 10 #seconds
max_duration = 20 #seconds

def main():
    timeout = np.random.randint(min_duration, max_duration)
    timeout_start = time.time()
    while 1:
        #After a set time the heart rate will measured and a random intervention will be suggested
        #if the user is stressed (has an increased heart rate)
        if time.time() > timeout_start + timeout:
            #Run function here
            run_intervention()
            #Reset timer
            timeout = np.random.randint(min_duration, max_duration)
            timeout_start = time.time()
            continue
        else:
            time.sleep(1)
            text = furby.speech_to_text()
            furby_vocabulary.vocabulary(text)
            continue

main()
