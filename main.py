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
import cv2
import RecVocale
import RecFaciale
locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')

################################
############VARIABLES###########
################################
repeat = False

while true :
    
    ################################
    ########DETECTION VOCALE########
    ################################
    while (RecVocale.listen().find("Google") == -1 and repeat == False):
        print(".")
    if repeat == False:
        os.system("mpg321 yes.mp3")
    repeat = False
    text = RecVocale.listen()
    a = RecFaciale.Facialposition()
    
    if a > 0.8 :
        moteur = 1 #bouge droite
    elif a < 0.2 :
        moteur = 2 #bouge gauche
    
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
    RecFaciale.RecObjet()
    time.sleep(1)
    
    ################################
    #########REPONSE VOCALE#########
    ################################
    sentence.save("text.mp3")
    os.system("mpg321 text.mp3")
