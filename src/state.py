from const import *
import pygame
from enemy import enemy

class state:
    
    def __init__(self, scoreBoard, screen):
        self.__scoreBoard = scoreBoard
        self.__screen = screen
        self.__playerDrawScore = None
        self.__playerDrawLives = None
        self.__PScore = 0
        self.__PLives = 5
        self.__gameOver = False
    
    def drawIt(self, lbl1, lbl2):
        self.__playerDrawScore = self.__scoreBoard.render(lbl1 + str(self.getPScore()), 1, WHITE)
        if (lbl2 == GAMEOVER_LBL):
            self.__playerDrawLives = self.__scoreBoard.render(lbl2, 1, WHITE)
        else:
            self.__playerDrawLives = self.__scoreBoard.render(lbl2 + str(self.getPLives()), 1, WHITE)
        self.__screen.blit(self.__playerDrawScore, (CENTER/2-50, SCORE_Y))
        self.__screen.blit(self.__playerDrawLives, (CENTER+150, SCORE_Y))
    
    def update(self, enemy):
        if (self.__PLives == 0 or enemy.getRemaining() == 0):
            self.drawIt(SCORE_LBL, GAMEOVER_LBL)
            
            self.__gameOver = True
            
            pygame.display.flip()
            pygame.time.delay(3000)
            self.resetGame()
        else:
            self.drawIt(SCORE_LBL, LIVES_LBL)
    
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
    def getGameOver(self):
        return self.__gameOver
