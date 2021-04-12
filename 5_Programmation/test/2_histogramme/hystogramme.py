#hystogramme.py / 18.11.2020 / Robin Forestier
#import de la bibliothèque opencv et matplotlib
import cv2
from matplotlib import pyplot as plt

#charge l'image minecraft.jpg dans img en nuance de gris
img = cv2.imread('minecraft.jpg',0) 

#calcule de l'histogramme
plt.hist(img.ravel(),256,[0,256])

#affichage de l'histogramme
plt.show()