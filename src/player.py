import pygame
from const import *

class player(pygame.Rect):
    __xspeed = None
    __yspeed = None
    
    def __init__(self, xpos, ypos, wid, ht, xspeed, yspeed):
        super(player, self).__init__(xpos, ypos, wid, ht)
        self.__xspeed = xspeed
        self.__yspeed = yspeed
        self.__xpos = xpos
        self.__ypos = ypos
        self.__direction = None

    def checkIt(self, direction):
        self.__direction = direction
        if (self.__direction == "MOVE_LEFT" and self.x >= 2*BOUND_WID):
            self.x -= self.__xspeed
        elif (self.__direction == "MOVE_RIGHT" and self.x <= SCREEN_WID_HT-PLAYER_WID-2*BOUND_WID):
            self.x += self.__xspeed
        elif (self.__direction == "MOVE_UP" and self.y >= 2*BOUND_WID):
            self.y -= self.__xspeed   
        elif (self.__direction == "MOVE_DOWN" and self.y <= SCREEN_WID_HT-PLAYER_HT-2*BOUND_WID):
            self.y += self.__xspeed
        
    def getPlayerDirection(self):
        return self.__direction
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y