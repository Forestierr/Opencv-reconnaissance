#segmentation.py / 23.11.2020 / Robin Forestier
#import de la bibliothèque opencv
import cv2
import numpy as np

#charge l'image 
img = cv2.imread('coins.jpg')
#convertion en gris
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#seuillage de l'image
ret,thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

#suppretion du bruit
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=2)

#back ground
sure_bg = cv2.dilate(opening,kernel,iterations=3)

#first plan
dist_tranform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_tranform,0.7*dist_tranform.max(),255,0)

#unknow region
sure_fg = np.uint8(sure_fg)
unknow = cv2.subtract(sure_bg,sure_fg)

ret, markers = cv2.connectedComponents(sure_fg)
#+ 1 pour que background oit 1 et pas 0
markers += 1
#markers unknow = 0
markers[unknow==255] = 0

#apply watersheld
markers = cv2.watershed(img,markers)
img[markers == -1] = [255,0,0]

#affiche l'image
cv2.imshow('mon image', opening)

#attendre qu'une touch soit pressée
cv2.waitKey(0)
#ferme toutes les fenêtre
cv2.destroyAllWindows()