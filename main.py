from Furby import furby
import time
from time import sleep
import Heart_beat_getter as bpm
import numpy as np
import os
from random import choice
import furby_vocabulary
import scenario1

#Heart rate threshold, the actual threshold will be determined in the onboarding
bpm_threshold = 60

#Scenarios where randomly can be choosen from
intervention = [scenario1.scenario1]

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



