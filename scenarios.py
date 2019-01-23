from Furby import furby
import time
from time import sleep
import Heart_beat_getter as bpm
import numpy as np
import os
import exercises, interventions
from random import choice

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
            furby.speak(interventions.interv_text_id1[10])
        else:
            furby.speak(interventions.interv_text_id1[9])

def feedback():
    furby.speak(scen1_dict[4])
    feedback = furby.speech_to_text()
    furby.speak(scen1_dict[5])
    #sleep(30)
    heart_rate = bpm.heart_rate()
    print(heart_rate)
    return feedback, heart_rate

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

#Randomly select an exercise
exercise_choices = [exercises.exercise_dict_id1, exercises.exercise_dict_id2, exercises.exercise_dict_id3]

#Function to run scenario 1
def run_intervention_1(interv_text):
    #Introduce exercise
    exercise_1 = choice(exercise_choices)
    furby.speak(interv_text[1])
    sleep(pause)
    furby.speak(interv_text[2] %exercise_1['title'])
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
            run_exercise_intro(exercise_1, pause)
            sleep(pause)
            #Run exercise
            furby.speak(interv_text[7])
            sleep(pause)
            run_exercise(exercise_1, pause)
            sleep(pause)
            furby.speak(interv_text[8])
        if answer2 is 'nee':
            furby.speak(interv_text[7])
            sleep(pause)
            #Run exercise
            run_exercise(exercise_1, pause)
            sleep(pause)
            furby.speak(interv_text[8])
    if answer is 'nee':
        #Ask if the user wants do a alternative exercise
        furby.speak(interv_text[4])
        answer3 = ja_of_nee()
        if answer3 is 'ja':
            exercise_2 = choice(exercise_choices)
            furby.speak(interv_text[2] %exercise_2['title'])
            #ask if user want to do an exercise
            answer4 = ja_of_nee()
            if answer4 is 'ja':
                furby.speak(interv_text[3])
                #ask if the exercise needs to be introduced
                answer5 = ja_of_nee()
                if answer5 is 'ja':
                    #Run exercise intro
                    furby.speak(interv_text[6])
                    sleep(pause)
                    run_exercise_intro(exercise_2, pause)
                    sleep(pause)
                    #Run exercise
                    furby.speak(interv_text[7])
                    sleep(pause)
                    run_exercise(exercise_2, pause)
                    sleep(pause)
                    furby.speak(interv_text[8])
                if answer5 is 'nee':
                    furby.speak(interv_text[7])
                    sleep(pause)
            if answer4 is 'nee':
                furby.speak(interv_text[5])
        if answer3 is 'nee':
            furby.speak(interv_text[5])

#list of available interventions
intervention_choices = [run_intervention_1]

def activate_scenario_1():
    choice(intervention_choices)(interventions.interv_text_id1)
