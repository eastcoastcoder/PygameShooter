import pygame
from const import *
from Bullet import Bullet

class Player(pygame.Rect):
    
    def __init__(self, screen, state, xpos, ypos):
        
        self.xpos = xpos
        self.ypos = ypos
        self.wid = PLAYER_WID
        self.ht = PLAYER_HT
        super(Player, self).__init__(self.xpos, self.ypos, self.wid, self.ht)
        
        self.speed = PLAYER_SPEED
        
        self.screen = screen
        self.state = state
        
        self.direction = 'MOVE_UP'
        self.bullets = []
        
    def checkIt(self, direction):
        if (direction == "MOVE_LEFT" and self.x >= 2*BOUND_WID):
            self.x -= self.speed
        elif (direction == "MOVE_RIGHT" and self.x <= SCREEN_WID_HT-PLAYER_WID-2*BOUND_WID):
            self.x += self.speed
        elif (direction == "MOVE_UP" and self.y >= 2*BOUND_WID):
            self.y -= self.speed   
        elif (direction == "MOVE_DOWN" and self.y <= SCREEN_WID_HT-PLAYER_HT-2*BOUND_WID):
            self.y += self.speed
        self.direction = direction
        
    def getPlayerDirection(self):
        return self.direction
    
    def drawIt(self):
        pygame.draw.rect(self.screen, RED, self)
        
    def drawMoveBullets(self):
        for bullet in self.bullets:
            bullet.drawIt()
            
    def checkBullet(self, enemy):
        for bullet in self.bullets:
            enemy.checkIt(bullet, self)
    
    def fire(self):
        self.bullets.append(Bullet(self.screen, self))
        print (self.bullets)
        