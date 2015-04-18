import pygame
from random import randint
from const import *
from state import state

class bullet(pygame.Rect):
    
    def __init__(self, screen, player):
        self.xpos = player.x+14
        self.ypos = player.y-14
        self.player = player
        self.wid = PUCK_WD_HT
        self.ht = PUCK_WD_HT
        super(bullet, self).__init__(self.xpos, self.ypos, self.wid, self.ht)
        
        self.screen = screen

    def drawIt(self):
        pygame.draw.rect(self.screen, WHITE, (self.xpos, self.ypos, self.wid, self.ht), 0)
        self.ypos -= 20


            #if (bullet.colliderect(enemy)):
            #    player.bullets.remove(bullet)
            
            #if (bullet.colliderect(enemy)):
            #    self.bullets.remove(bullet)   
            #    print("Removed")
    
    '''
    def checkPuck(self, player, boundLeft, boundRight, boundTop):
        for bullet in self.__bullets:
            self.__bullets.remove(bullet)
    
            #if (self.colliderect(player) or self.colliderect(boundTop)):
            #    self.__bullets.remove(bullet)
        
            if (self.colliderect(boundLeft) or self.colliderect(boundRight)):
                self.__bullets.remove(bullet)   
    
    def move(self, playerDirection):
        if self.__fire == True:
            if playerDirection == 'MOVE_DOWN':
                self.y += self.__yspeed
            elif playerDirection == 'MOVE_UP':
                self.y -= self.__yspeed
            elif playerDirection == 'MOVE_LEFT':
                self.x += self.__xspeed
            elif playerDirection == 'MOVE_RIGHT':
                self.x -= self.__xspeed
        
    '''   
            