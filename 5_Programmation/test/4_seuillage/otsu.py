#otsu.py / 18.11.2020 / Robin Forestier
#import de la bibliothèque opencv
import cv2

#charge l'image sudoku.jpeg dans img
img = cv2.imread('sudoku.jpeg',0)

#réalisation d'un lissage gaussian
blur = cv2.GaussianBlur(img,(5,5),0)
#réalisation du seuillage
ret2, otsu = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#affichage de l'image original et de l'image modifiée
cv2.imshow('otsu',otsu)
cv2.imshow('original',img)

#attendre qu'une touch soit pressée
cv2.waitKey(0)
#ferme toutes les fenêtre
cv2.destroyAllWindows()