#dense_optical_flow.py / 18.11.2020 / Robin Forestier
#import de la bibliothèque OpenCv et de numpy
import cv2
import numpy as np
import time 
#sélection de la caméra
cap = cv2.VideoCapture(0)

#première image
ret, frame1 = cap.read()
prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[...,1] = 255
prev_frame_time = 0
new_frame_time = 0
    
#boucle infinie
while(True):
    #enregistrement de l'image dans frame
    ret, frame2 = cap.read()
    next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
    
    flow = cv2.calcOpticalFlowFarneback(prvs,next,None,0.5,3,15,3,5,1.2,0)
        
    mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
    hsv[...,0] = ang*180/np.pi/2
    hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
    rgb = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR) 

    font = cv2.FONT_HERSHEY_SIMPLEX 
    new_frame_time = time.time()
    fps = 1/(new_frame_time-prev_frame_time) 
    prev_frame_time = new_frame_time 

    fps = float(fps) 

    fps = str(fps)
    cv2.putText(rgb, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)
    cv2.imshow('frame',rgb)
    
    prvs = next
        
    k = cv2.waitKey(60) & 0xff
    if k == 27:
        break

#décharge de la mémoire
#fermeture de toutes les fenêtres
cap.release()
cv2.destroyAllWindows()