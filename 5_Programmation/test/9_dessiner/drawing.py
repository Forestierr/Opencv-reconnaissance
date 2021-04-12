#drawing.py / 18.11.2020 / Robin Forestier
#import de la bibliothèque opencv et numpy
import cv2
import numpy as np

#création d'un background noir
img = np.zeros((512,512,3), np.uint8)

#création d'une diagonale bleu
img = cv2.line(img,(0,0),(511,511),(255,127,0),5)

#création d'un rectangle vert dans le coin gauche
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),2)

#création d'un cercle rougle dans le carré
img = cv2.circle(img,(447,63),63,(0,0,255),-1)

#création d'une demi-elipse bleu aux centre
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

#création d'un polygone
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))

#insertion du texte "OpenCV"
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500),font,4,(255,255,255),2,cv2.LINE_AA)

#affichage de img
cv2.imshow('test',img)

#attendre qu'une touch soit pressée
cv2.waitKey(0)
#ferme toutes les fenêtre
cv2.destroyAllWindows()