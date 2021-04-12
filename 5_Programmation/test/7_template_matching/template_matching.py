#template_matching.py / 18.11.2020 / Robin Forestier
#import de la bibliothèque OpenCv et numpy
import cv2
import numpy as np

#charge l'image minecraft.jpg dans my_image
img = cv2.imread('minecraft.jpg',0)
#charge l'image a rechercher steve.jpg dans template
template = cv2.imread('steve.jpg',0)

#taille de template
w, h = template.shape[::-1]

#matching des images 
res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

threshold = 0.8

loc = np.where(res >= threshold)

#affichage des carrés noirs
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h),(0,255,255))
 
#affiche img / titre = Detected
cv2.imshow('Detected',img)

#attendre qu'une touch soit pressée
cv2.waitKey(0)
#ferme toutes les fenêtre
cv2.destroyAllWindows()