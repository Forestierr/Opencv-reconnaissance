#meanshift.py / 18.11.2020 / Robin Forestier
#import de la bibliothèque OpenCv
import cv2
import numpy as np

#sélection de la caméra
cap = cv2.VideoCapture(0)

#première image
ret, frame = cap.read()

#première position de la fenetre
r,h,c,w = 250,90,400,125
track_window = (c,r,w,h)

#set up the ROI for traking
roi = frame[r:r+h,c:c+w]
hsv_roi = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi,np.array((0.,60.,32.)),np.array((180.,255.,255.)))
roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)

term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10,1)

#boucle infinie
while(True):
    #enregistrement de l'image dans frame
    ret, frame = cap.read()

    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
        
        #aplique meanshift pour detecter la nouvelle localisation
        ret, track_window = cv2.meanShift(dst, track_window, term_crit)
        
        #dessine sur l'image
        x,y,w,h = track_window
        img2 = cv2.rectangle(frame,(x,y),(x+w,y+h),255,2)
        
        #affiche
        cv2.imshow('img2',img2)
        cv2.imshow('f',dst)
        
        #esc to quit
        k = cv2.waitKey(60) & 0xff
        if k == 27:
            break
        
    else:
        break

#décharge de la mémoire
#fermeture de toutes les fenêtres
cap.release()
cv2.destroyAllWindows()