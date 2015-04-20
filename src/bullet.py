import pygame
from random import randint
from const import *
from state import state


class bullet(pygame.Rect):
    
    def __init__(self, screen, player):
        self.x = player.x+14
        self.y = player.y-14
        self.player = player
        self.wid = PUCK_WD_HT
        self.ht = PUCK_WD_HT
        super(bullet, self).__init__(self.x, self.y, self.wid, self.ht)
        
        self.screen = screen

    def drawIt(self):
        #print('bullet self.xpos: ', self.xpos, 'bullet self.ypos: ', self.ypos )
        pygame.draw.rect(self.screen, WHITE, (self.x, self.y, self.wid, self.ht), 0)
        self.y -= PLAYER_SPEED    
        #self.move(self.player.getPlayerDirection())
    
    def checkIt(self, player):
        for x in player.bullets:
            player.bullets.remove(x)
    
            #if (self.colliderect(player) or self.colliderect(boundTop)):
            #    self.__bullets.remove(bullet)
        
            #if (self.colliderect(boundLeft) or self.colliderect(boundRight)):
            #    self.__bullets.remove(bullet)   
    '''
    def move(self, playerDirection):
        if playerDirection == 'MOVE_DOWN':
            self.ypos += PLAYER_SPEED
        elif playerDirection == 'MOVE_UP':
            self.ypos -= PLAYER_SPEED
        elif playerDirection == 'MOVE_LEFT':
            self.xpos += PLAYER_SPEED
        elif playerDirection == 'MOVE_RIGHT':
            self.xpos -= PLAYER_SPEED
        
    '''

