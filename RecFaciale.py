################################
###########LIBRAIRIES###########
################################
import cv2

################################
########DETECTION OBJETS########
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

def RecObjet() :
    success,img = cap.read()
    classIds, confs, bbox = net.detect(img,confThreshold=0.5)
    print(classIds,bbox)
    if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)                         # Crée le rectange autour de l'objet
            cv2.putText(img, classNames[classId - 1].upper(), (box[0] + 10, box[1] + 30),   # crée le texte avec le nom de l'objet
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), thickness=2)
            cv2.putText(img, str(round(confidence * 100, 2)), (box[0] + 200, box[1] + 30),  # crée le chiffre de précision
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0),thickness=2)
            cv2.imshow("Output",img)
            cv2.waitKey(1)
            
def Facialposition():
    
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)  # construit le maillage
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:  # pour chaque maillage (de chaque visage trouvé)
            # Dessine le maillage sur le visage
            mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACEMESH_CONTOURS, drawSpec, drawSpec)
            print(faceLms) 
            x = faceLms.split(" ")
            a = x[2]
            b = float(a)
            
    return b
