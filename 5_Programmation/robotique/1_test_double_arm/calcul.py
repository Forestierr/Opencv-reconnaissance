from math import *

'''
[INFO] calcul.py | 15.04.2021 | Robin Forestier
Programme servant aux calcul des angles pour le bras du robot de Kilyan De Blasio.
'''

def calc(x):
    '''
    [INFO] calc(x) | calcul.py
    Calcul les deux angles pour le bras GAUCHE du robot de Kylian De Blasio.
    XWiki : PET'ELO
    @parma1 x => nombre de pixel jusqu'au centre de l'objet.
    return r[1,2] => 1 : angle moteur 2 || 2 : angle moteur 3
    return 0 => trop longue distance
    '''
    #number of pixel from midle to red
    x = 320 - x
    #calc distance
    x = x * 0.25
    
    #left of the screen
    if x < 80 and x > 0:
        #distance between motor and red
        p = 75 - x
        
        if p == 0:
            #in frot of the arms
            a = 90
        else :
            p = radians(p)
            m = radians(170)
            #calcul angle a
            a = atan((m/p))
        
        x = 135 - degrees(a)
        #calcul disatnce of the arms
        d = 170 / sin(a)
        d1 = sin(radians(x)) * 57
        d2 = sqrt(57**2 - d1**2)
        #d3 length between arm and object
        d3 = sqrt(d1**2 + (d - d2)**2)
        if d3 > 185 :
            #object too far away
            return 0
        else :
            #calcul angle 
            b = acos((125**2 + 60**2 - d3**2) / (2 * 125 * 60))
            c = asin((125 * sin(b)) / d3)
            c1 = acos(d1 / d3)
            c2 = asin(d2/57)
            #calcul opposite angle 
            c = 360 - (90 + (degrees(c) +  degrees(c1) + degrees(c2)))
            b = 180 - (degrees(b) - 90)
            r = [0,0]
            #return
            r[0] = int(c)
            r[1] = int(b)
            return r
    
     ###   ###   ###   ###   
    # Right of the screen #
     ###   ###   ###   ###  
    
    else :
        if x < 0:
            #negatif value
            x = x * -1
        #calcul distance
        p = 75 + x
        p = radians(p)
        m = radians(170)
        #calcul angle
        a = atan((m/p))
        x = 135 - degrees(a)
        d = 170 / sin(a)
        d1 = sin(radians(x)) * 57
        d2 = sqrt(57**2 - d1**2)
        d3 = sqrt(d1**2 + (d - d2)**2)
        if d3 > 185 :
            #objet too far away
            return 0
        else:
            #calcul angle 
            b = acos((125**2 + 60**2 - d3**2) / (2 * 125 * 60))
            c = asin((125 * sin(b)) / d3)
            c1 = acos(d1 / d3)
            c2 = asin(d2/57)
            #calcul opposite angle 
            c = 360 - (90 + (degrees(c) +  degrees(c1) + degrees(c2)))
            b = 180 - (degrees(b) - 90)
            r = [0,0]
            #return
            r[0] = int(c)
            r[1] = int(b)
            return r