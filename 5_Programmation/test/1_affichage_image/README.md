# Lecture et affichage d'une image

Pour travailler avec OpenCv, il nous faudra une image ou une vidéo. <br>
Pour commencer nous allons simplement sélectionner une image sur notre Raspberry et l’afficher.

- Ouvrer votre IDE python (Thonny)
- ouvrer le fichier [affiche_image.py](http://172.16.32.230/Forestier/reconnaissance-visuel/blob/master/5_Programmation/test/1_affichage_image/affiche_image.py)

Dans ce cas nous allons ouvrir l'image minecraft.jpg se trouvant dans notre fichier.

## Code

```python
#affiche_image.py / 18.11.2020 / Robin Forestier
#import de la bibliothèque opencv
import cv2

#charge l'image minecraft.jpg dans my_image
my_image = cv2.imread('minecraft.jpg') 

#affiche my_image / titre = mon image
cv2.imshow('mon image', my_image)

#attendre qu'une touch soit pressée
cv2.waitKey(0)
#ferme toutes les fenêtre
cv2.destroyAllWindows()

```

## Ereur

Si vous obtenez l'erreur suivante :

>>>
`cv2.imshow('mon image', my_image)` <br>
`error : (-215:Assertion failed) size.with>0 && size.height>0 in function 'imshow' ` 
>>>

cela signifie que votre programme n'as pas réussi a ouvrire ou a trouver votre image. <br>
Vérifier que votre image se trouve bien dans le mème fichier que votre programme et que son nom et son extension son indentique dans votre programme.


<h2> </h2>

<div align="center">
    <i>Robin Forestier</i>
</div>
