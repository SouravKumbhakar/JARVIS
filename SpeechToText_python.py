# pip install SpeechRecognition
import speech_recognition as sr
import os  #To managing paths in local system
import threading #Threading deal with multiple operation run
#pip install mtranslate
from mtranslate import translate #Deals with multiple language
#pip install colorama // For terminal design
from colorama import Fore, Style, init

init(autoreset=True)

def print_loop():
    while True:
        print(Fore.GREEN +"Listning....", flush=True)
        print(Style.RESET_ALL,end="", flush=True)

def Translate_hindi_to_english(text):
    english_text = translate(text,"en-us") 
    return english_text

def Speech_To_Text_Python():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False # Its slow downs machines energy and side sound
    recognizer.energy_threshold =34000 #This specify the energy of the voice in the sence of decimal and it may change
    recognizer.dynamic_energy_adjustment_damping = 0.010
    recognizer.dynamic_energy_ratio = 1.0
    recognizer.pause_threshold = 0.3 # this is stopping condition if no sound till 0.3 sec
    recognizer.operation_timeout = None # listening with no timeout
    recognizer.pause_threshold = 0.2
    recognizer.non_speaking_duration = 0.2 # in which time gap after its responding

    with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source) # The noise is selecting wrt the source
            while True:
                print(Fore.GREEN +"Listning....", flush=True)
                
                try:
                     audio = recognizer.listen(source,timeout=None)
                     print("\r" + Fore.BLUE + "Recog.....", end="", flush=True) #\r : erase the privous one
                     recognizer_text = recognizer.recognize_google(audio).lower()  # saving text which is recognized
                     if recognizer_text:
                         trans_text = Translate_hindi_to_english(recognizer_text)
                         print("\r"+Fore.LIGHTBLUE_EX + "user: " + trans_text)
                         return trans_text
                     else:
                          return ""
                except sr.UnknownValueError:
                     recognizer_text = ""      
                finally:
                     print("\r",end="",flush=True)
                os.system("cls" if os.name == "nt" else "clear")
            stt_thread = threading.Thread(target=Speech_To_Text_Python)    
            print_thread = threading.Thread(target=print_loop) 
            stt_thread.start()
            print_loop.start()
            stt_thread.join()
            print_loop.join()

Speech_To_Text_Python()            

