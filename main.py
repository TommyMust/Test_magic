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

################################
######DETECTION FACIALE#########
################################
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
classNames = []
classFile = "coco.names"
with open(classFile, "rt") as f:
    classNames = f.read().rstrip("\n").split("\n")
#print(classNames) Voir tour ce qu'il y a dans coco.names
configPath = "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weightsPath = "frozen_inference_graph.pb"
net = cv2.dnn_DetectionModel(weightsPath,configPath) #Bounding : rectangle de délimitations
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

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