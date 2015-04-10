import pygame
from const import *
from bullet import *

class player(pygame.Rect):
    
    def __init__(self, xpos, ypos, wid, ht, xspeed, yspeed, screen, state):
        super(player, self).__init__(xpos, ypos, wid, ht)
        self.__xspeed = xspeed
        self.__yspeed = yspeed
        self.__xpos = xpos
        self.__ypos = ypos
        self.__direction = ""
        self.__screen = screen
        self.__state = state
        self.__bullets = []
        
    def checkIt(self, direction):
        if (direction == "MOVE_LEFT" and self.x >= 2*BOUND_WID):
            self.x -= self.__xspeed
        elif (direction == "MOVE_RIGHT" and self.x <= SCREEN_WID_HT-PLAYER_WID-2*BOUND_WID):
            self.x += self.__xspeed
        elif (direction == "MOVE_UP" and self.y >= 2*BOUND_WID):
            self.y -= self.__xspeed   
        elif (direction == "MOVE_DOWN" and self.y <= SCREEN_WID_HT-PLAYER_HT-2*BOUND_WID):
            self.y += self.__xspeed
        self.__direction = direction
        
    def getPlayerDirection(self):
        return self.__direction
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def fire(self, playerPosX, playerPosY):
        self.__fire = True
        self.__bullets.append(bullet(self.__xpos, self.__ypos, PUCK_WD_HT, PUCK_WD_HT, -PLAYER_SPEED, PLAYER_SPEED, self.__screen, self.__state, self.getPlayerDirection()))
        
    def removeBullet(self, boundLeft, boundRight, boundTop):
        for bullet in self.bullets:        
            if (self.colliderect(boundLeft) or self.colliderect(boundRight)):
                self.bullets.remove(bullet)

    def drawMoveBullet(self):
        for bullet in self.__bullets:
            bullet.drawIt(self.__screen)
            if self.__direction == 'MOVE_DOWN':
                bullet.ypos += bullet.yspeed
            elif self.__direction == 'MOVE_UP':
                bullet.ypos -= bullet.yspeed
            elif self.__direction == 'MOVE_LEFT':
                bullet.xpos += bullet.xspeed
            elif self.__direction == 'MOVE_RIGHT':
                bullet.xpos -= bullet.xspeed
    
            