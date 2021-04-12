# Hystogramme d'une image

Un histogramme est une représentation du nombre de pixel a une intensité lumineuse précise.

Pour afficher l’histogramme on utilise la bibliothèque pyplot. <br>
Si vous utiliser une image entièrement blanche, votre histogramme affichera une grande barre tout a droite. En insérant une image noire, la barre se situera tout à gauche. <br> 
Nous pourrons utiliser ces valeurs visualisées pour le seuillage d’image. <br>


## Code

```python
#hystogramme.py / 18.11.2020 / Robin Forestier
#import de la bibliothèque opencv et matplotlib
import cv2
from matplotlib import pyplot as plt

#charge l'image minecraft.jpg dans img en nuance de gris
img = cv2.imread('minecraft.jpg',0) 

#calcule de l'histogramme
plt.hist(img.ravel(),256,[0,256])

#affichage de l'histogramme
plt.show()

```

## Exemple

<p> <img src="http://172.16.32.230/Forestier/reconnaissance-visuel/raw/master/5_Programmation/test/2_histogramme/Exemples/01.png"  width="420" height="240"> </p>

<h2> </h2>

<div align="center">
    <i>Robin Forestier</i>
</div>
