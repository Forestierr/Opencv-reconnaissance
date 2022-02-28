#hsv_converter.py / 18.11.2020 / Robin Forestier
#code permetant de convertire une couleur BGR en HSV.

#récupérer la première valeur retournée, ajouté et soustraire 10
#a celle si et vous aurrez votre plage de couleur.

#import de la bibliothèque opencv et numpy
import cv2
import numpy as np

#import de l'image en BGR
color = np.uint8([[[34,87,255]]])

#convertion
hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

#affichage
print(hsv_color)