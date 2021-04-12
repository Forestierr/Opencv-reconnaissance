#reglage.py / 18.11.2020 / Robin Forestier
#Programme de test de la caméra
#import de la bibliothèque OpenCv
import cv2 

#sélection de la caméra
cap = cv2.VideoCapture(0)

#réglage des fps
cap.set(cv2.CAP_PROP_FPS, 50)

#réglage hauteur / largeur
ret = cap.set(3,704)
ret = cap.set(4,480)

#lecture des valeurs
h = int(cap.get(3))
w = int(cap.get(4))
fps = int(cap.get(5))

#affichage des valeurs
print("quality : ", h, " , ",w)
print("fps : ",fps)

#boucle infinie
while(True):
    #enregistrement de l'image dans frame
    ret, frame = cap.read()

    #convertion de l'image en nuance de gris
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #affiche l'image dans le fenêtre caméra
    cv2.imshow('caméra',frame)
    
    #si touche "q" pressée arrêt de la boucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#décharge de la mémoire
#fermeture de toutes les fenêtres
cap.release()
cv2.destroyAllWindows()