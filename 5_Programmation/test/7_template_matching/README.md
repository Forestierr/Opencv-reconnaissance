# Template matching

Le template matching permet la reconnaissance d’un bout d’image dans une image. <br>
L’algorithme est assez restrictif il sera donc compliqué de reconnaître un objet d’une autre image. <br>
Pour le test vous aurez besoin d’une image et d’un bout de cette même image. 

## Code

```python
#template_matching.py / 18.11.2020 / Robin Forestier
#import de la bibliothèque OpenCv et numpy
import cv2
import numpy as np

#charge l'image minecraft.jpg dans my_image
img = cv2.imread('minecraft.jpg',0)
#charge l'image a rechercher steve.jpg dans template
template = cv2.imread('steve.jpg',0)

#taille de template
w, h = template.shape[::-1]

#matching des images 
res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

threshold = 0.8

loc = np.where(res >= threshold)

#affichage des carrés noirs
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h),(0,255,255))
 
#affiche img / titre = Detected
cv2.imshow('Detected',img)

#attendre qu'une touch soit pressée
cv2.waitKey(0)
#ferme toutes les fenêtre
cv2.destroyAllWindows()
```

## Exemples

<div align="center">

<p> Original : <img src="http://172.16.32.230/Forestier/reconnaissance-visuel/raw/master/5_Programmation/test/7_template_matching/minecraft.jpg"  width="640" height="240"> </p>
<p> Template : <img src="http://172.16.32.230/Forestier/reconnaissance-visuel/raw/master/5_Programmation/test/7_template_matching/steve.jpg"  width="71" height="64"> </p>
    
<p> 
Résultat : <img src="http://172.16.32.230/Forestier/reconnaissance-visuel/raw/master/5_Programmation/test/7_template_matching/Exemples/01.png"  width="640" height="240"> 

</p>

</div>


<h2> </h2>

<div align="center">
    <i>Robin Forestier</i>
</div>
