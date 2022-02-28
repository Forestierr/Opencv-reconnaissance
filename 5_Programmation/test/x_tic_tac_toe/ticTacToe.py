"""
ticTacToe.py | 12.08.2021 | Robin Forestier
"""

import cv2
import numpy as np
import random

from minimax import Minimax

m = Minimax()

RANDOM_PLAYER = False
RANDOM_HARD = True
AI_PLAYER = False

class TicTacToe:
    def __init__(self):
        self.game = 0
        self.grid = []
        self.grid_play = [[0,0,0],[0,0,0],[0,0,0]] #1 or 2
        self.player = 0 # player 1 or 2
        self.p1_forme = False #false = rond / true = croix
        self.shape_detect = None
    
    #game 0
    def start(self, frame):
        if self.game != 0:
            print("[INFO] Game already lauched.")
        else:
            if len(self.grid) != 9:
                #print("[GAME] Try to detect the grid.")
                frame, self.grid = self.detect_grid(frame)
                frame , self.gride = self.sort_grid(frame, self.grid)
                return frame
            print("[GAME] Grid detect, Game start !")
            self.game = 1
            #detetct_first(frame)
        return frame
    
    #game 1       
    def detetct_first(self, frame):
        if self.game == 0:
            print("[INFO] Game not lauched")
            self.start(frame)
        elif self.game != 1:
            print("[ERROR] detect first case already done")
        else:
            if self.player == 2 :
                self.game = 2
                self.next_player(frame)
                
            self.player = 1
            frame, self.shape_detect  = self.detect_shape(frame, self.grid)
            if self.shape_detect is not None:
                if self.shape_detect == 0 :
                    self.p1_forme = False
                    print("[GAME] Le joueur 1 à les  O .")
                else :
                    self.p1_forme = True
                    print("[GAME] Le joueur 1 à les  X .")
                self.player = 2
                self.game = 2
                
            return frame
            
    #game 2        
    def next_player(self, frame):
        if self.game < 2 :
            print("[ERROR] game not started properly")
            start(frame)
        elif self.game != 2 :
            print("[ERROR] game faild")
        else:
            if self.player == 1:
                print("[GAME] C'est a Player : {} de jouer !".format(self.player))
                
                frame, self.shape_detect  = self.detect_shape(frame, self.grid)
                if self.shape_detect is not None:    
                    ret = self.check_win(self.grid_play)
                    if ret is not None:
                        if ret == 0 : print("[GAME] ## Tie ##")
                        else : print("[Game] ## Player ", self.player, " WIN ##")
                        cv2.imshow("frame", frame)
                        cv2.waitKey(-1)
                    
                    if self.player == 1: self.player = 2
                    else : self.player = 1
                        
            elif AI_PLAYER:
                self.grid_play = m.best_move(self.grid_play)
                ret = self.check_win(self.grid_play)
                if ret is not None:
                    if ret == 0 : print("[GAME] ## Tie ##")
                    else: print("[Game] ## Player ", self.player, " WIN ##")
                    cv2.imshow("frame", frame)
                    cv2.waitKey(-1)
                
                if self.player == 1: self.player = 2
                else : self.player = 1
            
            elif RANDOM_PLAYER:
                self.rand_player()
                ret = self.check_win(self.grid_play)
                if ret is not None:
                    if ret == 0 : print("[GAME] ## Tie ##")
                    else: print("[Game] ## Player ", self.player, " WIN ##")
                    cv2.imshow("frame", frame)
                    cv2.waitKey(-1)
                        
                if self.player == 1: self.player = 2
                else : self.player = 1
                     
                
            else:
                print("[GAME] C'est a Player : {} de jouer !".format(self.player))
                
                frame, self.shape_detect  = self.detect_shape(frame, self.grid)
                if self.shape_detect is not None:    
                    if self.player == 1: self.player = 2
                    else : self.player = 1
                    ret = self.check_win(self.grid_play)
                    if ret is not None:
                        print(ret)
                        cv2.imshow("frame", frame)
                        cv2.waitKey(-1)
            
        return frame
      
    def rand_player(self):
        ret = 0
        if RANDOM_HARD == True:
            ret = self.rand_check_win()
        
        if ret == 0:
            i = random.randint(0,2)
            j = random.randint(0,2)
            
            if self.grid_play[i][j] == 0:
                self.grid_play[i][j] = self.player
            
            else:
                self.rand_player()
            
    
    def rand_check_win(self):
        for i in range(3):
            for j in range(3):
                if self.grid_play[i][j] == 0:
                    self.grid_play[i][j] = self.player
                    result = self.check_win(self.grid_play)
                    if result is None:
                        self.grid_play[i][j] = 0
                    else:
                        return 1
                    
        if self.player == 1: self.player = 2
        else : self.player = 1
                    
        for i in range(3):
            for j in range(3):
                if self.grid_play[i][j] == 0:
                    self.grid_play[i][j] = self.player
                    result = self.check_win(self.grid_play)
                    if result is None:
                        self.grid_play[i][j] = 0
                    else:
                        if self.player == 1: self.player = 2
                        else : self.player = 1
                        self.grid_play[i][j] = self.player
                        return 1 
        
        if self.player == 1: self.player = 2
        else : self.player = 1
        return 0
    
    
    def check_win(self, grid_play):
        """
        win 0 -> tie
        win 1 -> player 1
        win 2 -> player 2
        """
        win = None
    
        if grid_play[0][0] == grid_play[1][1] and grid_play[0][0] == grid_play[2][2] and grid_play[0][0] != 0:
            #print("[Game] ## Player : ", grid_play[1][1], " win ##")
            win = grid_play[1][1]
            
        elif grid_play[0][2] == grid_play[1][1] and grid_play[0][2] == grid_play[2][0] and grid_play[0][2] != 0:
            #print("[Game] ## Player : ", grid_play[1][1], " win##")
            win = grid_play[1][1]
        
        else:
            for i in range(3):
                if (len(set(grid_play[i]))==1) and grid_play[i] != [0,0,0]:
                    #print("[Game] ## Player : ", grid_play[i][0], " win ##")
                    win = grid_play[i][0]
                
                if grid_play[0][i] == grid_play[1][i] and grid_play[0][i] == grid_play[2][i] and grid_play[0][i] != 0:
                    #print("[Game] ## Player : ", grid_play[0][i], " win ##")
                    win = grid_play[0][i]
        
        if not 0 in grid_play[0] and not 0 in grid_play[1] and not 0 in grid_play[2] and win == None:
            #print("[GAME] ## TIE ##")
            win = 0
        
        return win
    
    def draw_win_line(self, frame, grid1, grid2):
        x,y,w,h = grid1
        c_x1 = int((x + (x + w)) / 2)
        c_y1 = int((y + (y + h)) / 2)
                
        x2,y2,w2,h2 = grid2
        c_x2 = int((x2 + (x2 + w2)) / 2)
        c_y2 = int((y2 + (y2 + h2)) / 2)
        
        frame = cv2.line(frame, (c_x1, c_y1), (c_x2, c_y2), (0,0,255), 5)
                
        return True, frame 
    
    def detect_grid(self, frame):
        self.grid.clear()
        #convertion de l'image en nuance de gris
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #egalisation de l'histogramme
        gray = cv2.equalizeHist(gray)
        #threshold
        _, thresh = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
        #sup noise
        kernel = np.ones((5,5),np.uint8)
        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        #detect contour
        
        contours, hierarchy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        hierarchy = hierarchy[0]
        for i in zip(contours, hierarchy):
            currentContours = i[0]
            currentHierarchy = i[1]   
            x, y, w, h = cv2.boundingRect(currentContours)
            
            #contour intern
            if currentHierarchy[0] > 0 or (currentHierarchy[0] == -1 and currentHierarchy[1] > 0):
                #cv2.putText(frame, str(currentHierarchy), (x, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,0), 1) #show hierarchy
                cv2.rectangle(frame, (x,y), (x+w,y+h),(255,0,0),2)
                self.grid.append([x,y,w,h])
        return frame, self.grid        
                
    def sort_grid(self, frame, grid):
        self.grid = sorted(self.grid, key=lambda l:l[1])
        self.grid[0:3] = sorted(self.grid[0:3], key=lambda l:l[0])
        self.grid[3:6] = sorted(self.grid[3:6], key=lambda l:l[0])
        self.grid[6:9] = sorted(self.grid[6:9], key=lambda l:l[0])
        c = 0
        """
        #show number on the gride
        for i in self.grid:
            x, y, h, w = i
            frame = cv2.putText(frame, str(c), (x + 30,y + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, 255)
            c += 1
        """
        return frame, self.grid

    
    def detect_shape(self, frame, grid):
        c = 0
        n_dot = 0
        self.shape_detect = None
        
        for i in range(3):
            for j in range(3):
                x,y,w,h = grid[c]

                if self.grid_play[i][j] == 0:
                    roi = frame[y:y+h, x:x+w]
                    roiG = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
                    gray = cv2.equalizeHist(roiG)
             
                    #Cirlce
                    circles = cv2.HoughCircles(roiG, cv2.HOUGH_GRADIENT, 1, 50,
                                                param1=50, param2=30, minRadius=20, maxRadius=300)
                            
                    if circles is not None:
                        self.grid_play[i][j] = self.player
                        frame = self.dessine(frame, grid, c)
                        #print(self.grid_play)
                        self.shape_detect = 0
                    
                    #crois
                    else :
                        roi = frame[y:y+h, x:x+w]
                        roiG = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
                        gray = cv2.equalizeHist(roiG)
                        _, th = cv2.threshold(roiG, 30, 255,cv2.THRESH_BINARY_INV)
                        
                        contours,hierarchy = cv2.findContours(th,2,1)
                        
                        if len(contours) > 0:
                            cnt = max(contours, key = cv2.contourArea)
                            
                            """
                            perimetre = cv2.arcLength(cnt, True)
                            approx = cv2.approxPolyDP(cnt, 0.01*perimetre, True)
                            print(len(approx))
                            cv2.imshow("th",th)
                            cv2.waitKey(0)
                            """
                            
                            hull = cv2.convexHull(cnt,returnPoints = False)
                            defects = cv2.convexityDefects(cnt,hull)
                            if defects is not None:
                                n_dot = 0
                                for x in range(defects.shape[0]):
                                    s,e,f,d = defects[x,0]
                                    start = tuple(cnt[s][0])
                                    end = tuple(cnt[e][0])
                                    far = tuple(cnt[f][0])
                                    #cv2.line(roi,start,end,[0,255,0],2)
                                    #cv2.circle(roi,far,5,[0,0,255],-1)
                                    
                                    if far is not None: n_dot += 1
                                    
                                if n_dot == 4:
                                    self.grid_play[i][j] = self.player
                                    frame = self.dessine(frame, grid, c)
                                    #print(self.grid_play)
                                    self.shape_detect = 1

                c += 1       
        return frame, self.shape_detect
                    
        
    
    def dessine(self, frame, grid, n_grid):
        x, y, w, h = self.grid[n_grid]
        
        if self.p1_forme:
            frame = cv2.line(frame, (x,y), (x + w, y + h), (255,125,0), 3)
            frame = cv2.line(frame, (x,y + h), (x + w,y), (255,125,0), 3)
        
        else:
            center_x = int((x + (x + w)) / 2)
            center_y = int((y + (y + h)) / 2)
            
            if y + h < x + w :
                radius = int(((y + h) - y) / 2)
            else :
                radius = int(((x + w) - x) / 2)
            
            frame = cv2.circle(frame, (center_x, center_y) , radius - 20, (255,0,255), 3)
            
        return frame
        
        
    def dessine_all(self, frame):
        """
        self.player = 0 # player 1 or 2
        self.p1_forme = False #false = rond / true = croix
        """
        pose = 0
        
        for i in range(3):
            for j in range(3):
                if (self.grid_play[i][j] == 1 and self.p1_forme == True) or (self.grid_play[i][j] == 2 and self.p1_forme == False):
                    frame = self.draw_croix(frame, self.grid[pose], (255,255,0), 3) 
                elif self.grid_play[i][j] != 0:
                    frame = self.draw_rond(frame, self.grid[pose], (255,0,255), 3)
                else :
                    pass
                pose += 1
            
        return frame
        
    def draw_croix(self, frame, loc, color, thinkness):
        x, y, w, h = loc
        frame = cv2.line(frame, (x,y), (x + w, y + h), color, thinkness)
        frame = cv2.line(frame, (x,y + h), (x + w,y), color, thinkness)
            
        return frame
        
    def draw_rond(self, frame, loc, color, thinkness):
        x,y,w,h = loc
        center_x = int((x + (x + w)) / 2)
        center_y = int((y + (y + h)) / 2)
                    
        if y + h < x + w :
            radius = int(((y + h) - y) / 2)
        else :
            radius = int(((x + w) - x) / 2)
        
        if (radius - 20) <= 0 : radius = 20
        
        frame = cv2.circle(frame, (center_x, center_y) , radius - 20, color, thinkness)
            
        return frame