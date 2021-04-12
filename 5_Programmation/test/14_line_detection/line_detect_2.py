#line_detect_2.py / 18.11.2020 / Robin Forestier
#import de la bibliothèque opencv
import cv2
import numpy as np

#charge l'image 
img = cv2.imread('lightning.png')
#passe image en gris
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray,50,150,apertureSize = 3)

lines = cv2.HoughLinesP(edges,1,np.pi/180,10,minLineLength=10,maxLineGap=10)

for line in lines:
    x1,y1,x2,y2 = line[0]
    
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

#affiche my_image / titre = mon image
cv2.imshow('mon image', img)

#attendre qu'une touch soit pressée
cv2.waitKey(0)
#ferme toutes les fenêtre
cv2.destroyAllWindows()