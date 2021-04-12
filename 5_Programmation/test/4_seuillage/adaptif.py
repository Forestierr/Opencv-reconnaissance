#adaptif.py / 18.11.2020 / Robin Forestier
#import de la bibliothèque opencv
import cv2

#charge l'image sudoku.jpeg dans img
img = cv2.imread('sudoku.jpeg',0)

#réalisation du seuillage adaptif gaussian
th = cv2.adaptiveThreshold(img, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
#réalisation du seuillage adaptif moyen
th2 = cv2.adaptiveThreshold(img, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

#affichage de l'image original et des images modifiées
cv2.imshow('gauss', th)
cv2.imshow('gauss mean', th2)
cv2.imshow('original',img)

#attendre qu'une touch soit pressée
cv2.waitKey(0)
#ferme toutes les fenêtre
cv2.destroyAllWindows()