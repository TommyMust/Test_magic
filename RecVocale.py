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

def météo() :
    if text.find("météo") != -1:
        sentence = gTTS(text="De quelle ville ?", lang='fr', slow=False)
        sentence.save("text.mp3")
        os.system("mpg321 text.mp3")
        ville = listen()
        temperature = meteo.temp(ville)
        print(ville)
        if temperature != 666:
            sentence = gTTS(text="Il fait " + temperature + " degrées à " + ville, lang='fr', slow=False)
        else:
            sentence = gTTS(text="Je ne connais pas cette ville désolé", lang='fr', slow=False)
            repeat = True
            
def horaire() :
    if text.find("heure") != -1:
        sentence = gTTS(text="Il est "+time.strftime("%H:%M"), lang='fr', slow=False)
            
def racismeapprouvé() :
    if text.find("singe") != -1:
        sentence = gTTS(text="Ouga bouga", lang='fr', slow=False)
            
def date() :
    if text.find("date") != -1:
        sentence = gTTS(text="Nous sommes le "+time.strftime('%d %b %Y'), lang='fr', slow=False)
            
def musique() :
    if text.find("musique") != -1:
        sentence = gTTS(text="C'est pas fait", lang='fr', slow=False)
            
def blague() :
    if text.find("blague") != -1:
        sentence = gTTS(text=blague.blague_alea(), lang='fr', slow=False)
            
def brumisateur() :
    if text.find("brumisateur") != -1:
        if text.find("allume") != -1:
            #os.system("python3 allumerBrumisateur.py")
            sentence = gTTS(text="J'allume le brumisateur", lang='fr', slow=False)
        else:
            #os.system("python3 eteindreBrumisateur.py")
            sentence = gTTS(text="J'éteint le brumisateur", lang='fr', slow=False)
        else:
            sentence = gTTS(text="Je n'ai pas compris, merci de répété", lang='fr', slow=False)
            repeat = True