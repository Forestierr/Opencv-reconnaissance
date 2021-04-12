#simple.py / 18.11.2020 / Robin Forestier
#import de la bibliothèque opencv
import cv2

#charge l'image sudoku.jpeg dans img
img = cv2.imread('sudoku.jpeg',0)

#réalisation du seuillage
ret, thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

#affichage de l'image original et de l'image modifiée
cv2.imshow('thresh',thresh)
cv2.imshow('original',img)

#attendre qu'une touch soit pressée
cv2.waitKey(0)
#ferme toutes les fenêtre
cv2.destroyAllWindows()