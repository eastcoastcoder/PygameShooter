'''
The goal of this assignment is to accomplish a tried and true single screen arena shooter game.  
Moving and shooting will be the primary mechanics along with the prescence of hostile agents.

Inspirations: 

Crimson Land - https://youtu.be/XD_EBXpUYX0
Smash TV - https://youtu.be/n6uyWTtuYxg
Astroids - https://youtu.be/WYSupJ5r2zo
Space Invaders - https://youtu.be/437Ld_rKM2s

Specifications:
The player should be able to move and move. 
The player shoud have access to at least two weapons 
Grade Levels (applies to the specifications portion of the rubric)
A - Full control against artificial agents that are actively aggressive - Smash TV
B - More dynamic controls shooting of mobile targets that don't show intelligence (although they might move back) - Astroids
C - Simple moving and shooting against stationary or nearly stationary obstacles - Space Invaders
'''
import sys
import pygame
from const import *
from player import player
from enemy import enemy
from bullet import bullet
from state import state
from controller import controller

pygame.init()
pygame.display.set_caption("Breakout")
scoreBoard = pygame.font.SysFont( "arial", 30 )
screen = pygame.display.set_mode((SCREEN_WID_HT, SCREEN_WID_HT))
clock = pygame.time.Clock()

# Instantiate Basic Rects
boundTop = pygame.Rect(ORIGIN, ORIGIN, SCREEN_WID_HT, BOUND_WID)
boundLeft = pygame.Rect(ORIGIN, ORIGIN, BOUND_WID, SCREEN_WID_HT)
boundRight = pygame.Rect(SCREEN_WID_HT-BOUND_WID, ORIGIN, BOUND_WID, SCREEN_WID_HT)

# Instantiate Objects
gameState = state(scoreBoard, screen)
player = player(PLAYER_X, PLAYER_Y, PLAYER_WID, PLAYER_HT, PLAYER_SPEED, 0)
bullet = bullet(player.getX(), player.getY(), PUCK_WD_HT, PUCK_WD_HT, -PLAYER_SPEED, PLAYER_SPEED, screen, gameState)
enemy = enemy(screen, gameState)

def main():

    while True:
        controller(pygame.key.get_pressed(), player, bullet)
            
        bullet.checkIt(enemy, boundLeft, boundRight, boundTop)
        enemy.checkIt(bullet)
        
        bullet.move()
            
        screen.fill((BLACK))
        
        pygame.draw.rect(screen, WHITE, boundTop)
        pygame.draw.rect(screen, WHITE, boundLeft)
        pygame.draw.rect(screen, WHITE, boundRight)
        
        pygame.draw.rect(screen, RED, player)
        pygame.draw.rect(screen, WHITE, bullet)
        
        enemy.drawIt()
        #bullet.drawIt()
        
        gameState.update(enemy)
        
        if(gameState.getGameOver()):
            enemy(screen, gameState)
        
        pygame.display.flip()
                
        clock.tick(30)

if __name__ == '__main__':
    main()