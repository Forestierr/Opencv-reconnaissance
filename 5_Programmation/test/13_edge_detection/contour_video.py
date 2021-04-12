#contour_video.py / 18.11.2020 / Robin Forestier
#import de la bibliothèque opencv
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    #passe image en gris
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    #réalisation d'un seuillage
    ret, thresh = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY)

    thresh = cv2.GaussianBlur(thresh,(5,5),5)
    
    #recherche des contours
    contours, hierarchy = cv2.findContours(thresh,1, 2)
    
    for contour in contours:
        cnt = contour

        #rectangle
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(img,[box],0,(0,255,0),2)


    #affiche my_image / titre = mon image
    cv2.imshow('mon image', img)
    cv2.imshow('th',thresh)

    #si touche "q" pressée arrêt de la boucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#décharge de la mémoire
#fermeture de toutes les fenêtres
cap.release()
cv2.destroyAllWindows()    