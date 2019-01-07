
# coding: utf-8

#libraries
import pyaudio
import speech_recognition as sr
from gtts import gTTS
import os

#Get an overview of available input devices
def list_input_devices():
    p = pyaudio.PyAudio()    
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    print("Available input devices (Microphones):")
    for i in range(0, numdevices):
            if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

#Get an overview of available output devices
def list_output_devices():
    p = pyaudio.PyAudio()        
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    print("Available output devices (Speakers):")
    for i in range(0, numdevices):
            if (p.get_device_info_by_host_api_device_index(0, i).get('maxOutputChannels')) > 0:
                print("Output Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

class furby():
    #Input devices settings
    THRESHOLD = 500
    CHUNK_SIZE = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    INPUT_DEVICE = 2
    OUTPUT_DEVICE = 2
    r = sr.Recognizer()
    
    #Function to record speech
    def recordAudio(): #device_index=furby.INPUT_DEVICE, chunk_size=furby.CHUNK_SIZE, sample_rate=furby.RATE
        with sr.Microphone() as source:
            print("Zegt u het maar!")
            audio = furby.r.listen(source)
        return audio
    
    #Function to ouput speech
    def speak(audioString):
        print(audioString)
        tts = gTTS(text=audioString, lang='nl')
        tts.save("audio.mp3")
        #works only for linux
        os.system("mpg321 audio.mp3")

    #Function to convert speech to text
    def speech_to_text():
        _data = ""
        try:
            # Uses the default API key
            # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            _data = furby.r.recognize_google(furby.recordAudio(), language='nl-NL')
            print("U zei: " + _data)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return _data