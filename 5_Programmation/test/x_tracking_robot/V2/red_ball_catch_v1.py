#red_ball_catch_v1.py / 18.11.2020 / Robin Forestier
#first test try to catch the red ball with one arm of the robot.
#import OpenCV
import cv2 
import numpy as np
import serial
import time

#init serial
ser = serial.Serial("/dev/ttyS0",baudrate=115200,timeout = 3.0)

#sélection de la caméra
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('out.avi', fourcc,30.0, (640,480))
new_cnts = None

colour_x = (100,100,100)
colour_y = (100,100,100)

def send(x,y,radius):
    code = 0
    pos = [0,0,0]
    
    print('[moove]')
    
    if 0 < x < 280 :
        code = code + 4
        #print('g')
    elif 360 < x < 640:
        code = code + 8
        #print('d')
    else :
        pos[1] = 1
        print('x')
        colour_x = (255,0,0)
      
    if 0 < y < 200 :
        code = code + 16
        #print('h')
    elif 280 < y < 480 :
        code = code + 32
        #print('b')
    else :
        pos[2] = 1
        print('y')
        colour_y = (255,0,0)
        
    if pos[1] == 1 & pos[2] == 1 :
        if radius < 120 :      
            code = code + 1
            print('haut')
        elif radius > 140 :
            code = code + 2
            print('bas')
        else :
            code = code + 64
            print('[END] !!! GOOD !!!')
            out.release
            ser.close()
            cap.release()
            cv2.destroyAllWindows()
            exit()
        
    
    #print('b' + str(hex(code)))
    #print(bin(code))
    x = code.to_bytes(1,'little')
    print(x)
    ser.write(x)
    
    time.sleep(0.8)
    
#boucle infinie
while(True):
    #enregistrement de l'image dans frame
    ret, frame = cap.read()
    norm = cv2.normalize(frame, (np.zeros((480,640,3),np.float32)), 200, 50, cv2.NORM_INF)
    
    hsv = cv2.cvtColor(norm, cv2.COLOR_BGR2HSV)
   
    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    
    lower_red = np.array([170,120,70])
    upper_red = np.array([180,255,255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    
    mask = mask + mask1    
    
    rest = cv2.bitwise_and(frame,frame,mask = mask)
    
    th = cv2.dilate(rest, None, iterations= 2)
    th_gray = cv2.cvtColor(th, cv2.COLOR_BGR2GRAY)
    cnts, hierarchy = cv2.findContours(th_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    maxy = 1
    
    x = None
    y = None
    radius = None
    
    #recherche du contour avec le plus grand périmètre
    for c in cnts:
        perimetre = cv2.arcLength(c, True)
        if maxy <= perimetre : 
            new_cnts = c
            maxy = perimetre
    
    if new_cnts is not None :
        (x,y), radius = cv2.minEnclosingCircle(new_cnts)
        center = (int(x),int(y))
        radius = int(radius)
        cv2.circle(frame, center, radius, (0,255,0), 2)
    
    #envoie en uart
    if x and y and radius is not None:
        send(x,y,radius)
    
    cv2.line(frame,(320,0),(320,480),colour_y,1)
    cv2.line(frame,(0,240),(640,240),colour_x,1)
    
    #affiche l'image dans le fenêtre caméra
    cv2.imshow('caméra',frame)
    
    #out.write(frame)
    
    cv2.imshow('rest',rest)
    
    #si touche "q" pressée arrêt de la boucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#décharge de la mémoire
#fermeture de toutes les fenêtres
out.release
ser.close()
cap.release()
cv2.destroyAllWindows()
