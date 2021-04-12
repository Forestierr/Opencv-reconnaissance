#corner_detection.py / 18.11.2020 / Robin Forestier
#Harris corner detection
#import de la bibliothèque opencv
import cv2
import numpy as np

#charge l'image minecraft.jpg dans img
img = cv2.imread('sudoku.jpeg')
#convertion de l'image en nuance de gris
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
#detection des coins
dst = cv2.cornerHarris(gray,2,3,0.04)

dst = cv2.dilate(dst,None)
#choix de la couleur et  la valeurmde seuil
img[dst>0.04*dst.max()]=[0,0,255]

#affiche img / titre = mon image
cv2.imshow('mon image', img)

#attendre qu'une touch soit pressée
cv2.waitKey(0)
#ferme toutes les fenêtre
cv2.destroyAllWindows()