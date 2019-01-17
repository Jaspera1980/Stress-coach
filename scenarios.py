from Furby import furby
import time
from time import sleep
import Heart_beat_getter as bpm
import numpy as np
import os

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
        
        
#Scenario 2 script
scen2_dict = {0: "Ik denk dat het goed is om even iets anders te gaan doen. Ik kan je helpen met een korte mindfulness oefening. Wil je dat?",
              1: "Oké! Omdat je deze oefening voor het eerst doet, geef ik eerst een uitleg. Wil je dat?",
              2: "Negatieve gedachten zorgen voor een vervelend of somber gevoel: ‘Het gaat vast niet lukken’ of ‘Ze vonden het vast raar wat ik zei.’ Je gedachten zijn niet ‘de waarheid’. Het zijn slechts gedachten, die komen en gaan. Door middel van deze oefening leer je gedachten te zien als voorbijgaande ideeën. ",
              3: "Ik ga nu door met de oefening. De eerste keer dat je deze oefening doet, kun je er het best even rustig voor gaan zitten. Later kun je de oefening makkelijker 'even tussendoor doen.' Heb je tijd om er even voor te gaan zitten?",
              4: "Dan bewaar ik deze oefening voor een later moment.",
              5: "Mooi! Sluit je ogen en richt je aandacht op je gedachten. Waar denk je aan? Benoem dit hardop.",
              6: "Je hoeft helemaal niets met deze gedachte te doen. Zie het als een wolkje dat voorbij drijft. Lukt het om de gedachte als een wolkje voorbij te laten drijven?",
              7: "Dat geeft niets. Oefening baart kunst. Mindfulness draait om aandacht en bewustzijn. Dit kun je nooit fout doen. Probeer het nog maar eens! {daarna korte pauze en dan naar links}",
              8: "Als er weer een gedachtenstroom op gang komt, ga dan weer terug naar deze oefening. Focus op iedere nieuwe gedachte en laat die als een wolkje voorbij drijven.",
              9: "Dat was de oefening. Geef me een seintje als je me weer nodig hebt.",
              10: "Wil je misschien iets anders doen?",
              11: "Ik kan je helpen met een yoga oefening",
              12: "Oké, geef me een seintje als je me weer nodig hebt."}

#module for exercise 1
def scen2_module_1():
    furby.speak(scen2_dict[3])
    answer_mod1 = ja_of_nee()
    if answer_mod1 is 'ja':
        furby.speak(scen2_dict[5])
        sleep(5)
        furby.speak(scen2_dict[6])
        answer_mod1_2 = ja_of_nee()
        if answer_mod1_2 is 'ja':
            furby.speak(scen2_dict[8])
            sleep(3)
            #ask feedback on the exercise
            _feedback = feedback()
            #log answer + heart rate in database
        if answer_mod1_2 is 'nee':
            furby.speak(scen2_dict[7])
            #Run other module?          
    if answer_mod1 is 'nee':
        furby.speak(scen2_dict[4])
        #Run other module?
        scen2_module_2()

#left branch of convesation
def scen2_module_2():
    furby.speak(scen2_dict[10])
    answer_mod2 = ja_of_nee()
    if answer_mod2 is 'ja':
        furby.speak(scen2_dict[11])
        sleep(3)
        #Run exercise
        #...
        #ask feedback on the exercise
        #_feedback = feedback()
        #log answer + heart rate in database
    if answer_mod2 is 'nee':
        furby.speak(scen2_dict[12])
        #stop  


#implementation of scenario 2
def scenario2():
    #start with measuring heart rate
    #bpm = bpm.heart_rate()
    #ask first yes no no question
    furby.speak(scen2_dict[0])
    answer = ja_of_nee()
    if answer is 'ja':
        #ask if user want to do an exercise
        furby.speak(scen2_dict[1])
        answer2 = ja_of_nee()
        if answer2 is 'ja':
            #play exercise file
            furby.speak(scen2_dict[2])
            sleep(5)
            #Run exercise
            scen2_module_1()
        if answer2 is 'nee':
            #Run exercise
            scen2_module_1()
    if answer is 'nee':
        scen2_module_2()
        
scenario2()
