#red_box_v2
#import de la bibliothèque OpenCv
import cv2
import numpy as np
import serial

ser = serial.Serial("/dev/ttyS0",baudrate=115200,timeout = 3.0)

#sélection de la caméra
cap = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX

new_pos = 5
last_pos = new_pos

ret = cap.set(12,50)
#résolution de l'image
ret = cap.set(3,640)
ret = cap.set(4,480)

def calc(point):
    t1 = ('')
    t2 = ('')
    p = 5
    x = (point[0][0] + point[2][0]) / 2
    y = (point[0][1] + point[2][1]) / 2
    
    x = int(x)
    y = int(y)
    
    if x > 270 and x < 370 and y > 190 and y < 290:
        #print("center")
        t1 = ('C')
        t2 = ('')
        p = b'\x05'
    else:
        if x > 320 and y > 240:
            t1 = ('G')
            t2 = ('B')
            p = b'\x02'
        if x > 320 and y < 240:
            #print('droite',x)
            t1 = ('G')
            t2 = ('H')
            p = b'\x04'
        if x < 320 and y < 240:
            t1 = ('D')
            t2 = ('H')
            p = b'\x03'
        if x < 320 and y > 240:
            #print('droite',x)
            t1 = ('D')
            t2 = ('B')
            p = b'\x01'
   
    return [x,y,t1,t2,p]
    
def dist(point):
    y = (((point[0][0] - point[1][0]) ** 2) + ((point[0][1] - point[1][1]) ** 2)) ** (1.0/2)
    y = int(y)
    
    if y != 0 :
        long = int(7400/y)
    else:
        long = '?'
    
    return long

#première image
ret, frame = cap.read()

#première position de la fenetre
r,h,c,w = 250,90,400,125
track_window = (c,r,w,h)

#set up the ROI for tracking
roi = frame[r:r+h,c:c+w]
hsv_roi = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi,np.array((-6.,100.,100.)),np.array((14.,255.,255.)))
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
        
        #aplique CamShift pour detecter la nouvelle localisation
        ret, track_window = cv2.CamShift(dst, track_window, term_crit)
        
        #dessine le polygone
        pts = cv2.boxPoints(ret)
        pts = np.int0(pts)
        img2 = cv2.polylines(frame,[pts],True,255,2)
        
        centre = calc(pts)
        
        ser.write(centre[4])
        print(centre[4])
        
        last_pos = centre[4]
        long = f'{dist(pts)}' + "cm"
        
        #affichage des ligne est carré
        cv2.line(frame,(320,0),(320,480),(100,100,100),1)
        cv2.line(frame,(0,240),(640,240),(100,100,100),1)
        cv2.rectangle(frame,(270,190),(370,290),(100,100,100),1)
        
        cv2.line(frame,(centre[0],centre[1]),(centre[0],centre[1]),(0,0,255),5)
        cv2.putText(frame,centre[2]+centre[3],(30,30),font,1,(255,255,255),1,cv2.LINE_AA)
        cv2.putText(frame,long,(30,60),font,1,(255,255,255),1,cv2.LINE_AA)
        
        #affiche
        cv2.imshow('img2',img2)
        cv2.imshow('f',dst)
        
        k = cv2.waitKey(60) & 0xff
        if k == 27:
            break
        
    else:
        break

#décharge de la mémoire
#fermeture de toutes les fenêtres
cap.release()
cv2.destroyAllWindows()