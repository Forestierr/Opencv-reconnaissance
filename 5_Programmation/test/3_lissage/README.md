# Lissage

Le lissage est une fonctionnalité très utile est très utilisée. Elle permet par exemple de réduire le bruit. <br>
Pour lisser une image il existe plusieurs algorithmes, le plus souvent ce sont des algorithmes a box. <br>
Imaginez avoir une image de 10x10 pixels de côté, est nous devons le filtrer avec une boite de 3x3 pixels. <br>


## Code

### Average

```python
average_image = cv2.blur(img,(3,3))

#affichage
plt.imshow(average_image); plt.show()

```
### Gaussian

```python
gaussian_image = cv2.GaussianBlur(img,(3,3),0)
#affichage
plt.imshow(gaussian_image); plt.show()

```

### Median

```python
median_image = cv2.medianBlur(img,3)

#affichage
plt.imshow(median_image); plt.show()

```

### Bilateral

```python
bilateral_image = cv2.bilateralFilter(img,9,75,75)

#affichage
plt.imshow(bilateral_image); plt.show()

```

## Exemples

<div align="center">

<p> Original : <img src="http://172.16.32.230/Forestier/reconnaissance-visuel/raw/master/5_Programmation/test/3_lissage/noise.jpg"  width="240" height="240"> </p>
    
<p> 
Average : <img src="http://172.16.32.230/Forestier/reconnaissance-visuel/raw/master/5_Programmation/test/3_lissage/Exemples/average.png"  width="240" height="240"> 
Gaussian : <img src="http://172.16.32.230/Forestier/reconnaissance-visuel/raw/master/5_Programmation/test/3_lissage/Exemples/gaussian.png"  width="240" height="240">
</p>

<p> 
Median : <img src="http://172.16.32.230/Forestier/reconnaissance-visuel/raw/master/5_Programmation/test/3_lissage/Exemples/median.png"  width="240" height="240">
Bilateral : <img src="http://172.16.32.230/Forestier/reconnaissance-visuel/raw/master/5_Programmation/test/3_lissage/Exemples/bilateral.png"  width="240" height="240">
</p>

</div>

<h2> </h2>

<div align="center">
    <i>Robin Forestier</i>
</div>
