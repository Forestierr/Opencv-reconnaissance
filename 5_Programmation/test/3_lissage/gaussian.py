#gaussian.py / 18.11.2020 / Robin Forestier
#import de la bibliothèque opencv
import cv2

#charge l'image noise.jpg dans original
original = cv2.imread('noise.jpg')

#réalisation du lissage (gaussian)
gaussian_image = cv2.GaussianBlur(original,(3,3),0)

#affichage de l'original et de l'image lissée
cv2.imshow('original',original)
cv2.imshow('lissée',gaussian_image)

#attendre qu'une touch soit pressée
cv2.waitKey(0)
#ferme toutes les fenêtre
cv2.destroyAllWindows()