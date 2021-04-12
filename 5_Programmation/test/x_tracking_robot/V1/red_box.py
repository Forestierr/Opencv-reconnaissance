#detection boite rouge
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX

#résolution de l'image
ret = cap.set(3,640)
ret = cap.set(4,480)

def calc(x ,y, h, w):
    m_x = int(x + (w / 2))
    m_y = int(y + (h / 2))
    
    if m_x > 320:
        #print('droite',m_x)
        t1 = ('D')
    else:
        #print('gauche',m_x)
        t1 = ('G')
        
    if m_y > 240:
        #print('bas',m_y)
        t2 = ('B')
    else:
        #print('haut',m_y)
        t2 = ('H')
        
    return t1 + t2

#première image
ret, frame = cap.read()

#première position de la fenetre
r,h,c,w = 250,90,400,125
track_window = (c,r,w,h)

#set up the ROI for traking
roi = frame[r:r+h,c:c+w]
hsv_roi = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi,np.array((-10.,100.,100.)),np.array((10.,255.,255.)))
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
        
        text = calc(x, y, h, w)
        
        #dessin des deux lignes
        cv2.line(frame,(320,0),(320,480),(100,100,100),1)
        cv2.line(frame,(0,240),(640,240),(100,100,100),1)
        
        cv2.putText(frame,text,(x,y),font,1,(255,0,0),1,cv2.LINE_AA)
        
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