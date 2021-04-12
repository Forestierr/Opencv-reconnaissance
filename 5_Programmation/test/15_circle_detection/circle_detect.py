#circle_detect.py / 23.11.2020 / Robin Forestier
#import de la bibliothèque opencv
import cv2
import numpy as np

#charge l'image 
img = cv2.imread('rond.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray,5)


circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,50,
                           param1=50,param2=30,minRadius=0,maxRadius=150)

#vérification si il y a un cercles
if circles is not None :
    circles = np.uint16(np.around(circles))
    #affiches les cercles et leur centre
    for i in circles[0,:]:
        cv2.circle(img,(i[0],i[1]),i[2],(0,255,255),2)
        cv2.circle(img,(i[0],i[1]),2,(0,0,0),3)

#affiche l'image
cv2.imshow('mon image', img)

#attendre qu'une touch soit pressée
cv2.waitKey(0)
#ferme toutes les fenêtre
cv2.destroyAllWindows()