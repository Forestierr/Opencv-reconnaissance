#contour.py / 18.11.2020 / Robin Forestier
#import de la bibliothèque opencv
import cv2
import numpy as np

#charge l'image 
img = cv2.imread('lightning.png')
#passe image en gris
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#réalisation d'un seuillage
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

#recherche des contours
contours, hierarchy = cv2.findContours(thresh,1, 2)

cnt = contours[0]

    #rectangle
#rect = cv2.minAreaRect(cnt)
#box = cv2.boxPoints(rect)
#box = np.int0(box)
#cv2.drawContours(img,[box],0,(0,255,0),2)

    #cercle
#(x,y),radius = cv2.minEnclosingCircle(cnt)
#center = (int(x),int(y))
#radius = int(radius)
#cv2.circle(img,center,radius,(0,255,0),2)

    #ellipse
#ellipse = cv2.fitEllipse(cnt)
#cv2.ellipse(img,ellipse,(0,255,0),2)

    #trait
rows,cols = img.shape[:2]
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)

x,y,w,h = cv2.boundingRect(cnt)
aspect_ratio = float(w)/h
print("ratio : ",aspect_ratio)

(x,y),(MA,ma),angle = cv2.fitEllipse(cnt)
print("angle  : ",angle)

#affiche my_image / titre = mon image
cv2.imshow('mon image', img)

#attendre qu'une touch soit pressée
cv2.waitKey(0)
#ferme toutes les fenêtre
cv2.destroyAllWindows()