import pygame
from random import randint
from const import *
from State import State


class Bullet(pygame.Rect):
    
    def __init__(self, screen, player):
        self.x = player.x+14
        self.y = player.y-14
        self.player = player
        self.wid = PUCK_WD_HT
        self.ht = PUCK_WD_HT
        super(Bullet, self).__init__(self.x, self.y, self.wid, self.ht)
        
        self.screen = screen

    def drawIt(self):
        pygame.draw.rect(self.screen, WHITE, (self.x, self.y, self.wid, self.ht), 0)
        self.y -= PLAYER_SPEED    
    
    def checkIt(self, player, enemy):
        for x in player.bullets:
            #player.bullets.remove(x)
            
            if (self.colliderect(enemy)):
                player.bullets.remove(x)
            
            #if (self.colliderect(player) or self.colliderect(boundTop)):
            #    self.__bullets.remove(Bullet)
        
            #if (self.colliderect(boundLeft) or self.colliderect(boundRight)):
            #    self.__bullets.remove(Bullet)   
