#canny_edge.py / 18.11.2020 / Robin Forestier
#import de la bibliothèque OpenCv
import cv2

#sélection de la caméra
cap = cv2.VideoCapture(0)

#boucle infinie
while(1):
    #enregistrement de l'image dans frame
    ret, frame = cap.read()
    
    #réalisation des contoures
    edge = cv2.Canny(frame,100,150)
    
    #affiche l'image dans le fenêtre caméra
    cv2.imshow('caméra',edge)
    
    #si touche "q" pressée arrêt de la boucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#décharge de la mémoire
#fermeture de toutes les fenêtres
cap.release()
cv2.destroyAllWindows()