#segmentation.py / 25.11.2020 / Robin Forestier
#import de la bibliothèque opencv
import numpy as np
import cv2

#charge l'image robin.png dans my_image
img = cv2.imread('forme.png') 

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,250,255,cv2.THRESH_BINARY_INV)

contours, h = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    perimetre = cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,0.01*perimetre,True)
    
    M = cv2.moments(cnt)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
    else:
        cx,cy = 0,0
    cv2.drawContours(img,[cnt],-1,(0,255,0),2)

    if len(approx)==3:
        shape = "triangle"
    elif len(approx) == 4:
        (x,y,w,h) = cv2.boundingRect(approx)
        ratio = w/float(h)
        if ratio >= 0.95 and ratio <= 1.05:
             shape = "carre"
        else:
              shape = "rectangle"
    elif len(approx) == 5:
           shape = "pentagone"
    elif len(approx) == 6:
        shape = "hexagone"
    else:
        shape = "cercle"
    cv2.putText(img,shape,(cx,cy),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),2)

#affichage du résultat
cv2.imshow('image', img)
cv2.imshow('iage', thresh)

#attendre qu'une touch soit pressée
cv2.waitKey(0)
#ferme toutes les fenêtre
cv2.destroyAllWindows()
