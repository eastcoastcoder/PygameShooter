from Const import *

class GameState:
    __PScore = 0
    __PLives = 5
    
    def __init__(self, scoreBoard, screen):
        self.__scoreBoard = scoreBoard
        self.__screen = screen
        self.__playerDrawScore = None
        self.__playerDrawLives = None
    
    def drawIt(self, lbl1, lbl2):
        self.__playerDrawScore = self.__scoreBoard.render(lbl1 + str(self.getPScore()), 1, WHITE)
        if (lbl2 == GAMEOVER_LBL):
            self.__playerDrawLives = self.__scoreBoard.render(lbl2, 1, WHITE)
        else:
            self.__playerDrawLives = self.__scoreBoard.render(lbl2 + str(self.getPLives()), 1, WHITE)
        self.__screen.blit(self.__playerDrawScore, (CENTER/2-50, SCORE_Y))
        self.__screen.blit(self.__playerDrawLives, (CENTER+150, SCORE_Y))
    
    # Mutators              
    def setPScore(self):
        self.__PScore += BLOCK_PT
    def setPLives(self):
        self.__PLives -= 1
    
    def resetGame(self):
        self.__PScore = 0
        self.__PLives = 5
    
    # Acessors
    def getPScore(self):
        return self.__PScore
    def getPLives(self):
        return self.__PLives
    
