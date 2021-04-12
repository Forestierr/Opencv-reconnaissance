# Seuillage d'une image

Le seuillage ou thresholding en anglais est utile dans le traitement d’image. <br>
On peut l’utiliser pour retrouver des informations au sein d’une image ou de venir détourer un sujet dans notre image. <br>
Il existe 3 méthodes pour réaliser un seuillage d’image. 

## Simple

Le seuillage simple vient regarder la valeur du pixel si elle se trouve en dessous de la valeur de référence, le pixel serra noir sinon le pixel serra blanc.

```python
ret, thresh = cv2.threshol(img,127,255,cv2.THRESH_BINARY)
```

## Adaptif

Le lissage adaptif est très utile dans un cas ou l’image n’as pas la même luminosité partout. Elle vient réalisé une lissage par zone. <br>
Il y a deux méthodes, la première, demande comme troisième paramètre : cv2.ADAPTIVE_THRESH_GAUSSIAN_C. <br>
Elle réalisera un lissage Gaussian. La deuxième réalisera un lissage par moyenne : cv2.ADAPTIVE_THRESH_MEAN_C


```python
#Gaussian
thresh = cv2.adaptiveThreshol(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 91, 5)
#Mean
thresh2 = cv2.adaptiveThreshol(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 91, 5)
```

## Otsu

Le lissage OTSU est utilisé quand une image présente deux pique aux sein de son histogramme.

```python
blur = cv2.GaussianBlur(img,(5,5),0)
ret,th = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
```

## Exemples

<div align="center">

<p> Original : <img src="http://172.16.32.230/Forestier/reconnaissance-visuel/raw/master/5_Programmation/test/4_seuillage/sudoku.jpeg"  width="240" height="240"> </p>
    
<p> 
Simple : <img src="http://172.16.32.230/Forestier/reconnaissance-visuel/raw/master/5_Programmation/test/4_seuillage/Exemples/simple.png"  width="240" height="240"> 
Gaussian : <img src="http://172.16.32.230/Forestier/reconnaissance-visuel/raw/master/5_Programmation/test/4_seuillage/Exemples/adaptiv_gaussian.png"  width="240" height="240">
</p>

<p> 
Mean : <img src="http://172.16.32.230/Forestier/reconnaissance-visuel/raw/master/5_Programmation/test/4_seuillage/Exemples/adaptiv_mean.png"  width="240" height="240">
Otsu : <img src="http://172.16.32.230/Forestier/reconnaissance-visuel/raw/master/5_Programmation/test/4_seuillage/Exemples/otsu.png"  width="240" height="240">
</p>

</div>

<h2> </h2>

<div align="center">
    <i>Robin Forestier</i>
</div>
