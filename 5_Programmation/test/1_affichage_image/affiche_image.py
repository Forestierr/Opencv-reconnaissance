#affiche_image.py / 18.11.2020 / Robin Forestier
#import de la bibliothèque opencv
import cv2

#charge l'image minecraft.jpg dans my_image
my_image = cv2.imread('minecraft.jpg') 

#affiche my_image / titre = mon image
cv2.imshow('mon image', my_image)

#attendre qu'une touch soit pressée
cv2.waitKey(0)
#ferme toutes les fenêtre
cv2.destroyAllWindows()