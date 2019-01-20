from Furby import furby
import time
from time import sleep
import Heart_beat_getter as bpm
import numpy as np
import os

#Function of ja of nee antwoordt
def ja_of_nee():
    for count in range(3):
        answer = furby.speech_to_text()
        if ("ja" in answer) or ("oké" in answer) or ("goed" in answer):
            print('antwoord is ja')
            return "ja"
        if ("nee" in answer) or ("niet" in answer) or ("geen" in answer):
            print('antwoord is nee')
            return "nee"
        if count == 2:
            furby.speak(interv_text_id1[10])
        else:
            furby.speak(interv_text_id1[9])
            
def feedback():
    furby.speak(scen1_dict[4])
    feedback = furby.speech_to_text()
    furby.speak(scen1_dict[5])
    #sleep(30)
    heart_rate = bpm.heart_rate()
    print(heart_rate)
    return feedback, heart_rate
      
#Text scenario 1
interv_text_id1 = {
    0: "Hoi! Ik heb je hartslag gemeten, deze is licht verhoogd. Wil je misschien een ontspanningsoefening doen?",
    1: "Ik denk dat het goed is om even iets anders te gaan doen.",
    #%s = the exercise title should be added
    2: "Ik kan je helpen met een %s. Wil je dat?",
    3: "Oké! Als je deze oefening voor het eerst doet, geef ik eerst een uitleg. Wil je dat?",
    4: "Oké! Wil je dan misschien iets anders doen?",
    5: "Oké, geef me een seintje als je me weer nodig hebt.",
    6: "Ik start nu de uitleg.",
    7: "Oké, ik start nu de oefening",
    8: "Dat was de oefening. Geef me een seintje als je me weer nodig hebt",
    9: "Ik begrijp het antwoord niet, je kunt Ja of Nee als antwoordt geven",
    10: "De oefening wordt afgebroken"
}

#Text first exercise
exercise_dict_id1 = {
    #OEFENINGSTITLE
    "title": "ademhalingsoefening", 
    #OEFENINGSUITLEG   
    "B0": "Als je druk of gespannen bent, ben je geneigd steeds hoger te gaan ademhalen.",
    "B1": "Niet lekker onderin je buik, maar hoog op de borst.",
    "B2": "Dat is een oppervlakkige, snellere en onrustigere ademhaling.",#
    "B3": "Door deze ademhalingsoefening kun je spanning wegnemen.",
    "B4": "Ga zo gemakkelijk mogelijk liggen op je rug, en sluit je ogen.",
    #OEFENINGSTEKST
    "C3": "Leg je handen op je buik. Hierdoor kun je straks voelen hoe je buik op en neer gaat.",
    "C4": "Haal diep adem door je neus. Doe dit zonder inspanning.", 
    "C5": "Trek je schouders dus niet op en zet je borst niet uit.",
    "C6": "Voel met je handen hoe je buik uitzet bij het inademen.",
    "C7": "Adem daarna via je mond langzaam, hoorbaar uit. …",
    "C8": "Voel met je handen dat je buik weer platter wordt. …",
    "C9": "Zodra je de behoefte voelt, adem je rustig via de neus weer in.",
    "C10": "Voel je buik omhoog komen.",
    "C11": "Adem weer rustig uit, via je mond.",
    "C12": "Voel je je buik weer platter worden?" ,
    "C13": "Herhaal dit een aantal keer terwijl je je concentreert op je ademhaling.",
    "C14": "…", 
    "C15": "…",
    "C16": "…",
    "C17": "…",
    "C18": "…",
    "C19": "Laat je ademhaling zo soepel verlopen, dat het een lange stroom van in en uitvloeiende lucht lijkt.",
    "C20": "…", 
    "C21": "…",
    "C22": "…",
    "C23": "Als je prettig vindt, kun je in gedachten rustig tellen, terwijl je in- en uitademt.",
    "C24:": "…",
    "C25": "Misschien lukt het niet meteen om onderin je buik adem te halen.",
    "C26": "Dat is niet erg." ,
    "C27": "Probeer het beetje bij beetje.",
    "C28": "Leg je handen steeds iets verder naar beneden op je buik, en breng je ademhaling daar rustig naar toe.",
    "C29": "…", 
    "C30": "…",
    "C31": "…"
}

#Set seconds of pause between spoken sentences
pause = 1

#Function to run exercise intro
def run_exercise_intro(exercise, pause):
    for count in range(len(exercise)):
        try:
            furby.speak(exercise['B%s' %count])
            sleep(pause)
        except:
            continue

#Function to run exercise text
def run_exercise(exercise, pause):
    for count in range(len(exercise)):
        try:
            furby.speak(exercise['C%s' %count])
            sleep(pause)
        except:
            continue      

#implementation of scenario 2
def run_intervention(interv_text, exercise):
    #Introduce exercise
    furby.speak(interv_text[1])
    sleep(pause)
    furby.speak(interv_text[2] %exercise['title'])
    #ask if user want to do an exercise
    answer = ja_of_nee()
    if answer is 'ja':
        furby.speak(interv_text[3])
        #ask if the exercise needs to be introduced
        answer2 = ja_of_nee()
        if answer2 is 'ja':
            #Run exercise intro
            furby.speak(interv_text[6])
            sleep(pause)
            run_exercise_intro(exercise, pause)
            sleep(pause)
            #Run exercise
            furby.speak(interv_text[7])
            sleep(pause)
            run_exercise(exercise, pause)
            sleep(pause)
            furby.speak(interv_text[8])
        if answer2 is 'nee':
            furby.speak(interv_text[7])
            sleep(pause)
            #Run exercise
            run_exercise(exercise, pause)
            sleep(pause)
            furby.speak(interv_text[8])
    if answer is 'nee':
        #Ask if the user wants do a alternative exercise
        furby.speak(interv_text[4])
        answer3 = ja_of_nee()
        if answer3 is 'ja':
            furby.speak(interv_text[2] %exercise['title'])
            #ask if user want to do an exercise
            answer4 = ja_of_nee()
            if answer4 is 'ja':
                furby.speak(interv_text[2] %exercise['title'])
                #ask if user want to do an exercise
                answer5 = ja_of_nee()
                if answer5 is 'ja':
                    furby.speak(interv_text[3])
                    #ask if the exercise needs to be introduced
                    answer6 = ja_of_nee()
                    if answer6 is 'ja':
                        #Run exercise intro
                        furby.speak(interv_text[6])
                        sleep(pause)
                        run_exercise_intro(exercise, pause)
                        sleep(pause)
                        #Run exercise
                        furby.speak(interv_text[7])
                        sleep(pause)
                        run_exercise(exercise, pause)
                        sleep(pause)
                        furby.speak(interv_text[8])
                    if answer6 is 'nee':
                        furby.speak(interv_text[7])
                        sleep(pause)
                if answer5 is 'nee':
                    furby.speak(interv_text[5])
            if answer4 is 'nee':
                furby.speak(interv_text[5])
        if answer3 is 'nee':
            furby.speak(interv_text[5])

run_intervention(interv_text_id1, exercise_dict_id1)

