"""
main.py | 18.11.2020 | Robin Forestier
...
"""

#import de la bibliothèque OpenCv et numpy
import cv2
import numpy as np

from ticTacToe import TicTacToe

t = TicTacToe()

#sélection de la caméra
cap = cv2.VideoCapture(0)

#boucle infinie
while(True):
    #enregistrement de l'image dans frame
    ret, frame = cap.read()   
    
    if t.game == 0:
        frame = t.start(frame)
    if t.game == 1:
        if cv2.waitKey(1) & 0xFF == ord('w') and len(grid) == 9:
            frame = t.detetct_first(frame)
    if t.game == 2:
        if cv2.waitKey(1) & 0xFF == ord('e') and len(grid) == 9:
            frame = t.next_player(frame)
    
    frame, grid = t.detect_grid(frame)
    frame, grid = t.sort_grid(frame, grid)
    if len(grid) == 9:
        frame = t.dessine_all(frame)
    
    cv2.imshow('frame', frame)

    #si touche "q" pressée arrêt de la boucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    if cv2.waitKey(1) & 0xFF == ord('p'):
        cv2.imwrite("asd.png", frame)
        print("save")

#décharge de la mémoire
#fermeture de toutes les fenêtres
cap.release()
cv2.destroyAllWindows()