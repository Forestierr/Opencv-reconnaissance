'''
[INFO]
test_double_arm.py | 12.04.2021 | Robin Forestier
But : trouver le tournevis rouge pour indiquer sa position aux bras.
XWiki : PET'ELO | GitLab : PET'ELO
'''

import numpy as np
import cv2
from send import *
from calcul import calc

#poignée de main (ID)
'''
while True :
    if read_commande_line(1) :
        break
'''

font = cv2.FONT_HERSHEY_SIMPLEX

cap = cv2.VideoCapture(0)

# take first frame of the video
ret,frame = cap.read()

# setup initial location of window
r,h,c,w = 0,420,0,640  # simply hardcoded the values
track_window = (c,r,w,h)

# set up the ROI for tracking
roi = frame[r:r+h, c:c+w]
hsv_roi =  cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
#mask of color red
lower_red = np.array([0,120,70])
upper_red = np.array([10,255,255])
mask = cv2.inRange(hsv_roi, lower_red, upper_red)
    
lower_red = np.array([170,120,70])
upper_red = np.array([180,255,255])
mask1 = cv2.inRange(hsv_roi, lower_red, upper_red)
    
mask = mask + mask1
roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)

# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
nofp = 0
a=[0,0]
while(1):
    ret ,frame = cap.read()
    
    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
        # apply meanshift to get the new location
        ret, track_window = cv2.CamShift(dst, track_window, term_crit)

        # Draw it on image
        pts = cv2.boxPoints(ret)
        pts = np.int0(pts)
        
        M = cv2.moments(pts)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
        else :
            cx,cy = 0,0
        
        cv2.circle(frame,(cx,cy),7, (255,255,255),-1)
        img2 = cv2.polylines(frame,[pts],True, 255,2)
        
        a = calc(cx)
        nofp = nofp + 1
        
        #send UART with verification line
        read_commande_line(1,a)        
        
        cv2.imshow('img2',img2)
        cv2.waitKey(0) 
        k = cv2.waitKey(60) & 0xff
        if k == 27:
            break

    else:
        break

cv2.destroyAllWindows()
cap.release()