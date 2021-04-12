#masque.py / 18.11.2020 / Robin Forestier
#import de la bibliothèque opencv et numpy
import cv2
import numpy as np

#charge l'image minecraft.jpg dans my_image
my_image = cv2.imread('minecraft.jpg') 

#convertion en HSV
hsv = cv2.cvtColor(my_image, cv2.COLOR_BGR2HSV)

#créstion de la plage de couleur
#pour le calcul référer vous à hsv_converter.py
lower_green = np.array([38,50,50])
upper_green = np.array([58,255,255])

#création du mask
mask = cv2.inRange(hsv, lower_green, upper_green)

#création du reste
rest = cv2.bitwise_and(my_image,my_image,mask = mask)

#affiche my_image, du rest et du mask
cv2.imshow('mon image', my_image)
cv2.imshow('rest',rest)
cv2.imshow('mask',mask)

#attendre qu'une touch soit pressée
cv2.waitKey(0)
#ferme toutes les fenêtre
cv2.destroyAllWindows()