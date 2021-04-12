# Masquage de couleur

Le but de ce chapitre va être d’isoler une ou plusieurs couleur affichée a l’écran. <br>
Pour cela nous aurons besoin d’une plage de couleur que l’on veut isolé.<br>
Pour essayer nous allons prendre cette image : <br>

<div align="center"> <img src="http://172.16.32.230/Forestier/reconnaissance-visuel/raw/master/5_Programmation/test/5_masquage/Exemples/01.png"  width="320" height="160"> </div>

## Code

```python
#masque.py / 18.11.2020 / Robin Forestier
#import de la bibliothèque opencv et numpy
import cv2
import numpy as np

#charge l'image minecraft.jpg dans my_image
my_image = cv2.imread('minecraft.jpg') 

#convertion en HSV
hsv = cv2.cvtColor(my_image, cv2.COLOR_BGR2HSV)

#créstion de la plage de couleur
#pour le calcul référer vous à hsv_converter.py
lower_green = np.array([38,50,50])
upper_green = np.array([58,255,255])

#création du mask
mask = cv2.inRange(hsv, lower_green, upper_green)

#création du reste
rest = cv2.bitwise_and(my_image,my_image,mask = mask)

#affiche my_image, du rest et du mask
cv2.imshow('mon image', my_image)
cv2.imshow('rest',rest)
cv2.imshow('mask',mask)

#attendre qu'une touch soit pressée
cv2.waitKey(0)
#ferme toutes les fenêtre
cv2.destroyAllWindows()
```

## Calcul de la valeur HSV

```python
#hsv_converter.py / 18.11.2020 / Robin Forestier
#code permetant de convertire une couleur BGR en HSV.

#récupérer la première valeur retournée, ajouté et soustraire 10
#a celle si et vous aurrez votre plage de couleur.

#import de la bibliothèque opencv et numpy
import cv2
import numpy as np

#import de l'image en BGR
color = np.uint8([[[10,10,10]]])

#convertion
hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

#affichage
print(hsv_color)
```

### Exemple pour du bleu

>>>

RGB : 25, 50, 200  <br>
BGR : 200, 50, 25  <br>
HSV : 116, 223, 25 <br>
lower _blue => 106, 50, 50 <br>
upper_blue => 126, 255, 255 <br>

>>>

## Exemples

<div align="center">

<p> Original : <img src="http://172.16.32.230/Forestier/reconnaissance-visuel/raw/master/5_Programmation/test/5_masquage/Exemples/01.png"  width="320" height="160"> </p>
    
<p> 
Masque : <img src="http://172.16.32.230/Forestier/reconnaissance-visuel/raw/master/5_Programmation/test/5_masquage/Exemples/03.png"  width="320" height="160"> 
</p>

<p> 
Résultat : <img src="http://172.16.32.230/Forestier/reconnaissance-visuel/raw/master/5_Programmation/test/5_masquage/Exemples/02.png"  width="320" height="160">
</p>

</div>


<h2> </h2>

<div align="center">
    <i>Robin Forestier</i>
</div>
