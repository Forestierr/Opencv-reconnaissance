#qr.py / 25.11.2020 / Robin Forestier
#Programme de test de lecture de qr code
#import de la bibliothèque OpenCv et numpy
import cv2
import numpy as np

#sélection de la caméra
cap = cv2.VideoCapture(0)

#boucle infinie
while True:
    #enregistrement de l'image dans img
    ret, img = cap.read()
    
    #creation de l'objet qr CodeDetector
    qrCodeDetector = cv2.QRCodeDetector()
    
    #détection du qr code
    decodedText, points, straight_qrcode = qrCodeDetector.detectAndDecode(img)

    #test si il y a un qr code
    if points is not None:
        #affichage d'un carré bleu sur le qr code
        nrOfPoints = len(points)
        ret = cv2.minAreaRect(points)
        pts = cv2.boxPoints(ret)
        pts = np.int0(pts)
        img = cv2.polylines(img,[pts],True,255,2) 
    
        #affiche le contenu du qr code
        print(decodedText)
        
        #récupération du qr et enregistrement
        #if straight_qrcode is not None :
            #cv2.imshow('t',straight_qrcode)
            #cv2.imwrite('lastqr.png',straight_qrcode)
    else :
        print("QR not detect")
    
    #affiche du résultat
    cv2.imshow('image',img)
    
    #si touche "q" pressée arrêt de la boucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#décharge de la mémoire
#fermeture de toutes les fenêtres
cap.release()
cv2.destroyAllWindows()