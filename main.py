################################
###########LIBRAIRIES###########
################################
import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import time
import os
import locale
import meteo
import blague
import RecVoacale
import RecFaciale
locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')

################################
#########INITIALISATION#########
################################
engine = pyttsx3.init()
engine.setProperty("voice", "french")
engine.setProperty('rate', 200)
engine.setProperty('volume', 0.9)

################################
############VARIABLES###########
################################
repeat = False

################################
#######PRE-ENREGISTREMENT#######
################################
sentence = gTTS(text="Oui j'écoute?", lang='fr', slow=False)
sentence.save("yes.mp3")
sentence = gTTS(text="J'ai pas compris", lang='fr', slow=False)
sentence.save("repeat.mp3")
sentence = gTTS(text="Je peux pas répondre", lang='fr', slow=False)
sentence.save("unknown.mp3")

################################
#########ANALYSE VOCALE#########
################################
def listen():
    print("Ecoute")
    r = sr.Recognizer()
    speech = sr.Microphone(device_index=9)
    with speech as source:
        audio = r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Analyse")
        text = r.recognize_google(audio, language = 'fr-FR')
        return text
    except sr.UnknownValueError:
        return ""
    except sr.RequestError as e:
        os.system("mpg321 unknown.mp3")
        return ""

while true :
    
    ################################
    ########DETECTION VOCALE########
    ################################
    while (listen().find("Google") == -1 and repeat == False):
        print(".")
    if repeat == False:
        os.system("mpg321 yes.mp3")
    repeat = False
    text = listen()
    
    ################################
    ######APPEL DE FONCTIONS########
    ################################
    RecVocale.météo()
    time.sleep(1)
    RecVocale.horaire()
    time.sleep(1)
    RecVocale.racismeapprouvé()
    time.sleep(1)
    RecVocale.musique()
    time.sleep(1)
    RecVocale.blague()
    time.sleep(1)
    RecVocale.brumisateur()
    time.sleep(1)
    
    ################################
    #########REPONSE VOCALE#########
    ################################
    sentence.save("text.mp3")
    os.system("mpg321 text.mp3")