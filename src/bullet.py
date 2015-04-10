import pygame
from random import randint
from const import *
from state import state

class bullet(pygame.Rect):
    __bullets = []
    
    def __init__(self, xpos, ypos, wid, ht, xspeed, yspeed, screen, state, playerDirection):
        super(bullet, self).__init__(xpos, ypos-14, wid, ht)
        self.__xpos = xpos
        self.__ypos = ypos
        self.__wid = wid
        self.__ht = ht
        self.__xspeed = xspeed
        self.__yspeed = yspeed
        self.__screen = screen
        self.__state = state
        
        self.__r = 255
        self.__g = 255
        self.__b = 255
        self.__fire = False
        
    def checkIt(self, boundLeft, boundRight, boundTop):
        for bullet in self.__bullets:        
            if (self.colliderect(boundLeft) or self.colliderect(boundRight)):
                self.__bullets.remove(bullet)
        
    def drawIt(self):
        for bullet in self.__bullets:        
            pygame.draw.rect(self.__screen, (self.__r, self.__g, self.__b), bullet)
        
    def moveIt(self, playerDirection):
        if self.__fire == True:
            if playerDirection == 'MOVE_DOWN':
                self.y += self.__yspeed
            elif playerDirection == 'MOVE_UP':
                self.y -= self.__yspeed
            elif playerDirection == 'MOVE_LEFT':
                self.x += self.__xspeed
            elif playerDirection == 'MOVE_RIGHT':
                self.x -= self.__xspeed
        
    def fire(self, playerPosX, playerPosY):
        self.__fire = True
        self.__bullets.append(self)
        print self.__bullets
        
    def update(self):
        self.drawIt()
            