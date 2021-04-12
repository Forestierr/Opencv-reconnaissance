#corner_detection.py / 18.11.2020 / Robin Forestier
#Shi-Tomasi Corner Detection
#import de la bibliothèque opencv et numpy
import cv2
import numpy as np

#charge l'image minecraft.jpg dans img
img = cv2.imread('sudoku.jpeg')
#convertion de l'image en nuance de gris
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#détections des coins (140 => nbr de coins)
corner = cv2.goodFeaturesToTrack(gray,140,0.01,10)
corner = np.int0(corner)

#affichage des coins
for i in corner:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)

#affiche img / titre = mon image
cv2.imshow('mon image', img)

#attendre qu'une touch soit pressée
cv2.waitKey(0)
#ferme toutes les fenêtre
cv2.destroyAllWindows()