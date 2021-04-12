#ORB_detection.py / 27.01.2021 / Robin Forestier
#import de la bibliothèque opencv et numpy
import cv2
import numpy as np

def ORB_detector(new_image, image_template):
    # Fonction qui compare l'image envoyer avec la template
    # Et retourn le nombre de "matche" trouver entre les deux
    image1 = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)

    # Création d'un ORB detector avec 1000 "points" et un facteur pyramide de 1.2
    orb = cv2.ORB_create(1000, 1.2)

    # Detection des "points" (keypoints) dans l'image
    (kp1, des1) = orb.detectAndCompute(image1, None)

    # Detection des "points" dans la template
    (kp2, des2) = orb.detectAndCompute(image_template, None)

    # Creation d'un matcher 
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    # Match
    matches = bf.match(des1,des2)

    # Trit des matches en rapport a la distance
    # Petite distance est meilleur
    matches = sorted(matches, key=lambda val: val.distance)
    return len(matches)

cap = cv2.VideoCapture(0)

# Image template, image de référence
image_template = cv2.imread('red-bull.jpeg', 0) 

while True:
    ret, frame = cap.read()

    # Récupérer le nombre de matches
    matches = ORB_detector(frame, image_template)

    # Afficher le nombre de matches 
    output_string = "Matches = " + str(matches)
    cv2.putText(frame, output_string, (50,450), cv2.FONT_HERSHEY_COMPLEX, 2, (250,0,150), 2)

    # Le threshold et le seuille après lequelle on décide,
    # que l'objet se trouva dans l'image
    # Note : Avec 1000 matches, un threshold a 350 serrait égale a min 35% d matches
    threshold = 190

    if matches > threshold:
        # Affiche object found
        cv2.putText(frame,'Object Found',(50,50), cv2.FONT_HERSHEY_COMPLEX, 2 ,(0,255,0), 2)
    
    #affiche image
    cv2.imshow('Object Detector using ORB', frame)
    
    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break

cap.release()
cv2.destroyAllWindows()