import pygame
from const import *

class bullet(pygame.Rect):
   
    def __init__(self, xpos, ypos, wid, ht, xspeed, yspeed, screen, state, playerDirection):
        super(bullet, self).__init__(xpos, ypos, wid, ht)
        self.xpos = xpos
        self.ypos = ypos
        self.wid = wid
        self.ht = ht
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.__screen = screen
        self.__state = state
        
        self.__r = 255
        self.__g = 255
        self.__b = 255
        self.__fire = False
        
    def drawIt(self, screen):
        pygame.draw.rect(screen, WHITE, (self.xpos, self.ypos, self.wid, self.ht), 0)