# Utilisation de la caméra 

Pour réaliser des codes fonctionnant en temps réel, nous allons utiliser la caméra. 

|Nom |Utile |Liens |Prix |
|:---- |:---:   |:----|:--- |
|Raspberry Pi cam V1.3|✔|[Raspberry cam (v2)](https://www.raspberrypi.org/products/camera-module-v2/)|30 .-|

<h3>Instalation de la caméra</h3>

Pour brancher la caméra veiller à :
- Ne pas être charger en électriciter static.
- Débrancher l'alimentation de votre Raspberry Pi.

<p> <img src="http://172.16.32.230/Forestier/reconnaissance-visuel/raw/master/1_Documentation/img/install_cam.gif"  width="400" height="200"> </p>

- Dans les réglages d'interface de Raspberry Pi, activer la caméra.

<h3>Tester la caméra </h3>

Pour tester la caméra taper la commande suivante dans votre terminal.

>>>
Prendre une photo :
`raspistill -o photo_01.jpg -t 5000` <br>
Prendre une vidéo :
`raspivid -o video_01.h264 -t 5000` <br>
>>>


## Code

```python
#camera.py / 18.11.2020 / Robin Forestier
#Programme de test de la caméra
#import de la bibliothèque OpenCv
import cv2 

#sélection de la caméra
cap = cv2.VideoCapture(0)

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

```

N'oublier pas la ligne `cap.release()` permetant de libérer la mémoire.

<h2> </h2>

<div align="center">
    <i>Robin Forestier</i>
</div>
