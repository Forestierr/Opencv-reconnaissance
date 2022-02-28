#minimax.py | 17.08.2021 | Robin Forestier

import math

class Minimax:
    def __init__(self):
        
        import ticTacToe
        self.t = ticTacToe
         
    def best_move(self, grid_play):
        best_score = -math.inf
        
        for i in range(3):
            for j in range(3):
                if grid_play[i][j] == 0:
                    grid_play[i][j] = 2
                    score = self.minimax(grid_play, 0, False)
                    grid_play[i][j] = 0
                    if score > best_score:
                        best_score = score
                        move_i = i
                        move_j = j
        
        
        grid_play[move_i][move_j] = 2
        return grid_play
    
    
    def minimax(self, grid_play, depth, isMaximising):
        t = self.t.TicTacToe()
        result = t.check_win(grid_play)
        if result is not None:
            if result == 1 : return -1
            else : return result 
        
        if isMaximising == True:
            best_score = -math.inf
            for i in range(3):
                for j in range(3):
                    #check if spot is available
                    if grid_play[i][j] == 0:
                        grid_play[i][j] = 2
                        score = self.minimax(grid_play, depth + 1, False)
                        grid_play[i][j] = 0
                        best_score = max(score, best_score)
            
            return best_score
        
        else:
            best_score = math.inf
            for i in range(3):
                for j in range(3):
                    #check if spot is available
                    if grid_play[i][j] == 0:
                        grid_play[i][j] = 1
                        score = self.minimax(grid_play, depth + 1, True)
                        grid_play[i][j] = 0
                        best_score = min(score, best_score)
            
            return best_score
        
    