# Utilisation de la souris

Le but est d'utiliser la souris pour selectionner un bout de mon image.

## Code

```python
'''
[INFO]
souris.py / 12.04.2021 / Robin Forestier
But : utiliser la souris pour sélectionner un buot de l'image.
'''
#import de la bibliothèque opencv
import cv2
import numpy as np

point = []

def selection(event, x, y, flags, param):
    print(param)
    global point
    
    if event == cv2.EVENT_LBUTTONDOWN:
        point = [(x,y)]
        
    elif event == cv2.EVENT_LBUTTONUP:
        point.append((x,y))
        
        cv2.rectangle(img, point[0], point[1],(255,0,0),2)
        

if __name__ == "__main__":
    #img = cv2.imread('minecraft.jpg')
    img = cv2.imread('minecraft.jpg')
    clone = img.copy()
    #img = np.zeros((512,512,3), np.uint8)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', selection)
    
    while True:
        cv2.imshow('image', img)
        
        if cv2.waitKey(20) & 0xff == 27:
            break
        
        if cv2.waitKey(1) & 0xff == ord('r'):
            img = clone.copy()
    
    cv2.destroyAllWindows()
```


<h2> </h2>

<div align="center">
    <i>Robin Forestier</i>
</div>
