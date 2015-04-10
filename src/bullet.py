import pygame
from random import randint
from const import *
from state import state

class bullet(pygame.Rect):

    def __init__(self, xpos, ypos, wid, ht, xspeed, yspeed, screen, state):
        super(bullet, self).__init__(xpos, ypos, wid, ht)
        self.__xpos = xpos
        self.__ypos = ypos
        self.__wid = wid
        self.__ht = ht
        self.__xspeed = xspeed
        self.__yspeed = yspeed
        self.__screen = screen
        self.__state = state
        self.__direction = None
        self.__fire = False
        self.bullets = []
        
    def checkIt(self, enemy, boundLeft, boundRight, boundTop):
        for bullet in self.bullets:
            if (self.colliderect(boundLeft) or self.colliderect(boundRight) or self.colliderect(boundTop) or self.colliderect(enemy)):
                self.remove(bullet)
    
    def remove(self, bullet):
        self.bullets.remove(bullet)
        print 'rm'
        
    def drawIt(self):
        for bullet in self.bullets:
            pygame.draw.rect(self.__screen, WHITE, bullet)
            
    def moveIt(self):
        if self.__fire == True:
            if self.__direction == 'MOVE_DOWN':
                self.y += self.__yspeed
            elif self.__direction == 'MOVE_UP':
                self.y -= self.__yspeed
            elif self.__direction == 'MOVE_LEFT':
                self.x += self.__xspeed
            elif self.__direction == 'MOVE_RIGHT':
                self.x -= self.__xspeed
        
    def fire(self, player, direction):
        self.__fire = True
        self.__direction = direction
        self.bullets.append(bullet(player.getX(), player.getY(), PUCK_WD_HT, PUCK_WD_HT, -PLAYER_SPEED, PLAYER_SPEED, self.__screen, self.__state))
        self.drawIt()
        print self.bullets
        
            