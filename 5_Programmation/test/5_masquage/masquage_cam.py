#masquage_cam.py / 18.11.2020 / Robin Forestier
#import de la bibliothèque opencv et numpy
import cv2
import numpy as np

#sélection de la caméra
cap = cv2.VideoCapture(0)

#boucle infinie
while(1):
    #enregistrement de l'image dans frame
    ret, frame = cap.read()
    
    #convertion en HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #créstion de la plage de couleur
    #pour le calcul référer vous à hsv_converter.py
    lower_blue = np.array([80,50,50])
    upper_blue = np.array([100,255,255])
    
    #création du mask
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    #création du reste
    rest = cv2.bitwise_and(frame,frame,mask = mask)
    
    #affiche rest
    cv2.imshow('rest',rest)
    
    #si touche "q" pressée arrêt de la boucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#décharge de la mémoire
#fermeture de toutes les fenêtres
cap.release()
cv2.destroyAllWindows()