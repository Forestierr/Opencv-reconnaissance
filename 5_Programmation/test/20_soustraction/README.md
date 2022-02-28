# Soustration

Le but de se code est de soustraire deux image pour en resortir les différences. 

## Code

```python
'''
soustraction.py | 19.01.2021 | Robin Forestier
Programme de spustraction d'image et de récupération d'information
'''

#import de la bibliothèque OpenCv et numpy
import cv2
import numpy as np

#sélection de la caméra
cap = cv2.VideoCapture(0)

#capture la première image
ret, frame = cap.read()
s_frame = frame
#transformation en gris et dilatation
s_gray = cv2.cvtColor(s_frame, cv2.COLOR_BGR2GRAY)
s_gray = cv2.dilate(s_gray, None, iterations=2)

#boucle infinie
while(True):
    #enregistrement de l'image dans frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #soustraction des deux image (en gris)
    res =cv2.subtract(s_gray, gray,dst=None,dtype=None)
    #enregistrement de la dernoère image
    s_gray = gray
    
    #dans l'image soustraitem, réalisation  d'un lissage
    res = cv2.threshold(res, 20, 255, cv2.THRESH_BINARY)[1]
    res = cv2.dilate(res, None, iterations=10)
    #détection des contours
    cnts, hierarchy = cv2.findContours(res, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    maxy = 100
    #recherche du contour avec le plus grand périmètre
    for c in cnts:
        perimetre = cv2.arcLength(c, True)
        if maxy <= perimetre : 
            new_cnts = c
            maxy = perimetre
               
    #création d'une image avec la l'objet trouver et dessin du rectangle vert    
    x,y,w,h = cv2.boundingRect(new_cnts)
    cut_img = frame[y:y+h, x:x+w]
    cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0),1)
    
    #resize de l'image de l'objet trouver
    aff_cut_img = cv2.resize(cut_img,(640,480),interpolation=cv2.INTER_AREA)
    
    #affichage des images
    cv2.imshow('caméra',aff_cut_img) #image zommée 
    cv2.imshow('frame',frame) #image complète
    cv2.imshow('sus',res) #zonne de pixel en mouvement 
    
    #si touche "q" pressée arrêt de la boucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#décharge de la mémoire
#fermeture de toutes les fenêtres
cap.release()
cv2.destroyAllWindows()


```
